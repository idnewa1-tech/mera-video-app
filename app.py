import streamlit as st
from gradio_client import Client

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Prompt se asli chalne wali MP4 video banayein:")

prompt = st.text_input("Prompt likhein:", placeholder="E.g., A red sports car speeding on a neon highway...")

TOKEN = "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"

if st.button("Generate Video"):
    if prompt:
        with st.spinner("AI Video ban raha hai... 1 se 2 minute intezar karein..."):
            try:
                client = Client("ByteDance/AnimateDiff-Lightning", headers={"Authorization": f"Bearer {TOKEN}"})
                
                # fn_index=0 use karne se api_name ka koi error nahi aayega
                result = client.predict(
                    prompt,
                    "4-Step",
                    fn_index=0
                )
                
                st.success("Asli Video ready hai!")
                st.video(result)
                
            except Exception as e:
                st.error(f"Error aaya: {e}")
    else:
        st.warning("Pehle prompt likhein!")
