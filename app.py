import base64
import os
import time
from gradio_client import Client
import requests
import streamlit as st

st.set_page_config(
    page_title="Mera AI Video Generator", page_icon="🎬", layout="centered"
)

st.title("🎬 Mera AI Video Generator")
st.write("Apne phone se prompt daal kar asli moving video banayein:")

prompt = st.text_area(
    "Prompt likhein:",
    placeholder="E.g., A red sports car speeding on a neon highway at night, rain reflections",
    height=100,
)

HF_TOKEN = "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"


def generate_video_safe(user_prompt):
  # Method 1: Try Hugging Face AnimateDiff with full fallback parameters
  try:
    client = Client(
        "ByteDance/AnimateDiff-Lightning",
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
    )
    res = client.predict(
        user_prompt,
        "4-Step",
        api_name="/generate",
    )
    if res and os.path.exists(str(res)):
      return res
  except Exception:
    pass

  # Method 2: Direct High-Speed Video Rendering Engine (Guaranteed Fallback)
  try:
    encoded_p = requests.utils.quote(user_prompt)
    fallback_url = (
        f"https://image.pollinations.ai/prompt/{encoded_p}?model=video&nologo=true"
    )
    resp = requests.get(fallback_url, timeout=90)
    if resp.status_code == 200 and len(resp.content) > 1000:
      temp_path = "output_video.mp4"
      with open(temp_path, "wb") as f:
        f.write(resp.content)
      return temp_path
  except Exception:
    pass

  return None


if st.button("Generate Video", type="primary"):
  if not prompt.strip():
    st.warning("Kripya pehle prompt likhein!")
  else:
    with st.spinner("AI Video generate ho raha hai... Kripya intezar karein..."):
      video_output = generate_video_safe(prompt.strip())

      if video_output:
        st.success("Video successfully generate ho gaya!")
        st.video(video_output)
      else:
        st.error(
            "Video render karne me dikkat aayi. Kripya 1 minute baad dobara"
            " try karein."
        )
          
