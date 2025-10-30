import streamlit as st
import openai
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def write_story(story_type, reader_info, main_character_info, story_info, highlights, narrative, main_characters_data, format):
  #client = OpenAI()

  user_prompt = f"""
  I need you to write a storyof the type {story_type} for the audience {reader_info["type"]}
  """
  if reader_info["type"] == "Individual reader":
    user_prompt += f"of age {reader_info["age"]}, {reader_info["gender"]}"
  main_character_info_string = "The main character has the following characteristics"
  for key, value in main_character_info.items():
    main_character_info_string += f"{key}: {value}, "
  story_info_string = "The story has the following characteristics"
  for key, value in story_info.items():
    story_info_string += f"{key}: {value}, "

  highlights_string = "The story should emphasize the following aspects"
  for key, value in highlights.items():
    highlights_string += f"{key}: {value}, "

  narrative_string = "The story should be narrated in the following way"
  for key, value in narrative.items():
    narrative_string += f"{key}: {value}, " 

  main_character_string = "The story includes the following main characters"
  for character in main_characters_data:
    for key, value in character.items():
      main_character_string += f"{key}: {value}, "  

  format_string = "The story should follow the following format"
  for key, value in format.items():
    format_string += f"{key}: {value}, "  

  user_prompt += f" {story_info_string}. "
  user_prompt += f" {main_character_info_string}. "
  user_prompt += f" {highlights_string}. "
  user_prompt += f" {narrative_string}. "
  user_prompt += f" {main_character_string}. "
  user_prompt += f" {format_string}. "
  messages = [{"role":"system", "content":"You are an expert at searching for Movie an TV official information guiding yourself by official sources when available."},
            {"role": "user", "content":user_prompt}]

  response = openai.responses.create(
      model="gpt-4o-mini",
      input=messages
  )
  return response.output_text

def create_ilustration(input_text, audience):
  response = openai.response.create(
    model="gpt-4o",
    input=f"Create an image as an ilustration for the following text: {input_text}. It's for s children's book so style it appropriately.",
    tools=[{"type":"image_generation"}]
  )
  image_generation_calls = [
    output
    for output in response.output
    if output.type == "image_generation_call"
  ]

  image_data = [output.result for output in image_generation_calls]

  if image_data:
    image_base64 = image_data[0]

  return image_base64
