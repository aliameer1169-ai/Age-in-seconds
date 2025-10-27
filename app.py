import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Age in Seconds Calculator", page_icon="⏱️", layout="centered")

st.title("⏱️ Age into Seconds Calculator by Ameer Ali")

st.write("This app calculates your age in **seconds**, based on your date of birth.")

# --- User Input ---
dob = st.date_input("Enter your Date of Birth:", min_value=date(1900, 1, 1), max_value=date.today())

# --- Calculate age ---
if st.button("Calculate Age in Seconds"):
    now = datetime.now()
    dob_datetime = datetime.combine(dob, datetime.min.time())
    age_seconds = (now - dob_datetime).total_seconds()
    
    st.success(f"🎉 Your age is approximately **{int(age_seconds):,} seconds**!")
    st.caption(f"That’s roughly {round(age_seconds / (60*60*24*365.25), 2)} years.")

# --- Info Section ---
with st.expander("ℹ️ How it works"):
    st.markdown("""
    This app:
    1. Takes your **date of birth**.
    2. Compares it with the **current date and time**.
    3. Calculates the **difference in seconds**.

    Uses Python’s built-in `datetime` module for accurate calculations.
    """)

st.caption("Made with ❤️ using Streamlit")
