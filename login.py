import streamlit as st
from auth import supabase
import random

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="NovaSOC Login",
    page_icon="🛡️",
    layout="centered"
)

# =====================================================
# HANDLE GOOGLE CALLBACK
# =====================================================

if "code" in st.query_params:

    st.session_state.logged_in = True

    st.switch_page("pages/dashboard.py")

# =====================================================
# CHECK ACTIVE SESSION
# =====================================================

if "logged_in" in st.session_state:

    if st.session_state.logged_in:

        st.switch_page("pages/dashboard.py")

# =====================================================
# GOOGLE AUTH URL
# =====================================================

google_auth_url = supabase.auth.sign_in_with_oauth(
    {
        "provider": "google",
        "options": {
            "redirect_to": "http://23.20.45.8:8501"
        }
    }
).url

# =====================================================
# CAPTCHA GENERATION
# =====================================================

if "captcha_a" not in st.session_state:

    st.session_state.captcha_a = random.randint(1, 9)
    st.session_state.captcha_b = random.randint(1, 9)

captcha_answer = (
    st.session_state.captcha_a +
    st.session_state.captcha_b
)

# =====================================================
# STYLING
# =====================================================

st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #071120 0%, #020617 70%);
    color: white;
}

header {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    max-width: 540px;
}

.title {
    text-align: center;
    color: #00ffd5;
    font-size: 5rem;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 1.2rem;
    margin-bottom: 3rem;
}

.section-title {
    text-align: center;
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 2rem;
}

.stTextInput > div > div {
    background-color: #0f172a !important;
    border: 1px solid #1f2937 !important;
    border-radius: 14px !important;
    height: 58px !important;
}

.stTextInput input {
    background-color: transparent !important;
    color: white !important;
    border: none !important;
}

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid #00ffd5;
    background: transparent;
    color: #00ffd5;
    padding: 0.9rem;
    font-weight: 700;
}

.stButton > button:hover {
    background-color: rgba(0,255,213,0.08);
}

.social-btn {
    width: 100%;
    padding: 16px;
    margin-top: 14px;
    border-radius: 14px;
    border: 1px solid #374151;
    background-color: rgba(15,23,42,0.85);
    color: white;
    font-size: 1rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    text-decoration: none;
}

.social-btn:hover {
    border-color: #00ffd5;
}

.social-logo {
    width: 28px;
    height: 28px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# UI
# =====================================================

st.markdown(
    "<div class='title'>NovaSOC</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Enterprise SOC + SIEM + SOAR Platform</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='section-title'>🔐 Secure Login</div>",
    unsafe_allow_html=True
)

email = st.text_input(
    "Email",
    placeholder="Enter your email"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)

# =====================================================
# EMAIL LOGIN
# =====================================================

if st.button("Login"):

    try:

        auth_response = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )

        if auth_response.user:

            st.session_state.logged_in = True

            st.switch_page("pages/dashboard.py")

    except Exception:

        st.error("Invalid email or password")

# =====================================================
# DIVIDER
# =====================================================

st.markdown("""
<div style='text-align:center; margin-top:25px; margin-bottom:20px; color:gray;'>
────────── OR ──────────
</div>
""", unsafe_allow_html=True)

# =====================================================
# GOOGLE LOGIN
# =====================================================

st.markdown(f"""
<a href="{google_auth_url}" target="_self" class="social-btn">
<img class="social-logo"
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg">
Continue with Google
</a>
""", unsafe_allow_html=True)

# =====================================================
# GUEST ACCESS
# =====================================================

st.markdown("""
<div style='text-align:center; margin-top:25px; margin-bottom:15px; color:gray;'>
────────── GUEST ACCESS ──────────
</div>
""", unsafe_allow_html=True)

st.info(
    f"Solve CAPTCHA: "
    f"{st.session_state.captcha_a} + "
    f"{st.session_state.captcha_b}"
)

guest_captcha = st.text_input(
    "Enter CAPTCHA Answer",
    placeholder="Solve the math problem",
    key="guest_captcha"
)

continue_guest = st.button(
    "Continue as Guest",
    use_container_width=True
)

if continue_guest:

    try:

        entered_answer = int(
            st.session_state.guest_captcha
        )

        if entered_answer == captcha_answer:

            st.session_state.logged_in = True

            st.session_state.guest_user = True

            st.switch_page("pages/dashboard.py")

        else:

            st.error("Incorrect CAPTCHA")

    except:

        st.error("Please enter a valid number")

# =====================================================
# CREATE ACCOUNT
# =====================================================

if st.button("Create Account"):

    if email == "" or password == "":

        st.error("Please enter email and password")

    else:

        try:

            response = supabase.auth.sign_up(
                {
                    "email": email,
                    "password": password
                }
            )

            st.success("Account created successfully!")

        except Exception as e:

            st.error(f"Unable to create account: {e}")

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div style='text-align:center; margin-top:40px; color:#6b7280;'>
Cloud-Native Cybersecurity Monitoring Platform
</div>
""", unsafe_allow_html=True)
