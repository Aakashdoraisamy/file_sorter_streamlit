# app.py

import streamlit as st
from sorter import sort_files
from pathlib import Path
from PIL import Image

# Page config
st.set_page_config(page_title="File Sorter", layout="centered", page_icon="📂")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 10px;
        font-size:16px;
    }
    .stTextInput>div>div>input {
        height: 2.5em;
        font-size:16px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📁 File Sorter Web App")
st.write("Organize your files by type and date automatically!")

# Optional: Add an image/banner
# image = Image.open("banner.png")
# st.image(image, use_column_width=True)

# Folder input
folder_path = st.text_input("Enter the folder path to sort:")

# Checkboxes for extra features
use_date_sort = st.checkbox("Sort files into Year-Month folders")
show_logs = st.checkbox("Show log after sorting")

# Sort button
if st.button("Sort Files") and folder_path:
    folder = Path(folder_path)
    
    if not folder.exists():
        st.error("❌ Folder does not exist!")
    else:
        with st.spinner("Sorting files... ⏳"):
            moved_files = sort_files(folder_path)  # Your sorter.py handles date sorting
            
        st.success(f"✅ Sorted {len(moved_files)} files!")

        # Progress bar
        progress = st.progress(0)
        for i in range(len(moved_files)):
            progress.progress((i+1)/len(moved_files))
        
        # Show moved files
        with st.expander("See Moved Files"):
            for f in moved_files:
                st.write(f)
        
        # Show logs
        if show_logs:
            log_file = Path("logs/file_log.txt")
            if log_file.exists():
                st.subheader("📄 Log File")
                st.text(log_file.read_text())

# Footer / credits
st.markdown("---")
st.markdown("Created by **Aakash D** | Streamlit File Sorter Project")
