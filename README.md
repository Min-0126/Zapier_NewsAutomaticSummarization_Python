# Zapier News Automation (Python + News API)
The project utilizes Zapier to automatically send a summary of the latest articles in a specific area.

It collects the recent news based on the keywords I provided, and aligns the items according to news title, summary, and URL.

The programming language 'Python' is used.


## Features

  **Keyword Research**: Using 'News API' and 'everything' endpoint.

  **Structured Output**: Returns titles[], descriptoin[], and urls[] arrays for easy Formatter mapping

  **Flexible Input**: Accepts either 'n' or 'max_result' as the number of resutls to fetch.

  **Zapier-Compatible**: Follows 'input_data' and 'output' standards for Code by Zapier

  **Latest-First Sorting**: Uses 'sortBy=publishedAt' to return the most recent articles first.


## Workflow
1. Trigger
2. Action -> Run Python
3. Create Line Itemizer
4. AI Summarization and Email Delivery

## Requirements

+ Zapier
+ NewsAPI Key
+ Outbound Internet access

## Input Fields
+ API Key  => My NewsAPI Key
+ Keyword  => Certain topic
+ max_results => Number of Results
+ n -> Number of News collect

## Output Fields
```
{
  "keyword": "AI", 
  "count": 5,
  "titles": ["Title 1", "Title 2", "..."], 
  "descriptions": ["Description 1", "Description 2", "..."], 
  "urls": ["https://...", "https://...", "..."] 
}
```

## Zapier Setup Summary
1. Trigger:
   + Schedule by Zapier -> Every day at 8:00AM
2. Action - Zapier (Run Python)
   + Input Data
       + API_key
       + Keyword
       + N: 5
    + Code: Paste the script from Zapier_Automation.py
    
3. Action - Formatter (Utilities -> Create Line Itemizer)
  + Line-items Group Name: articles
      + Line-item Properties:
          + title -> titles
          + description -> descriptions
          + url -> urls

4. AI by Zapier (Analyze and Return Data)
   + Model: openai/gpt-40-mini
   + Prompt:
       + News Analysis and Grouping
       + Summary Structure
       + Tweet Writing Guideline
       + Topic: Content Structure
       + Language and Tone
       + Hashtags and Final Check

5. Email
    + Send outbound email
    + Use Output from Step 4

## API reference
Endpoint: https://newsapi.org/v2/everything

## Security
Keep api_key in Zapier Secrets and never expose it in code or screenshots

## Code
```
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
```

## Author

Jongmin Kim (Min)

email: minha0126@proton.me


