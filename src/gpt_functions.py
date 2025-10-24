import streamlit as st
import openai
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def write_story(story_type, reader_info, main_character_info, story_info):
  #client = OpenAI()

  user_prompt = f"""
  I need you to write a storyof the type {story_type} for the audience {reader_info["type"]}
  """
  if reader_info["type"] == "Individual reader":
    user_prompt += f"of age {reader_info["age"]}, {reader_info["gender"]}"
  messages = [{"role":"system", "content":"You are an expert at searching for Movie an TV official information guiding yourself by official sources when available."},
            {"role": "user", "content":user_prompt}]

  response = openai.responses.create(
      model="gpt-4o-mini",
      input=messages
  )
  return response.output_text

def create_ilustration(input_text, audience):
  response = openai.response.create(
    model="gpt-4o"
    input=f"Create an image as an ilustration for the following text: {input_text}. It's for s children's book so style it appropriately.",
    tools=[{"type":"image_generation"}]
  mage_generation_calls = [
    output
    for output in response.output
    if output.type == "image_generation_call"
  ]

  image_data = [output.result for output in image_generation_calls]

  if image_data:
    image_base64 = image_data[0]

  return image_base64
