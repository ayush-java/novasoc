import streamlit as st
import pandas as pd
import psycopg2
import os

from dotenv import load_dotenv
from auth import supabase
# =====================================================
# LOAD ENV
# =====================================================

load_dotenv()

# =====================================================
# ADMIN AUTH CHECK
# =====================================================

ADMIN_EMAIL = "adv220002@utdallas.edu"

try:

    user = supabase.auth.get_user()

    if not user or not user.user:

        st.error("Access Denied")

        st.stop()

    current_email = user.user.email

    if current_email != ADMIN_EMAIL:

        st.error("Access Denied")

        st.stop()

except:

    st.error("Access Denied")

    st.stop()

DATABASE_URL = os.getenv("DATABASE_URL")

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="NovaSOC Admin Activity",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("🛡️ NovaSOC Admin Activity Dashboard")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================

conn = psycopg2.connect(DATABASE_URL)

query = """

SELECT
    email,
    action,
    login_method,
    timestamp

FROM user_activity_logs

ORDER BY timestamp DESC

"""

df = pd.read_sql(query, conn)

conn.close()

# =====================================================
# METRICS
# =====================================================

total_events = len(df)

guest_events = len(
    df[df["login_method"] == "guest"]
)

real_users = len(
    df[df["login_method"] == "google/email"]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Events",
    total_events
)

col2.metric(
    "Guest Sessions",
    guest_events
)

col3.metric(
    "Authenticated Users",
    real_users
)

st.markdown("---")

# =====================================================
# ACTIVITY TABLE
# =====================================================

st.subheader("📋 User Activity Logs")

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# ACTIVITY CHART
# =====================================================

st.markdown("---")

st.subheader("📈 Login Method Distribution")

chart_data = (
    df["login_method"]
    .value_counts()
)

st.bar_chart(chart_data)

# =====================================================
# LATEST ACTIVITY
# =====================================================

st.markdown("---")

st.subheader("⚡ Latest Activity")

latest = df.head(10)

for _, row in latest.iterrows():

    st.info(
        f"""
        User: {row['email']}

        Action: {row['action']}

        Method: {row['login_method']}

        Time: {row['timestamp']}
        """
    )
