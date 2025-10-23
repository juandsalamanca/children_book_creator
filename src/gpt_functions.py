import openai

def write_story(story_type, audience, reader_info, main_character_info, rememberance, extra_details):
  #client = OpenAI()
  user_prompt = f"""
  I need you to write a storyof the type {story_type} for the audience {audience}
  """
  messages = [{"role":"system", "content":"You are an expert at searching for Movie an TV official information guiding yourself by official sources when available."},
            {"role": "user", "content":user_prompt}]

  response = openai.responses.create(
      model="gpt-4o-mini",
      input=messages
  )
  return response.output_text
