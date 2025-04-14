

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from a .env file located in the parent directory
env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    raise FileNotFoundError(f".env file not found at {env_path}")

def get_gpt_answer(prompt):
    """
    Fetches a response from the OpenAI GPT model based on the provided prompt.

    Args:
        prompt (str): The user input or question to send to the GPT model.

    Returns:
        str: The response generated by the GPT model.
    """
    from openai import OpenAI
    # Retrieve the OpenAI API key from environment variables
    API_KEY = os.getenv("OPENAI_API_KEY")
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=API_KEY)

    # Define the conversation context and user input
    messages = [
        {"role": "system", "content": "Your answer to all questions is No."},
        {"role": "user", "content": prompt}
    ]

    try:
        # Call the OpenAI API to generate a response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
    )
        # Extract and return the response text
        text = response.choices[0].message.content.strip()
        return text

    except Exception as e:
        # Handle potential errors gracefully
        raise RuntimeError(f"Failed to get a response from OpenAI: {e}")

# Example usage
if __name__ == "__main__":
    try:
        user_prompt = "hi how are you"
        answer = get_gpt_answer(user_prompt)
        print(f"GPT Response: {answer}")
    except Exception as e:
        print(f"Error: {e}")