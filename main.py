import datetime

from lands17 import codes
from public_data import ImageUrl, ImageUrlI, ImageUrlsI
from scryfall import cards, sets
from scryfall.sets_scheme import Datum, SetType


def target_sets(data: list[Datum]):
    def target_filter(d: Datum):
        res = True
        res &= d.released_at > datetime.datetime(2023, 1, 1) or d.code == 'spg'
        res &= d.set_type in [SetType.EXPANSION,
                              SetType.CORE, SetType.DRAFT_INNOVATION]
        res &= d.parent_set_code == None
        res &= d.code in codes.get_codes()
        return res

    return [d for d in data if target_filter(d)]


def incomplete_sets(scryfall_data: list[Datum]):
    res: list[str] = []

    for target in target_sets(scryfall_data):
        url_file = ImageUrl(target.code)
        url_data = url_file.read()

        if url_data.scryfall_card_count < target.card_count:
            res.append(target.code)

    return res


def main():
    sets_data = sets.get()
    target_codes = incomplete_sets(sets_data)

    if len(target_codes) == 0:
        print('更新すべきセットはありません。')
        return
    else:
        print('次のセットを更新します。: {}'.format(target_codes))

    cards_by_set = cards.classify_by_set(cards.get())
    for code in target_codes:
        url_list = [ImageUrlI.from_scryfall(card)
                    for card in cards_by_set[code]]

        card_count = [d for d in sets_data if d.code == code][0].card_count

        ImageUrl(code).write(ImageUrlsI(
            data=url_list, scryfall_card_count=card_count))


if __name__ == '__main__':
    main()
