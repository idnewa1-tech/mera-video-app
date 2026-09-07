import urllib.parse
import streamlit as st

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Apne phone se video generate karein:")

prompt = st.text_area(
    "Prompt likhein:",
    placeholder="E.g., A colorful parrot flying over a green forest...",
)

if st.button("Generate Video"):
  if prompt:
    with st.spinner("AI video generate kar raha hai..."):
      encoded_prompt = urllib.parse.quote(prompt)
      # 100% Free, reliable video generation link
      video_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=video"

      st.success("Video ready hai!")
      st.video(video_url)
  else:
    st.warning("Pehle prompt to likhein!")
