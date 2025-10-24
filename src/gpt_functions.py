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
