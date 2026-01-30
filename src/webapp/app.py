import os
import sys
import streamlit as st

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))      
SRC_DIR = os.path.dirname(CURRENT_DIR)                        

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from webapp.constants import UPDATE_FREQ_SEC
from webapp.crypto_api import get_crypto_data
from webapp.utils import format_number_with_suffix

st.set_page_config(page_title="Crypto Price", layout="centered")
@st.fragment(run_every=UPDATE_FREQ_SEC)
def display_crypto_price():
    try:
        data = get_crypto_data()

        price = data.get("price", 0)
        change_24h = data.get("percent_change_24h", 0)
        symbol = data.get("symbol", "")

        st.metric(
            label=symbol,
            value=format_number_with_suffix(price),
            delta=f"{change_24h:.2f}%",
            border=True,
        )

    except Exception as e:
        st.error(f"Failed to load data: {e}")


if __name__ == "__main__":
    display_crypto_price()
