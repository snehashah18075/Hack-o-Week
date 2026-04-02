import streamlit as st
import string
import nltk
import re
import pandas as pd
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

st.set_page_config(page_title="Institute Enquiry Bot", page_icon="🎓", layout="wide")

# --- NLTK SETUP ---

@st.cache_resource
def download_nltk_data():
    nltk.download('punkt', quiet=True)
@@ -21,7 +21,7 @@
download_nltk_data()
lemmatizer = WordNetLemmatizer()

# --- BASE KNOWLEDGE ---

qa_pairs = {
    "hello": "Hello! Welcome to the Institute Enquiry Bot.",
    "hi": "Hello! Welcome to the Institute Enquiry Bot.",
@@ -33,7 +33,7 @@
    "bye": "Goodbye!"
}

# --- TASK 9: MULTICHANNEL MOCKUP ---

st.sidebar.title("📱 Channel Mockup (Task 9)")
channel = st.sidebar.selectbox("Simulate platform:", ["Web App", "WhatsApp", "SMS"])

@@ -44,14 +44,14 @@
        return f"Reply: {text[:100]}..."
    return text

# --- TASK 6: ENTITY EXTRACTION ---

def extract_entities(text):
    sem_match = re.search(r"(?i)(?:sem|semester)\s*(\d+)", text)
    course_match = re.search(r"(?i)\b(cs|me|ee|it|mba|b\.tech|m\.tech)\b", text)
    return (sem_match.group(1) if sem_match else None,
            course_match.group(1).upper() if course_match else None)

# --- CORE LOGIC (TASK 7 & 8) ---

def get_response(raw_input):
    user_text = raw_input.lower()
    sem, course = extract_entities(user_text)
@@ -111,7 +111,7 @@
    fallback_msg = "I didn't quite catch that. Did you mean to ask about Fees, Timings, Courses, or Exams?"
    return fallback_msg, "Fallback/Unknown", entity_log

# --- UI SETUP & STATE ---

if "messages" not in st.session_state:
    st.session_state.messages = []
if "context" not in st.session_state:
@@ -121,7 +121,7 @@

st.title("🎓 Smart Institute Bot")

# --- MAIN CHAT INTERFACE ---

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
@@ -149,7 +149,7 @@
        "Entities": entities
    })

# --- TASK 10: ANALYTICS DASHBOARD ---

st.sidebar.markdown("---")
st.sidebar.title("📊 Analytics (Task 10)")
if st.session_state.analytics_log:
@@ -158,4 +158,4 @@
    failed = len(df[df["Intent"] == "Fallback/Unknown"])
    st.sidebar.caption(f"Unanswered Queries: {failed}")
else:
    st.sidebar.info("Chat with the bot to see logs here.")
    st.sidebar.info("Chat with the bot to see logs here.")
