import streamlit as st
from sorter import sort_files
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="File Sorter", layout="centered", page_icon="📂")

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

st.title("📁 File Sorter Web App")
st.write("Organize your files by type and date automatically!")

folder_path = st.text_input("Enter the folder path to sort:")

use_date_sort = st.checkbox("Sort files into Year-Month folders")
show_logs = st.checkbox("Show log after sorting")

if st.button("Sort Files") and folder_path:
    folder = Path(folder_path)
    
    if not folder.exists():
        st.error("❌ Folder does not exist!")
    else:
        with st.spinner("Sorting files... ⏳"):
            moved_files = sort_files(folder_path)  
            
        st.success(f"✅ Sorted {len(moved_files)} files!")

        progress = st.progress(0)
        for i in range(len(moved_files)):
            progress.progress((i+1)/len(moved_files))

        with st.expander("See Moved Files"):
            for f in moved_files:
                st.write(f)
        
        if show_logs:
            log_file = Path("logs/file_log.txt")
            if log_file.exists():
                st.subheader("📄 Log File")
                st.text(log_file.read_text())

st.markdown("---")
st.markdown("Created by **Aakash D** | Streamlit File Sorter Project")
