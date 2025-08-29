import requests, json
from requests.exceptions import RequestException

def get_news(api_key, keyword, max_results):
    url = "https://newsapi.org/v2/everything"
    params = {"q": keyword, "apiKey": api_key, "language": "ko", "pageSize": max_results, "sortBy": "publishedAt"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    arts = data.get("articles", [])

    titles = [(a.get("title") or "").strip() for a in arts]
    descriptions = [(a.get("description") or "").strip() for a in arts]
    urls = [(a.get("url") or "").strip() for a in arts]

    #다음 스텝들에서 쓰기 쉽도록 keyword와 개수도 함께 반환
    return {
        "keyword": keyword,
        "count": len(arts),
        "titles": titles,
        "descriptions": descriptions,
        "urls": urls
    }

api_key = input_data.get("api_key")
keyword = input_data.get("keyword")            # 스텝의 Input Data(예: 'AI')를 그대로 씀

# n 또는 max_results 어느 쪽이든 받기
max_results = input_data.get("n", input_data.get("max_results", 5))

try:
    max_results = int(max_results)
except Exception:
    max_results = 5

output = get_news(api_key, keyword, max_results)
