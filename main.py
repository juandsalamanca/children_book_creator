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
st.text(desc)

reader_type_list = ['Individual reader', 'The whole family', 'General audience', 'Other']
reader_type = st.selectbox('Reader Type', reader_type_list)
if reader_type == 'Individual reader':
  age = st.text_input('Age')
  gender = st.text_input('Gender')
  relationship = st.text_input('Relationship to main character')
elif reader_type == 'Other':
  other_reader_type = st.text_input('Specify reader type')
