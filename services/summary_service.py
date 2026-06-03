def generate_summary(data):
    social = len(data.get("social_media", []))
    dev = len(data.get("developer_profiles", []))
    content = len(data.get("content_platforms", []))
    community = len(data.get("community_platforms", []))
    media = len(data.get("media_platforms", []))

    metrics = data.get("metrics", {})
    confidence = metrics.get("identity_confidence", 0)
    risk = metrics.get("risk_flag", "Unknown")

    total_profiles = social + dev + content + community + media

    if total_profiles > 10:
        presence = "very strong"
    elif total_profiles > 5:
        presence = "strong"
    elif total_profiles > 2:
        presence = "moderate"
    else:
        presence = "limited"

    if dev > social:
        focus = "technical/developer-focused"
    elif social > dev:
        focus = "socially active"
    else:
        focus = "balanced presence"

    if content > 2:
        content_status = "active content creator"
    elif content > 0:
        content_status = "occasional content publishing"
    else:
        content_status = "no significant content publishing"

    return (
        f"{presence.capitalize()} digital presence with {focus}. "
        f"{content_status}. "
        f"Identity confidence is {round(confidence,2)} with a {risk.lower()} risk profile."
    )