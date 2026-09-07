from gradio_client import Client
import streamlit as st

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Apne phone se video generate karein:")

prompt = st.text_area(
    "Prompt likhein:",
    placeholder="E.g., A majestic lion walking on a neon city street...",
)

if st.button("Generate Video"):
  if prompt:
    with st.spinner(
        "Video ban raha hai... isme 1 se 2 minute lag sakte hain..."
    ):
      try:
        # Publicly accessible Free Video AI space
        client = Client("fffiloni/zeroscope")
        result = client.predict(
            prompt,  # User Prompt
            api_name="/zrscp",
        )
        st.success("Video ready hai!")
        st.video(result)
      except Exception as e:
        st.error(f"Error aaya: {e}")
  else:
    st.warning("Pehle prompt to likhein!")
      
