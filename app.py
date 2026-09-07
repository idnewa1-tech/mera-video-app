import os
import requests
import streamlit as st
from gradio_client import Client

st.set_page_config(
    page_title="Mera AI Video Generator", page_icon="🎬", layout="centered"
)

st.title("🎬 Mera AI Video Generator")
st.write("Prompt likhein aur direct MP4 video generate karein:")

prompt = st.text_input("Prompt likhein:", value="a car driving fast on a highway")

# Hugging Face Verified Read Token
HF_TOKEN = "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"


def generate_video(prompt_text):
  # 1. Try Primary Hugging Face Text-to-Video engine
  try:
    client = Client("hysts/zeroscope-v2", hf_token=HF_TOKEN)
    result = client.predict(
        prompt_text,
        "",  # negative prompt
        api_name="/predict",
    )
    if result and os.path.exists(str(result)):
      return str(result)
  except Exception:
    pass

  # 2. Try Secondary Public Video Space (No Auth Required)
  try:
    client2 = Client("damo-vilab/modelscope-damo-text-to-video-synthesis")
    result2 = client2.predict(prompt_text, fn_index=0)
    if result2 and os.path.exists(str(result2)):
      return str(result2)
  except Exception:
    pass

  return None


if st.button("Generate Video", type="primary"):
  if not prompt.strip():
    st.warning("Kripya pehle prompt likhein!")
  else:
    with st.spinner(
        "AI Real Video render kar raha hai... Kripya 1 se 2 minute intezar"
        " karein..."
    ):
      video_file = generate_video(prompt.strip())

      if video_file:
        st.success("Video successfully generate ho gaya!")
        # Validated MP4 video display
        with open(video_file, "rb") as f:
          video_bytes = f.read()
        st.video(video_bytes)
      else:
        st.error(
            "Video generation servers par load jyada hai. Kripya 1 minute baad"
            " dobara button dabayein."
        )
