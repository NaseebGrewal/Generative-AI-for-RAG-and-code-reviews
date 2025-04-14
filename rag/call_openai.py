from openai import OpenAI
from dotenv import load_dotenv
import os


current_dir = os.path.dirname(__file__)
env_path = os.path.join(current_dir, "..", ".env")

load_dotenv(dotenv_path=env_path)

def get_gpt_answer(prompt):
    API_KEY = os.getenv("OPENAI_API_KEY")            
    client = OpenAI(api_key=API_KEY)
    prompt = [{"role": "system", "content": """Your answer to all question is No."""},{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
            model="gpt-4o-mini-search-preview",
            messages=prompt
    )
    
    text = response.choices[0].message.content
    return text


get_gpt_answer("hi how are you")