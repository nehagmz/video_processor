import os
from moviepy import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

if not os.path.exists('sample_videos/output'):
    os.makedirs('sample_videos/output')

# Function to load and display video details
def load_video(video_path):
    try:
        video_clip = VideoFileClip(video_path)
        print(f"Video loaded successfully: {video_clip.filename}")
        print(f"Duration: {video_clip.duration} seconds")
        print(f"Frame rate: {video_clip.fps} fps")
        print(f"Resolution: {video_clip.size}")
        return video_clip
    except Exception as e:
        print(f"Error loading video: {e}")
        return None

# Function to trim video from start_time to end_time
def trim_video(video_clip, start_time, end_time):
    # Ensure that the end_time does not exceed the video duration
    if end_time > video_clip.duration:
        end_time = video_clip.duration
    try:
        # Define the output path for the trimmed video
        output_path = "sample_videos/output/trimmed_video.mp4"
        # Use ffmpeg_extract_subclip to trim the video
        ffmpeg_extract_subclip(video_clip.filename, start_time, end_time, output_path)
        print(f"Trimmed video saved to: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error saving trimmed video: {e}")
        return None
    
# Main script execution
if __name__ == "__main__":
    video_path = "sample_videos/input/sample_video.mp4"
    # Load video
    video = load_video(video_path)
    if video:
        # Trim video (example: from 5s to 10s)
        trimmed_video_path = trim_video(video, 5, 10)
        if trimmed_video_path:
            print(f"Trimming successful.")
