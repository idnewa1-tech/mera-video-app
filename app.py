from gradio_client import Client
import streamlit as st

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Apne phone se video generate karein:")

prompt = st.text_area(
    "Prompt likhein:",
    placeholder="E.g., A colorful parrot flying over a green forest, cinematic 4k...",
)

if st.button("Generate Video"):
  if prompt:
    with st.spinner(
        "AI Video ban raha hai... isme 1 se 2 minute lag sakte hain..."
    ):
      try:
        # Aapka verified token auto-added hai
        HF_TOKEN = "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"

        client = Client(
            "damo-vilab/modelscope-damo-text-to-video-synthesis",
            hf_token=HF_TOKEN,
        )
        result = client.predict(
            prompt,
            api_name="/predict",
        )
        st.success("Video ready hai!")
        st.video(result)
      except Exception as e:
        st.error(f"Error aaya: {e}")
  else:
    st.warning("Pehle prompt to likhein!")
      
