import base64
import time
import requests
import streamlit as st

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Apne phone se video generate karein:")

prompt = st.text_area(
    "Prompt likhein:",
    placeholder="E.g., A colorful parrot flying over a green forest...",
)

HF_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/damo-vilab/modelscope-damo-text-to-video-synthesis"

if st.button("Generate Video"):
  if prompt:
    with st.spinner("AI video process kar raha hai... thoda intezar karein..."):
      headers = {"Authorization": f"Bearer {HF_TOKEN}"}
      response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

      if response.status_code == 200:
        st.success("Video ready hai!")
        st.video(response.content)
      elif (
          response.status_code == 503
      ):  # Jab model load ho raha hota hai HuggingFace par
        estimated_time = response.json().get("estimated_time", 60)
        st.info(
            f"Model cloud par load ho raha hai ({int(estimated_time)}s)."
            " Kripya 1 minute baad dobara button dabayein."
        )
      else:
        st.error(f"Error ({response.status_code}): {response.text}")
  else:
    st.warning("Pehle prompt to likhein!")
      
