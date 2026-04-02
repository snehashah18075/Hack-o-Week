import streamlit as st
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# --- 1. NLTK SETUP ---

try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
@@ -14,14 +14,13 @@
except Exception as e:
    st.error(f"Error downloading NLTK data: {e}")

# --- 2. PAGE CONFIG ---
# We removed the CSS block here. Streamlit defaults to white/light mode.
st.set_page_config(page_title="Institute Enquiry Bot", page_icon="🎓")

st.title("🎓 Institute Enquiry Chatbot")
st.write("Ask me about fees, timings, courses, or contact info!")

# --- 3. DATA & PREPROCESSING ---

lemmatizer = WordNetLemmatizer()

qa_pairs = {
@@ -76,4 +75,4 @@

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.messages.append({"role": "assistant", "content": response})
