import streamlit as st
import requests

# 🔗 Your FastAPI endpoint
API_URL = "http://127.0.0.1:8000/intelligence"

# ⚙️ Page config
st.set_page_config(
    page_title="GodsEye Tracker",
    layout="wide",
    page_icon="🧠"
)

# 🧠 Title
st.title("🧠 GodsEye - Digital Presence Tracker")
st.markdown("Track social, developer, and web presence across the internet")

# 🔍 Input
name = st.text_input("Enter Name", "Sujit Shibaprasad Maity")

# 🚀 Search button
if st.button("Search 🔍"):

    with st.spinner("🔎 Scanning global internet..."):

        try:
            response = requests.get(API_URL, params={"name": name})
            data = response.json()
        except Exception as e:
            st.error("❌ Backend not running or error occurred")
            st.stop()

    st.success("✅ Analysis Complete")

    # =========================
    # 🌐 SOCIAL MEDIA
    # =========================
    st.subheader("🌐 Social Media")
    social = data.get("social_media", [])
    if social:
        for p in social:
            st.markdown(f"• **{p['platform']}** → [Open Profile]({p['url']})")
    else:
        st.write("No data found")

    # =========================
    # 👨‍💻 DEVELOPER PROFILES
    # =========================
    st.subheader("👨‍💻 Developer Profiles")
    dev = data.get("developer_profiles", [])
    if dev:
        for p in dev:
            st.markdown(f"• **{p['platform']}** → [Open Profile]({p['url']})")
    else:
        st.write("No data found")

    # =========================
    # 💼 PROFESSIONAL
    # =========================
    st.subheader("💼 Professional Presence")
    prof = data.get("professional_presence", [])
    if prof:
        for p in prof:
            st.markdown(f"• **{p['platform']}** → [View]({p['url']})")
    else:
        st.write("No data found")

    # =========================
    # ✍️ CONTENT
    # =========================
    st.subheader("✍️ Content Platforms")
    content = data.get("content_platforms", [])
    if content:
        for p in content:
            st.markdown(f"• **{p['platform']}** → [Read]({p['url']})")
    else:
        st.write("No data found")

    # =========================
    # 💬 COMMUNITY
    # =========================
    st.subheader("💬 Community Platforms")
    community = data.get("community_platforms", [])
    if community:
        for p in community:
            st.markdown(f"• **{p['platform']}** → [Visit]({p['url']})")
    else:
        st.write("No data found")

    # =========================
    # 🎥 MEDIA
    # =========================
    st.subheader("🎥 Media Platforms")
    media = data.get("media_platforms", [])
    if media:
        for p in media:
            st.markdown(f"• **{p['platform']}** → [Watch]({p['url']})")
    else:
        st.write("No data found")

    # =========================
    # 🌍 OTHER WEBSITES
    # =========================
    st.subheader("🌍 Other Websites")
    other = data.get("other_websites", [])
    if other:
        for p in other:
            st.markdown(f"• **{p['platform']}** → [Visit]({p['url']})")
    else:
        st.write("No data found")

    # =========================
    # #️⃣ HASHTAGS
    # =========================
    st.subheader("#️⃣ Hashtags")
    hashtags = data.get("hashtags", [])
    if hashtags:
        st.write(", ".join(hashtags))
    else:
        st.write("No hashtags found")

    # =========================
    # 📊 METRICS
    # =========================
    st.subheader("📊 Metrics")

    metrics = data.get("metrics", {})

    col1, col2, col3 = st.columns(3)
    col1.metric("Search Accuracy", metrics.get("search_accuracy", "0%"))
    col2.metric("Identity Confidence", metrics.get("identity_confidence", 0))
    col3.metric("Profiles Linked", metrics.get("profiles_linked", 0))

    col4, col5 = st.columns(2)
    col4.metric("Fake Accounts", metrics.get("possible_fake_accounts", 0))
    col5.metric("Risk Level", metrics.get("risk_flag", "Unknown"))

    st.info(f"🧠 Behavior Pattern: {metrics.get('behavior_pattern', 'Unknown')}")

    # =========================
    # 🧾 SUMMARY
    # =========================
    st.subheader("🧾 Summary")
    st.success(data.get("summary", "No summary available"))