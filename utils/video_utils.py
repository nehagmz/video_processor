import logging
import os

# Set up logging configuration
def setup_logging():
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(filename=os.path.join(log_dir, 'processing_logs.txt'), level=logging.INFO,
                        format='%(asctime)s - %(message)s')

# Log a message to both the console and the log file
def log_message(message):
    logging.info(message)
    print(message)

# Function to check if the video file exists
def check_video_file(file_path):
    if not os.path.exists(file_path):
        log_message(f"Error: Video file not found at {file_path}")
        return False
    return True

# Function to validate video format (optional)
def validate_video_format(file_path, allowed_formats=[".mp4", ".avi", ".mov"]):
    if os.path.splitext(file_path)[1].lower() not in allowed_formats:
        log_message(f"Error: Unsupported video format '{file_path}'")
        return False
    return True
