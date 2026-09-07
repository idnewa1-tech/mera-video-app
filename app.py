import streamlit as st
from gradio_client import Client

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Prompt se asli chalne wali MP4 video banayein:")

prompt = st.text_input("Prompt likhein:", placeholder="A red sports car speeding on a neon highway...")

TOKEN = "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"

if st.button("Generate Video"):
    if prompt:
        with st.spinner("AI Video ban raha hai... isme 1 se 2 minute intezar karein..."):
            try:
                # Active public text-to-video client
                client = Client("diffusers/animatelcm-t2v", hf_token=TOKEN)
                
                # Single prompt call
                result = client.predict(
                    prompt=prompt,
                    api_name="/generate"
                )
                
                st.success("Asli Video ready hai!")
                st.video(result)
            except Exception as e:
                st.error(f"Error aaya: {e}")
    else:
        st.warning("Pehle prompt likhein!")
