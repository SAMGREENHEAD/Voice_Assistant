# app/commands/news.py

import requests

def get_news():
    api_key = "your_news_api_key"  # Replace with your actual News API key
    base_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(base_url)
    articles = response.json()["articles"]
    
    if articles:
        headlines = [article["title"] for article in articles[:5]]  # Get top 5 headlines
        return "Here are the top 5 news headlines: " + "; ".join(headlines)
    else:
        return "Sorry, I couldn't retrieve the news at this moment."
