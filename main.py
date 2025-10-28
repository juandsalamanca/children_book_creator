import streamlit as st
import openai
from src.gpt_functions import write_story

st.header('Children book generator')

if "story" not in st.session_state:
  st.session_state.story = None

category_list = ['Faith & Spirituality', 'Lessons & Values', 'Traditions & Celebrations', 'Love, Legacy & Legends']
category_desc_map = {"Faith & Spirituality": "Moments that connect us to God, hope or quiet wonder.",
                     "Lessons & Values": "Stories that shape beliefs, courage or character.",
                     "Traditions & Celebrations": "Stories tie to holidays, rituals, or family customs",
                     "Love, Legacy & Legends": "Stories that show who we are, how we love, and what we carry forward."}

category = st.selectbox('Category', category_list)
desc = category_desc_map[category]
st.write(desc)


st.subheader("Reader information")
reader_type_list = ['Individual reader', 'The whole family', 'General audience', 'Other']
reader_type = st.selectbox('Reader Type', reader_type_list)
if reader_type == 'Individual reader':
  age = st.text_input('Age')
  gender = st.text_input('Gender')
  relationship = st.text_input('Relationship to main character')
else:
  age = ""
  gender = ""
  reslationship = ""
  
if reader_type == 'Other':
  other_reader_type = st.text_input('Specify reader type')


st.subheader("Main character information")
name = st.text_input("Full name")

st.text("Date of birth")
col1, col2, col3 = st.columns(3)
with col1:
  year = st.number_input("Year")
with col2:
  month = st.number_input("Month")
with col3:
  day = st.number_input("Day")
  
st.selectbox("Gender", ["Male", "Female", "Animal"])


st.subheader("General story characteristics")

time = st.text_input("When did the story take place")
place = st.text_input("Where did the story take place?")
extra_specs = st.text_input("Any specifics about the time or place that would help bring the story to life? (optional)")

rememberance = st.text_input("Why do you want this story remembered? (optional)")
small_specs = st.text_input("Anything else that should be in the story? Funny details, exact phrases, or how the ending should feel?” (short paragraph)")

reader_info = {"type": reader_type, "age": age, "gender": gender, "realtionship": relationship}
main_character_info = {"name": name, "birthdate": f"{str(year)}-{str(month)}-{str(day)}"}
story_info = {"time": time, "place": place, "extra": extra_specs, "small": small_specs}
cat_desc = f"{category}: {desc}"

gen_button = st.button("Generate story")
if gen_button:
  try:
    story = write_story(cat_desc, reader_info, main_character_info, story_info) 
    st.session_state.story = story
  except Exception as e:
    st.error(f"Error generating the story: \n {str(e)}")
  
if st.session_state.story:
  st.write(story)
