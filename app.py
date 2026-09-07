import os
import streamlit as st
from gradio_client import Client

st.set_page_config(
    page_title="Mera AI Video Generator", page_icon="🎬", layout="centered"
)

st.title("🎬 Mera AI Video Generator")
st.write("Prompt likhein aur asli AI MP4 Video banayein:")

prompt = st.text_input(
    "Prompt likhein:",
    value="A red car speeding on a highway at night, cinematic",
)

HF_TOKEN = "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"

if st.button("Generate Video", type="primary"):
  if not prompt.strip():
    st.warning("Pehle prompt likhein!")
  else:
    with st.spinner(
        "AI Video render ho raha hai... (ZeroGPU queue me 1 se 2 minute lagte"
        " hain)..."
    ):
      try:
        # Verified Space Client
        client = Client("KingNish/Instant-Video", hf_token=HF_TOKEN)

        # Exact 4 backend parameters required by this Space
        result = client.predict(
            prompt.strip(),  # 1. Prompt text
            "ToonYou",  # 2. Base model
            "Zoom in",  # 3. Motion effect
            "4-Step",  # 4. Step quality
            api_name="/instant_video",  # Exact registered API endpoint
        )

        # Output validation
        if result and os.path.exists(str(result)):
          st.success("Video ready ho gaya!")
          st.video(str(result))
        else:
          st.error("Server se video file prapt nahi hui.")

      except Exception as e:
        st.error(f"Error detail: {e}")
          
