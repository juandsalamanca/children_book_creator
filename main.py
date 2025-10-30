import streamlit as st
import openai
from src.gpt_functions import write_story
from pypdf import PdfReader

st.header('StoryKin')

if "story" not in st.session_state:
  st.session_state.story = None

#------------------------------------------------------------------------
# Story category
#------------------------------------------------------------------------

category_list = ['Faith & Spirituality', 'Lessons & Values', 'Traditions & Celebrations', 'Love, Legacy & Legends']
category_desc_map = {"Faith & Spirituality": "Moments that connect us to God, hope or quiet wonder.",
                     "Lessons & Values": "Stories that shape beliefs, courage or character.",
                     "Traditions & Celebrations": "Stories tie to holidays, rituals, or family customs",
                     "Love, Legacy & Legends": "Stories that show who we are, how we love, and what we carry forward."}

category = st.selectbox('Category', category_list)
desc = category_desc_map[category]
st.write(desc)

#------------------------------------------------------------------------
# Reader information
#------------------------------------------------------------------------

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

#------------------------------------------------------------------------
# Main character information
#------------------------------------------------------------------------

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

#------------------------------------------------------------------------
# Story characteristics
#------------------------------------------------------------------------

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

#------------------------------------------------------------------------
# Upload base story
#------------------------------------------------------------------------

if "base_story" not in st.session_state:
  st.session_state.base_story = None

upload = st.selectbox("Select how to upload the story", ["File upload (PDF)", "Paste text", "Dictate story (Speech-to-text)"])

if "File" in upload:
  uploaded_files = st.file_uploader(
      "Upload you story", accept_multiple_files=True, type="pdf"
  )
  for uploaded_file in uploaded_files:
    if uploaded_file is not None:
      reader = PdfReader(uploaded_file)
      base_story = ""
      for page in reader.pages:
        base_story += page.extract_text()
      st.text_area("Extracted Story Text", base_story, height=300)

  st.session_state.base_story = base_story

elif "Paste" in upload:
  st.session_state.base_story = st.text_area("Paste your story text here")

elif "Dictate" in upload:
  st.write("Speech-to-text functionality coming soon!")


#------------------------------------------------------------------------
# Summary and Highlights
#------------------------------------------------------------------------

st.subheader("Story Summary and Highlights")
emphasis = st.text_input("Any parts you especially want featured or emphasized")
censored = st.text_input("Is there anything we should leave out or treat with sensitivity?")
context = st.text_input("Any context to the story we should know?")

personal_note = st.text_area("Add a personal note to be included with the story (optional)")

highlights = {"emphasis": emphasis, "censored": censored, "context": context, "personal_note": personal_note}

#------------------------------------------------------------------------
# Narrative Style & Perspective 
#------------------------------------------------------------------------

st.subheader("Narrative Style & Perspective")

perspective = st.selectbox("Preferred narrative style", ["First-person", "Third-person", "Omniscient narrator"])
narrator = st.selectbox("Preferred narrator", ["Grandparent", "Parent", "Friend", "Child", "Other"])

if narrator == "Other":
  narrator = st.text_input("Specify narrator")

tone = st.selectbox("Preferred tone", ["Heartfelt", "Funny", "Reflective", "Simple & Sweet", "Poetic", "Let us decide", "Other"])
if tone == "Other":
  tone = st.text_input("Specify tone")

narrative = {"perspective": perspective, "narrator": narrator, "tone": tone}

#------------------------------------------------------------------------
# Character descriptions
#------------------------------------------------------------------------

st.subheader("Character Descriptions")
main_characters_data = []
number_of_main_characters = st.number_input("Number of main characters (including the protagonist)", min_value=1, max_value=5, value=1)
for i in range(int(number_of_main_characters)):
  char_name = st.text_input(f"Name of main character {i+1}")
  char_desc = st.text_area(f"Description of main character {i+1} (appearance, personality, role in story)")

  main_characters_data.append({"name": char_name, "description": char_desc})

#------------------------------------------------------------------------
# Story length & Format
#------------------------------------------------------------------------

story_length = st.selectbox("Preferred story length", ["Tiny tales", "Short & Sweet", "The Whole Story"])
if story_length == "Tiny tales":
  length_desc = "Simple, quick reads with big , 150-350 words, 1-2 minute read, 6-8 illustrated scenes, 16 pages, Story Pages with text - abt 12"
elif story_length == "Short & Sweet":
  length_desc = "classic picture book feel, a bit more detail, 350-600 words, 3-4 minute read, 8-12 illustrated scenes, 24 pages, Story Pages with text - abt 18"
else:
  length_desc = "longer narrative, more plot & description, 600-900 words, 5-6 minute read, 12-14 illustrated scenes, 28-32 pages, Story Pages with text - abt 22-26"

format = {"story_length": story_length, "length_description": length_desc}
#------------------------------------------------------------------------
# Illustration
#------------------------------------------------------------------------

illustration_style = st.selectbox("Preferred illustration style", ["Watercolor", "Realistic", "Vintage Sketch", "Modern Minimalist", "Playful Tale"])
if illustration_style == "Watercolor":
  illustration_description = "Universally loved for keepsakes; soft, timeless, and emotional."
elif illustration_style == "Realistic":
  illustration_description = "Perfect for people who want an accurate likeness of their loved one."
elif illustration_style == "Vintage Sketch":
  illustration_description = "A nod to heritage and nostalgia, great for legacy stories."
elif illustration_style == "Modern Minimalist":
  illustration_description = "Clean and fresh for those with contemporary tastes."
else:
  illustration_description = "Cartoon like images. Perfect for capturing lighthearted stories."
st.write(illustration_description)

includes = st.text_input("People, animals or objects to include: (short text field/list)")
uploaded_files = st.file_uploader(
      "Upload a Photo(s) (Optional) ", accept_multiple_files=True, type="pdf"
  )
photo_list = []
for uploaded_file in uploaded_files:
  if uploaded_file is not None:
    photo_list.append(uploaded_file)

layout = st.selectbox("Preferred layout", ["Full-page illustrations",  "Double-page spreads", "Spot illustrations", "Mix of all", "Let us decide"])

#------------------------------------------------------------------------
# Generate story
#------------------------------------------------------------------------

gen_button = st.button("Generate story")
if gen_button:
  try:
    story = write_story(st.session_state.base_story, cat_desc, reader_info, main_character_info, story_info, highlights, narrative, main_characters_data, format) 
    st.session_state.story = story
  except Exception as e:
    st.error(f"Error generating the story: \n {str(e)}")
  
if st.session_state.story:
  st.write(st.session_state.story)