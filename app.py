import streamlit as st
from gradio_client import Client

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Prompt se asli MP4 video banayein:")

prompt = st.text_input("Prompt likhein:", placeholder="E.g., A red sports car speeding on a highway at night...")

if st.button("Generate Video"):
    if prompt:
        with st.spinner("AI video generate kar raha hai (isme 1-2 minute ka GPU time lag sakta hai)..."):
            try:
                # Active video model
                client = Client("multimodalart/cosmo-video-generator")
                video_path = client.predict(
                    prompt,
                    api_name="/generate_video"
                )
                
                st.success("Video ban gaya!")
                st.video(video_path)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle prompt likhein!")
        
