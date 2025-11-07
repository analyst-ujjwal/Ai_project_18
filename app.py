import streamlit as st
from story_generator import generate_story
from utils.helpers import save_story
import os

st.set_page_config(page_title="AI Storyteller", page_icon="🧙‍♂️", layout="wide")

st.title("🧙‍♂️ AI Storyteller — Powered by Groq + LLaMA")

st.sidebar.header("⚙️ Story Settings")
genre = st.sidebar.selectbox("Select Genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Adventure", "Horror"])
style = st.sidebar.selectbox("Writing Style", ["Narrative", "Dialogue", "Poetic", "Journal", "Screenplay"])
length = st.sidebar.slider("Story Length (words)", 100, 2000, 500)
temperature = st.sidebar.slider("Creativity (Temperature)", 0.3, 1.2, 0.8)

st.markdown("### ✨ Enter your story idea below:")
prompt = st.text_area("Story Idea", placeholder="Example: A lonely robot explores an abandoned city...")

if st.button("🪄 Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a story idea first.")
    else:
        with st.spinner("Summoning the storyteller... 🪄"):
            story = generate_story(prompt, genre, style, length, temperature)
            st.markdown("## 📖 Generated Story")
            st.write(story)
            save_story(story)
            st.success("Story saved successfully in `outputs/stories/`!")

st.markdown("---")
st.caption("Made with ❤️ using Groq + Streamlit")
