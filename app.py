import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Age in Seconds Calculator", page_icon="⏱️", layout="centered")

st.title("⏱️ Age into Seconds Calculator by Ameer Ali")
st.write("This app calculates your age in **seconds**, based on your date of birth.")

# --- User Input ---
dob = st.date_input("Enter your Date of Birth:", min_value=date(1900, 1, 1), max_value=date.today())

# --- Calculate Age ---
if st.button("Calculate Age in Seconds"):
    now = datetime.now()
    dob_datetime = datetime.combine(dob, datetime.min.time())

    if dob_datetime > now:
        st.error("🚫 Date of birth cannot be in the future!")
    else:
        delta = now - dob_datetime
        age_seconds = int(delta.total_seconds())

        # Conversions
        age_minutes = age_seconds // 60
        age_hours = age_seconds // 3600
        age_days = delta.days
        age_years = round(age_days / 365.25, 2)

        # Display results
        st.success(f"🎉 Your age: **{age_seconds:,} seconds**!")
        st.info(f"🕒 Minutes: **{age_minutes:,}**")
        st.info(f"⏰ Hours: **{age_hours:,}**")
        st.info(f"📅 Days: **{age_days:,}**")
        st.info(f"🎂 Years: **{age_years}**")

# --- Info Section ---
with st.expander("ℹ️ How it works"):
    st.markdown("""
    This app:
    1. Takes your **date of birth**
    2. Compares it with the **current date and time**
    3. Calculates your age in **seconds**
    4. Converts seconds into minutes, hours, days, and years
    
    Powered by Python’s built-in `datetime` module for accuracy.
    """)



