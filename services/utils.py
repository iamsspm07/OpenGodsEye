from urllib.parse import urlparse

def get_domain(url):
    try:
        return urlparse(url).netloc.lower()
    except:
        return ""

def deduplicate(results):
    seen = set()
    unique = []
    for r in results:
        link = r.get("link")
        if link and link not in seen:
            seen.add(link)
            unique.append(r)
    return unique