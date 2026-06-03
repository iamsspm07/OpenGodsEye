# 🧠 Detect behavior dynamically
def detect_behavior(data):
    social = len(data.get("social_media", []))
    dev = len(data.get("developer_profiles", []))
    content = len(data.get("content_platforms", []))
    community = len(data.get("community_platforms", []))

    if dev > social and dev > content:
        return "Tech-focused, developer activity"

    elif content > 2:
        return "Content creator / blogger"

    elif social > dev:
        return "Socially active user"

    elif community > 2:
        return "Community-driven participant"

    else:
        return "Balanced digital presence"


# 📊 Compute metrics
def compute_metrics(profiles, total, categorized=None):
    matched = [p for p in profiles if p["confidence"] > 0.5]

    metrics = {
        "search_accuracy": f"{int(len(matched) / total * 100) if total else 0}%",
        "identity_confidence": round(
            sum(p["confidence"] for p in matched) / len(matched), 2
        ) if matched else 0,
        "profiles_linked": len(matched),
        "possible_fake_accounts": len(profiles) - len(matched),
        "risk_flag": "Low" if len(matched) > 1 else "Medium"
    }

    # ✅ Dynamic behavior
    if categorized:
        metrics["behavior_pattern"] = detect_behavior(categorized)
    else:
        metrics["behavior_pattern"] = "Unknown"

    return metrics