import streamlit as st
from engine.zerodha import get_login_url, generate_token, get_ltp
from engine.strategy import iron_condor
from engine.pnl import max_profit, max_loss

st.set_page_config(page_title="Zerodha Algo App", layout="wide")

st.title("🚀 Zerodha Algo Trading Dashboard")

# ---------------- LOGIN ----------------
st.subheader("1. Login to Zerodha")

if st.button("🔐 Login to Zerodha"):
    login_url = get_login_url()
    st.markdown(f'''
        <a href="{login_url}" target="_blank">
        👉 Click here to Login to Zerodha
        </a>
    ''', unsafe_allow_html=True)

st.markdown("After login, paste your **request_token** below:")

request_token = st.text_input("Request Token")

if st.button("✅ Generate Access Token"):
    if request_token:
        kite = generate_token(request_token)

        # Save kite object in session
        st.session_state["kite"] = kite

        st.success("✅ Access Token Generated & Session Created")
    else:
        st.error("Please Paste Request Token First")

# ---------------- IF LOGGED IN ----------------
if "kite" in st.session_state:

    st.success("🟢 Connected to Zerodha")

    st.subheader("2. Get Live Price (LTP)")

    col1, col2 = st.columns(2)

    with col1:
        symbol = st.text_input("Enter Symbol (Ex: NIFTY, TATASTEEL, RELIANCE)")

    with col2:
        exchange = st.selectbox("Select Exchange", ["NSE"])

    if st.button("📈 Get LTP"):
        try:
            ltp = get_ltp(st.session_state["kite"], symbol, exchange)
            st.metric(label=f"{symbol} LTP", value=ltp)
        except Exception as e:
            st.error(str(e))

    # ---------------- STRATEGY SECTION ----------------
    st.subheader("3. Strategy Module (Upcoming)")
    st.info("Iron Condor + Multi-leg strategies coming soon 🚧")

    if st.button("🚪 Logout / Clear Session"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.success("Session Cleared")
        st.experimental_rerun()

else:
    st.warning("Please Login to Zerodha First")
