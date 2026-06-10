import streamlit as st
import requests

st.title("🤖 Smart Customer Support AI")

# Store chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask something...")

if st.button("Send"):
    if query.strip() != "":
        res = requests.get("http://127.0.0.1:8000/chat", params={"query": query})
        data = res.json()

        # Save chat
        st.session_state.chat.append(("You", query))
        st.session_state.chat.append(("Bot", data["response"]))

        # NEW: show decision + confidence
        st.session_state.chat.append((
            "Meta",
            f"Decision: {data.get('decision')} | Confidence: {round(data.get('confidence', 0), 2)}"
        ))

# Display chat
for sender, msg in st.session_state.chat:
    if sender == "Meta":
        st.info(msg)
    else:
        st.write(f"**{sender}:** {msg}")