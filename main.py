import streamlit as st
import openai

st.header('Children book generator')

category_list = ['Faith & Spirituality', 'Lessons & Values', 'Traditions & Celebrations', 'Love, Legacy & Legends']
category_desc_map = {"Faith & Spirituality": "Moments that connect us to God, hope or quiet wonder.",
                     "Lessons & Values": "Stories that shape beliefs, courage or character.",
                     "Traditions & Celebrations": "Stories tie to holidays, rituals, or family customs",
                     "Love, Legacy & Legends": "Stories that show who we are, how we love, and what we carry forward."}

category = st.selectbox('Category', category_list)
desc = category_desc_map[category]
st.write(desc)

st.text("Reader information")
reader_type_list = ['Individual reader', 'The whole family', 'General audience', 'Other']
reader_type = st.selectbox('Reader Type', reader_type_list)
if reader_type == 'Individual reader':
  age = st.text_input('Age')
  gender = st.text_input('Gender')
  relationship = st.text_input('Relationship to main character')
elif reader_type == 'Other':
  other_reader_type = st.text_input('Specify reader type')
  
st.text("Main character information")
st.text_input("Full name")

st.text("Date of birth")
col1, col2, col3 = st.columns(3)
with col1:
  year = st.number_input("Year")
with col2:
  year = st.number_input("Month")
with col3:
  year = st.number_input("Day")
  
st.selectbox("Gender", ["Male", "Female", "Animal"])
st.text("General story characteristics")
st.text_input("When did the story take place")
st.text_input("Where did the story take place?")
st.text_input("Any specifics about the time or place that would help bring the story to life? (optional)")
if reader_type == 'Individual reader':
  st.text_input("Relationship of the main characyer to the main reader")

st.text_input("Why do you want this story remembered? (optional)")
st.text_input("Anything else that should be in the story? Funny details, exact phrases, or how the ending should feel?” (short paragraph)")
