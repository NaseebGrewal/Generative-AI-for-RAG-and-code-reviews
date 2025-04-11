# """
# Author: Naseeb Grewal
# Description: openai_response.py for generative AI Chatbot.
# """

# import os

# import openai
# from dotenv import load_dotenv

# load_dotenv("../../.env")  # This loads the variables from .env into the environment


# def response_from_open_ai(messages: str) -> str:
#     """
#     Retrieve a response from the OpenAI model based on user input.

#     Args:
#         user_prompt (str): The user's input prompt.

#     Returns:
#         str: The response generated by the OpenAI model.
#     """

#     openai.api_key = os.environ["OPENAI_API_KEY"]
#     openai.api_type = os.environ["OPENAI_API_TYPE"]
#     openai.api_base = os.environ["OPENAI_API_BASE"]
#     openai.api_version = os.environ["OPENAI_API_VERSION"]

#     # models = ["gpt-35-turbo-16k","gpt-35-turbo","gpt-4-32k", "gpt-4"]
#     deployments = ["gpt-35-16k", "gpt-35-turbo-1106", "gpt-4-32k-prod", "gpt4-1106"]

#     engine = deployments[2]

#     # Generate a chat completion using OpenAI API
#     response = openai.ChatCompletion.create(
#         engine=engine, messages=messages, temperature=0, max_tokens=800
#     )

#     return response.choices[0].message["content"]


# def response_from_open_ai2(messages: str) -> str:
#     """
#     Retrieve a response from the OpenAI model based on user input.

#     Args:
#         user_prompt (str): The user's input prompt.

#     Returns:
#         str: The response generated by the OpenAI model.
#     """

#     openai.api_key = os.environ["OPENAI_API_KEY"]
#     openai.api_type = os.environ["OPENAI_API_TYPE"]
#     openai.api_base = os.environ["OPENAI_API_BASE"]
#     openai.api_version = os.environ["OPENAI_API_VERSION"]

#     # models = ["gpt-35-turbo-16k","gpt-35-turbo","gpt-4-32k", "gpt-4"]
#     deployments = ["gpt-35-16k", "gpt-35-turbo-1106", "gpt-4-32k-prod", "gpt4-1106"]

#     engine = deployments[-1]

#     # Generate a chat completion using OpenAI API
#     response = openai.ChatCompletion.create(
#         engine=engine, messages=messages, temperature=0, max_tokens=800
#     )

#     return response.choices[0].message["content"]


# def response_from_open_ai1(messages: str) -> str:
#     """
#     Retrieve a response from the OpenAI model based on user input.

#     Args:
#         user_prompt (str): The user's input prompt.

#     Returns:
#         str: The response generated by the OpenAI model.
#     """

#     openai.api_key = os.environ["OPENAI_API_KEY"]
#     openai.api_type = os.environ["OPENAI_API_TYPE"]
#     openai.api_base = os.environ["OPENAI_API_BASE"]
#     openai.api_version = os.environ["OPENAI_API_VERSION"]

#     # models = ["gpt-35-turbo-16k","gpt-35-turbo","gpt-4-32k", "gpt-4"]
#     deployments = ["gpt-35-16k", "gpt-35-turbo-1106", "gpt-4-32k-prod", "gpt4-1106"]

#     engine = deployments[1]

#     # Generate a chat completion using OpenAI API
#     response = openai.ChatCompletion.create(
#         engine=engine, messages=messages, temperature=0, max_tokens=800
#     )

#     return response.choices[0].message["content"]
