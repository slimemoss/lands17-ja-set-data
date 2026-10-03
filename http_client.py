from datetime import timedelta
import requests_cache

# キャッシュセッションの設定
# URLパターンごとに個別のTTL（有効期限）を設定
session = requests_cache.CachedSession(
    cache_name='cache_data/http_cache',
    backend='sqlite',
    urls_expire_after={
        '*17lands.com*': timedelta(hours=1),            # 17lands filters: 新セットの反映を検知するため1時間
        '*api.scryfall.com/sets*': timedelta(hours=12), # Scryfall セット一覧: 12時間
        '*api.scryfall.com/bulk-data*': timedelta(hours=12), # Scryfall bulk metadata: 12時間
        '*data.scryfall.io*': timedelta(days=7),        # Scryfall bulkデータ本体(jsonl.gz): 7日間
        '*': timedelta(hours=1),                        # その他デフォルト: 1時間
    },
)

# Scryfall等のAPI要件を満たすUser-Agentヘッダー
session.headers.update({
    'User-Agent': 'slimemoss/1.0 (contact: x.com/slimemoss2)'
})


def get(url: str, **kwargs):
    """キャッシュ付きGETリクエストを実行します。"""
    resp = session.get(url, **kwargs)
    if not resp.from_cache:
        print(f'Download: {url}')
    return resp
