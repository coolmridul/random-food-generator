import streamlit as st
import random
from googlesheet import *


# Set page config to wide mode and add custom CSS
st.set_page_config(layout="wide", page_title="Random Generator")

# Custom CSS to maximize height and add some styling
st.markdown("""
    <style>
        .main {
            padding-top: 0rem;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;
            border: 2px black;
        }
        .stButton>button {
            width: 100%;
            padding: 1rem;
            font-size: 1.2rem;
        }
        .st-emotion-cache-16idsys p {
            font-size: 20px;
        }
        .st-emotion-cache-q8sbsg p {
            font-size: 18px;
        }
        .random-result {
            font-size: 24px;
            text-align: center;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            background-color: #f0f2f6;
        }
    </style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Random Item Generator</h1>", unsafe_allow_html=True)

# Initialize the list in session state if it doesn't exist
if 'items' not in st.session_state:
    st.session_state['items'] = get_data_from_google_sheet('Sheet1')

# Create two columns with custom width
col1, col2 = st.columns([2, 1])

# Column 1: List management
with col2:
    st.markdown("<h2 style='text-align: center;'>List Management</h2>", unsafe_allow_html=True)
    
    # Add new item with placeholder
    new_item = st.text_input("", placeholder="Enter new item here...")
    if st.button("➕ Add Item", key="add_button"):
        if new_item:
            st.session_state['items'].append(new_item)
            push_data_to_google_sheet('Sheet1',data=[new_item])
            st.success(f"Added: {new_item}")
    
    # Display the list with a container
    st.markdown("<h3>Current List</h3>", unsafe_allow_html=True)
    list_container = st.container()
    with list_container:
        if not st.session_state['items']:
            st.info("Your list is empty. Add some items above!")
        for idx, item in enumerate(st.session_state['items'], 1):
            st.write(f"{idx}. {item}")

# Column 2: Random Generator
with col1:
    st.markdown("<h2 style='text-align: center;'>Random Generator</h2>", unsafe_allow_html=True)
    
    # Store random selection in session state
    if 'random_selection' not in st.session_state:
        st.session_state['random_selection'] = None
    
    # Centered generate button
    if st.button("🎲 Generate Random", key="generate_button"):
        if st.session_state['items']:
            st.session_state['random_selection'] = random.choice(st.session_state['items'])
        else:
            st.warning("Add some items to the list first!")

    # Display random selection
    if st.session_state['random_selection']:
        st.markdown(
            f"""<div class='random-result'>
                <h3>Your Random Selection:</h3>
                <p style='font-size: 32px; font-weight: bold; color: #ff4b4b;'>
                    {st.session_state['random_selection']}
                </p>
            </div>""", 
            unsafe_allow_html=True
        )

# # Add footer
# st.markdown("""
#     <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: #f0f2f6;'>
#         <p style='color: #666666;'>Made with ❤️ by Mridul</p>
#     </div>
# """, unsafe_allow_html=True)
