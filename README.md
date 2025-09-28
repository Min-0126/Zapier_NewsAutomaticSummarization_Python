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


## Author

Jongmin Kim

email: minha0126@proton.me


