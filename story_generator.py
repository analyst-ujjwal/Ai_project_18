from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.8
)

def generate_story(idea, genre, style, length, temperature):
    prompt_template = PromptTemplate.from_file("prompts/story_prompt.txt")
    formatted_prompt = prompt_template.format(
        idea=idea, genre=genre, style=style, length=length
    )
    response = llm.invoke(formatted_prompt)
    return response.content.strip()
