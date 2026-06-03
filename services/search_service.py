import requests, os
from services.utils import deduplicate

def search_serpapi(query):
    api_key = os.getenv("SERP_API_KEY")

    if not api_key:
        # fallback mock
        return [
            {"title": f"{query} LinkedIn", "link": "https://linkedin.com/in/sample"},
            {"title": f"{query} GitHub", "link": "https://github.com/sample"}
        ]

    try:
        res = requests.get(
            "https://serpapi.com/search",
            params={"q": query, "api_key": api_key}
        ).json()

        return [
            {
                "title": r.get("title"),
                "link": r.get("link"),
                "snippet": r.get("snippet","")
            }
            for r in res.get("organic_results", [])
        ]
    except:
        return []

def multi_search(name):
    queries = [
        name,
        f'"{name}" LinkedIn',
        f'"{name}" GitHub',
        f'"{name}" Kaggle',
        f'"{name}" Instagram',
        f'"{name}" site:linkedin.com',
        f'"{name}" site:github.com',
        f'"{name}" site:medium.com',
        f'"{name}" developer'
    ]

    results = []
    for q in queries:
        results.extend(search_serpapi(q))

    return deduplicate(results)