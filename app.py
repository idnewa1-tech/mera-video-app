from gradio_client import Client
import streamlit as st

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Apne phone se video generate karein:")

prompt = st.text_area(
    "Prompt likhein:",
    placeholder="E.g., A cute robot dancing on the moon, cinematic 4k...",
)

if st.button("Generate Video"):
  if prompt:
    with st.spinner(
        "Video ban raha hai... isme 1 se 2 minute lag sakte hain..."
    ):
      try:
        # Working Free Video AI space
        client = Client("KingNish/ZeroGPU-Wan2.1-1.3B")
        result = client.predict(
            prompt=prompt,
            api_name="/generate_video",
        )
        st.success("Video ready hai!")
        st.video(result)
      except Exception as e:
        st.error(f"Error aaya: {e}")
  else:
    st.warning("Pehle prompt to likhein!")
