import streamlit as st
import pandas as pd
import json
import os
import time
from datetime import datetime
import plotly.express as px
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

BLOCKED_FILE = "data/blocked_ips.txt"

from auth import supabase
# =====================================================
# ACTIVITY LOGGER
# =====================================================

def log_user_activity(
    email,
    action,
    login_method="unknown"
):

    try:

        conn = psycopg2.connect(DATABASE_URL)

        cur = conn.cursor()

        cur.execute(
            """

            INSERT INTO user_activity_logs
            (
                email,
                action,
                login_method
            )

            VALUES (%s, %s, %s)

            """,
            (
                email,
                action,
                login_method
            )
        )

        conn.commit()

        cur.close()

        conn.close()

    except Exception as e:

        print(e)
# =====================================================
# CHECK AUTH SESSION
# =====================================================

if "logged_in" not in st.session_state:

    st.switch_page("login.py")

# =====================================================
# TRACK USER ACCESS
# =====================================================

user_email = "guest_user"

login_method = "guest"

try:

    user = supabase.auth.get_user()

    if user and user.user:

        user_email = user.user.email

        login_method = "google/email"

except:
    pass

log_user_activity(
    user_email,
    "Opened Dashboard",
    login_method
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SOC Enterprise Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0b0f19;
    color: white;
    font-family: Arial;
}

.main {
    background-color: #0b0f19;
}

.block-container {
    padding-top: 1rem;
}

h1, h2, h3 {
    color: #00ffcc;
}

div[data-testid="metric-container"] {
    background-color: #111827;
    border: 1px solid #1f2937;
    padding: 20px;
    border-radius: 15px;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

.stDataFrame {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🛡️ SOC Enterprise")

# =====================================================
# LOGOUT BUTTON
# =====================================================

if st.sidebar.button("Logout"):

    log_user_activity(
        user_email,
        "Logged Out",
        login_method
    )

    supabase.auth.sign_out()

    if "logged_in" in st.session_state:
        del st.session_state["logged_in"]

    st.switch_page("login.py")

refresh_rate = st.sidebar.slider(
    "Auto Refresh",
    5,
    60,
    10
)

st.sidebar.success("SOC STATUS: ACTIVE")

st.sidebar.markdown("""
## Infrastructure

- AWS EC2
- Docker
- ELK Stack
- PostgreSQL
- Python SOAR
- Streamlit SOC

---

## Detection Engines

- SSH Brute Force
- SQL Injection
- DDoS Detection
- Malware Detection
- Privilege Escalation
- Port Scan Detection
""")

# =====================================================
# FILES
# =====================================================

# =====================================================
# LOAD ALERTS FROM POSTGRESQL
# =====================================================

conn = psycopg2.connect(DATABASE_URL)

query = """
SELECT
    timestamp,
    ip,
    country,
    attack_type,
    severity,
    status,
    threat_score,
    mitre_tactic
FROM alerts
ORDER BY id DESC
LIMIT 500
"""

df = pd.read_sql(query, conn)

# =====================================================
# HANDLE EMPTY DATA SAFELY
# =====================================================

required_columns = [
    "timestamp",
    "ip",
    "country",
    "attack_type",
    "severity",
    "status",
    "threat_score",
    "mitre_tactic"
]

if df.empty:
    df = pd.DataFrame(columns=required_columns)

for col in required_columns:
    if col not in df.columns:
        df[col] = None

# =====================================================
# LOAD BLOCKED IPS
# =====================================================

blocked_ips = []

if os.path.exists(BLOCKED_FILE):

    with open(BLOCKED_FILE, "r") as f:

        blocked_ips = [
            line.strip()
            for line in f
            if line.strip()
        ]

# =====================================================
# HANDLE EMPTY DATA SAFELY
# =====================================================

required_columns = [
    "timestamp",
    "ip",
    "country",
    "attack_type",
    "severity",
    "status",
    "threat_score",
    "mitre_tactic"
]

if df.empty:
    df = pd.DataFrame(columns=required_columns)

for col in required_columns:
    if col not in df.columns:
        df[col] = None

# =====================================================
# HEADER
# =====================================================

st.title("🛡️ SOC + SIEM + SOAR Enterprise Dashboard")

st.markdown("""
Real-time cybersecurity monitoring and automated response platform deployed on AWS EC2.
""")

st.markdown("---")

# =====================================================
# METRICS
# =====================================================

total_alerts = len(df)
total_blocked = len(blocked_ips)

latest_attacker = "N/A"

if total_alerts > 0:
    latest_attacker = df.iloc[0]["ip"]

threat_level = "LOW"

if total_alerts >= 10:
    threat_level = "MEDIUM"

if total_alerts >= 20:
    threat_level = "HIGH"

if total_alerts >= 30:
    threat_level = "CRITICAL"

avg_threat_score = 0

if total_alerts > 0:
    avg_threat_score = round(
        pd.to_numeric(df["threat_score"]).mean(),
        2
    )

metric1, metric2, metric3, metric4, metric5 = st.columns(5)

with metric1:
    st.metric("🚨 Total Alerts", total_alerts)

with metric2:
    st.metric("🚫 Blocked IPs", total_blocked)

with metric3:
    st.metric("🎯 Latest Attacker", latest_attacker)

with metric4:
    st.metric("⚠️ Threat Level", threat_level)

with metric5:
    st.metric("🔥 Avg Threat Score", avg_threat_score)

st.markdown("---")

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🚨 Incidents",
    "🌍 Threat Intel",
    "☁️ Infrastructure"
])

# =====================================================
# TAB 1 - OVERVIEW
# =====================================================

with tab1:

    row1_col1, row1_col2 = st.columns(2)

    # =================================================
    # ATTACK TIMELINE
    # =================================================

    with row1_col1:

        st.subheader("📈 Attack Timeline")

        if total_alerts > 0:

            timeline_df = df.copy()

            timeline_df["event"] = 1

            fig_timeline = px.line(
                timeline_df,
                x=timeline_df.index,
                y="event",
                title="Attack Timeline"
            )

            fig_timeline.update_layout(
                paper_bgcolor="#0b0f19",
                plot_bgcolor="#0b0f19",
                font_color="white"
            )

            st.plotly_chart(
                fig_timeline,
                use_container_width=True
            )

    # =================================================
    # SEVERITY DONUT CHART
    # =================================================

    with row1_col2:

        st.subheader("🔥 Severity Distribution")

        severity_counts = (
            df["severity"]
            .value_counts()
            .reset_index()
        )

        severity_counts.columns = [
            "Severity",
            "Count"
        ]

        fig_severity = px.pie(
            severity_counts,
            values="Count",
            names="Severity",
            hole=0.45,
            title="Threat Severity Levels"
        )

        fig_severity.update_layout(
            paper_bgcolor="#0b0f19",
            plot_bgcolor="#0b0f19",
            font_color="white"
        )

        st.plotly_chart(
            fig_severity,
            use_container_width=True
        )

    st.markdown("---")

    row2_col1, row2_col2 = st.columns(2)

    # =================================================
    # ATTACK TYPES
    # =================================================

    with row2_col1:

        st.subheader("🧨 Attack Type Distribution")

        attack_counts = (
            df["attack_type"]
            .value_counts()
            .reset_index()
        )

        attack_counts.columns = [
            "Attack Type",
            "Count"
        ]

        fig_attack = px.bar(
            attack_counts,
            x="Attack Type",
            y="Count",
            title="Attack Categories"
        )

        fig_attack.update_layout(
            paper_bgcolor="#0b0f19",
            plot_bgcolor="#0b0f19",
            font_color="white"
        )

        st.plotly_chart(
            fig_attack,
            use_container_width=True
        )

    # =================================================
    # WORLD THREAT MAP
    # =================================================

    with row2_col2:

        st.subheader("🌍 Global Threat Map")

        country_coords = {
            "Russia": {"lat": 61.5240, "lon": 105.3188},
            "China": {"lat": 35.8617, "lon": 104.1954},
            "Iran": {"lat": 32.4279, "lon": 53.6880},
            "North Korea": {"lat": 40.3399, "lon": 127.5101},
            "Brazil": {"lat": -14.2350, "lon": -51.9253},
            "Germany": {"lat": 51.1657, "lon": 10.4515},
            "USA": {"lat": 37.0902, "lon": -95.7129}
        }

        country_counts = (
            df["country"]
            .value_counts()
            .reset_index()
        )

        country_counts.columns = [
            "country",
            "count"
        ]

        latitudes = []
        longitudes = []

        for country in country_counts["country"]:

            coords = country_coords.get(
                country,
                {"lat": 0, "lon": 0}
            )

            latitudes.append(coords["lat"])
            longitudes.append(coords["lon"])

        country_counts["lat"] = latitudes
        country_counts["lon"] = longitudes

        fig_map = px.scatter_geo(
            country_counts,
            lat="lat",
            lon="lon",
            size="count",
            hover_name="country",
            color="count",
            projection="natural earth",
            title="Global Cyber Threat Activity"
        )

        fig_map.update_layout(
            paper_bgcolor="#0b0f19",
            font_color="white",
            geo=dict(
                bgcolor="#0b0f19",
                showland=True,
                landcolor="#1f2937",
                showcountries=True
            )
        )

        st.plotly_chart(
            fig_map,
            use_container_width=True
        )

    st.markdown("---")

    # =================================================
    # LIVE SOC FEED
    # =================================================

    st.subheader("🛰️ Live SOC Feed")

    latest_alerts = df.head(10)

    for _, row in latest_alerts.iterrows():

        severity = row["severity"]
        attack = row["attack_type"]
        ip = row["ip"]
        country = row["country"]
        timestamp = row["timestamp"]

        if severity == "CRITICAL":

            st.error(
                f"🚨 {severity} | {attack} detected from {ip} ({country}) at {timestamp}"
            )

        elif severity == "HIGH":

            st.warning(
                f"⚠️ {severity} | {attack} detected from {ip} ({country}) at {timestamp}"
            )

        else:

            st.info(
                f"ℹ️ {severity} | {attack} detected from {ip} ({country}) at {timestamp}"
            )

# =====================================================
# TAB 2 - INCIDENTS
# =====================================================

with tab2:

    st.subheader("🚨 Incident Alert Table")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🚫 Blocked IP Addresses")

    blocked_df = pd.DataFrame(
        blocked_ips,
        columns=["Blocked IP"]
    )

    st.dataframe(
        blocked_df,
        use_container_width=True
    )

# =====================================================
# TAB 3 - THREAT INTEL
# =====================================================

with tab3:

    intel1, intel2, intel3 = st.columns(3)

    with intel1:
        st.error("""
### Top Threat
Credential Access
""")

    with intel2:
        st.warning("""
### Most Targeted Service
Linux SSH
""")

    with intel3:
        st.success("""
### SOAR Response
Automatic IP Blocking
""")

    st.markdown("---")

    st.subheader("🎯 MITRE ATT&CK Tactics")

    mitre_counts = (
        df["mitre_tactic"]
        .value_counts()
        .reset_index()
    )

    mitre_counts.columns = [
        "MITRE Tactic",
        "Count"
    ]

    fig_mitre = px.bar(
        mitre_counts,
        x="MITRE Tactic",
        y="Count",
        title="MITRE ATT&CK Analytics"
    )

    fig_mitre.update_layout(
        paper_bgcolor="#0b0f19",
        plot_bgcolor="#0b0f19",
        font_color="white"
    )

    st.plotly_chart(
        fig_mitre,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🔥 Critical Incidents")

    critical_df = df[
        df["severity"] == "CRITICAL"
    ]

    st.dataframe(
        critical_df,
        use_container_width=True
    )

# =====================================================
# TAB 4 - INFRASTRUCTURE
# =====================================================

with tab4:

    st.subheader("☁️ Cloud Infrastructure")

    infra1, infra2, infra3 = st.columns(3)

    with infra1:
        st.success("AWS EC2: RUNNING")

    with infra2:
        st.success("Docker Containers: ACTIVE")

    with infra3:
        st.success("Dashboard: ONLINE")

    st.markdown("---")

    st.subheader("🏗️ SOC + SIEM + SOAR Pipeline")

    st.code("""
Attacker
   ↓
Live Attack Generator
   ↓
EC2 Telemetry Pipeline
   ↓
PostgreSQL Database
   ↓
SIEM Analysis
   ↓
SOAR Automation
   ↓
Streamlit Dashboard
""")

    st.markdown("---")

    st.subheader("🚀 Deployment Information")

    st.code("""
Cloud Provider : AWS EC2
Frontend       : Streamlit
Backend        : Python
Database       : PostgreSQL
Containers     : Docker
Security Stack : ELK Stack
OS             : Ubuntu Linux
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

current_time = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

st.caption(f"""
SOC + SIEM + SOAR Enterprise Dashboard

Last Updated: {current_time}
""")

# =====================================================
# AUTO REFRESH
# =====================================================

time.sleep(refresh_rate)
st.rerun()
