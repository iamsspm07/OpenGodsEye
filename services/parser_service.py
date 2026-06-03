# from services.platform_registry import PLATFORM_REGISTRY
# from services.utils import get_domain
# import re
#
#
# # 🔍 Match platform safely
# def match_platform(link):
#     domain = get_domain(link)
#
#     for key, value in PLATFORM_REGISTRY.items():
#         if key in domain:
#             return value
#
#     return ("Unknown", "other")
#
#
# # 🧹 Remove duplicates
# def deduplicate(profiles):
#     seen = set()
#     unique = []
#
#     for p in profiles:
#         if p["url"] not in seen:
#             seen.add(p["url"])
#             unique.append(p)
#
#     return unique
#
#
# # 📊 Extract & categorize platforms
# def extract_platforms(results):
#
#     categories = {
#         "social_media": [],
#         "developer_profiles": [],
#         "professional_presence": [],
#         "content_platforms": [],
#         "community_platforms": [],
#         "media_platforms": [],
#         "other_websites": []
#     }
#
#     for r in results:
#         link = r.get("link", "")
#         conf = r.get("confidence", 0)
#
#         name, category = match_platform(link)
#
#         entry = {
#             "platform": name,
#             "url": link,
#             "confidence": conf
#         }
#
#         # 🎯 Smart categorization
#         if category == "social":
#             categories["social_media"].append(entry)
#         elif category == "developer":
#             categories["developer_profiles"].append(entry)
#         elif category == "professional":
#             categories["professional_presence"].append(entry)
#         elif category == "content":
#             categories["content_platforms"].append(entry)
#         elif category == "community":
#             categories["community_platforms"].append(entry)
#         elif category == "media":
#             categories["media_platforms"].append(entry)
#         else:
#             categories["other_websites"].append(entry)
#
#     # 🧹 Deduplicate all categories
#     for key in categories:
#         categories[key] = deduplicate(categories[key])
#
#     return categories
#
#
# # #️⃣ Extract hashtags
# def extract_hashtags(titles):
#     tags = []
#
#     for t in titles:
#         tags += re.findall(r"#\w+", t)
#
#     return list(set(tags))


from services.platform_registry import PLATFORM_REGISTRY
from services.utils import get_domain
import re


# 🔍 Match platform safely
def match_platform(link):
    domain = get_domain(link)

    # Clean domain (remove www, ports)
    if domain:
        domain = domain.replace("www.", "").split(":")[0]

    # Match known platforms
    for key, value in PLATFORM_REGISTRY.items():
        if key in domain:
            return value

    # ✅ Return domain instead of "Unknown"
    return (domain if domain else "Unknown", "other")


# 🧹 Remove duplicates
def deduplicate(profiles):
    seen = set()
    unique = []

    for p in profiles:
        url = p.get("url")

        if url and url not in seen:
            seen.add(url)
            unique.append(p)

    return unique


# 📊 Extract & categorize platforms
def extract_platforms(results):

    categories = {
        "social_media": [],
        "developer_profiles": [],
        "professional_presence": [],
        "content_platforms": [],
        "community_platforms": [],
        "media_platforms": [],
        "other_websites": []
    }

    for r in results:
        link = r.get("link", "")
        conf = r.get("confidence", 0)

        if not link:
            continue

        name, category = match_platform(link)

        entry = {
            "platform": name,
            "url": link,
            "confidence": conf
        }

        # 🎯 Categorization
        if category == "social":
            categories["social_media"].append(entry)

        elif category == "developer":
            categories["developer_profiles"].append(entry)

        elif category == "professional":
            categories["professional_presence"].append(entry)

        elif category == "content":
            categories["content_platforms"].append(entry)

        elif category == "community":
            categories["community_platforms"].append(entry)

        elif category == "media":
            categories["media_platforms"].append(entry)

        else:
            categories["other_websites"].append(entry)

    # 🧹 Deduplicate all categories
    for key in categories:
        categories[key] = deduplicate(categories[key])

    return categories


# #️⃣ Extract hashtags
def extract_hashtags(titles):
    tags = []

    for t in titles:
        if not t:
            continue

        tags.extend(re.findall(r"#\w+", t))

    return list(set(tags))