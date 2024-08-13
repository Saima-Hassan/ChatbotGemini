import google.generativeai as genai
import streamlit as st
import os

# Get API key from environment variable for security reasons
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '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')

# Configure the Generative AI model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponse(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="Chatbot", layout="centered")

st.title("🤖 AI Chat Master 🤖")
st.write("Powered by Generative AI | Developed by Saima Hassan")

# Custom CSS for chat layout
st.markdown("""
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.user-msg {
    align-self: flex-end;
    background-color: #d4f4ff;
    border-radius: 10px;
    padding: 10px;
    max-width: 70%;
    word-wrap: break-word;
}
.bot-msg {
    align-self: flex-start;
    background-color: #f4f4f8;
    border-radius: 10px;
    padding: 10px;
    max-width: 70%;
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state["history"] = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your prompt:", "", max_chars=2000, label_visibility="visible")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = getResponse(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please enter a prompt.")

# Display chat history
if st.session_state.history:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for user_msg, bot_msg in st.session_state.history:
         # User message (right side)
        st.markdown(f"""
        <div style="
            background-color: #273443;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 5px 0;
            max-width: 95%;
            text-align: left;
            color: #ffffff;
            float: right;
            display: inline-block;
            ">
            <strong>👤 User:</strong>
            <p style="margin: 0; font-size: 16px; line-height: 24px;">{user_msg}</p>
        </div>
        <div style="clear: both;"></div>
        """, unsafe_allow_html=True)



        # Bot message (left side)
        st.markdown(f"""
        <div style="
            background-color: #075e54;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 5px 0;
            max-width: 95%;
            text-align: left;
            color: #ffffff;
            display: inline-block;
            ">
            <strong>🤖 Bot:</strong>
            <p style="margin: 0; font-size: 16px; line-height: 24px;">{bot_msg}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)