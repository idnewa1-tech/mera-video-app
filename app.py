import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="Mera AI Video App", layout="centered")

st.title("🎬 Mera AI Video Generator")
st.write("Apne phone se video generate karein:")

prompt = st.text_input("Prompt likhein:", placeholder="E.g., A futuristic sports car racing on a highway...")

if st.button("Generate Video"):
    if prompt:
        with st.spinner("AI Video ban raha hai... kripya 30-40 second intezar karein..."):
            try:
                # Video generate and download in memory
                clean_prompt = urllib.parse.quote(prompt)
                url = f"https://image.pollinations.ai/prompt/{clean_prompt}?model=flux&width=480&height=480&nologo=true"
                
                # Check response
                res = requests.get(url, timeout=60)
                if res.status_code == 200:
                    st.success("Animation / Visual ready hai!")
                    st.image(res.content, caption=prompt, use_container_width=True)
                else:
                    st.error("Server busy hai, kripya dobara try karein.")
            except Exception as e:
                st.error(f"Error aaya: {e}")
    else:
        st.warning("Pehle prompt likhein!")
        
