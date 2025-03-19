import streamlit as st
import os
from backend.video_processing import scan_directory_for_videos, load_video_clip
from backend.model_inference import run_model_inference

st.title("Video Event Viewer")

# --- Video Directory Scanning ---
video_dir = st.text_input("Enter video directory path", value="/path/to/videos")

if st.button("Scan Videos"):
    if os.path.isdir(video_dir):
        videos = scan_directory_for_videos(video_dir)
        if videos:
            st.session_state.videos = videos
            st.success(f"Found {len(videos)} videos.")
        else:
            st.warning("No videos found in the specified directory.")
    else:
        st.error("Invalid directory path.")

# --- Video Selection ---
if "videos" in st.session_state:
    selected_video = st.selectbox("Select a Video", st.session_state.videos)
else:
    selected_video = None

# Hardcoded clip selection for demonstration purposes.
clip = st.selectbox("Select a Clip", ["Clip A", "Clip B"])

if selected_video:
    st.write("Selected video:", selected_video)
    
    # --- Video Display ---
    # Note: st.video expects a URL or binary data. Here, we try to read and display the file.
    try:
        with open(selected_video, "rb") as video_file:
            video_bytes = video_file.read()
            st.video(video_bytes)
    except Exception as e:
        st.error(f"Error loading video: {e}")

# --- Model Selection and Prompt Input ---
model = st.selectbox("Select Model", ["Model A", "Model B", "LLM Model"])
prompt = st.text_area("Enter Prompt", "")

# --- Run Inference ---
if st.button("Run Inference"):
    if selected_video:
        clip_data = load_video_clip(selected_video, clip)
        predictions = run_model_inference(clip_data, prompt, model)
        st.subheader("Predictions (Events):")
        for event in predictions:
            st.write(f"- {event}")
    else:
        st.error("No video selected!")
