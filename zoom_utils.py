import os

def find_latest_audio_recording(root_dir):
    """
    This function walks through the given root directory, looks for `.m4a` audio files, 
    and returns the latest one based on the last modified time.
    """
    latest_file = None
    latest_time = 0

    # Walk through the directory and subdirectories
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Only consider .m4a files (audio recordings)
            if file.endswith('.m4a'):
                full_path = os.path.join(root, file)
                file_time = os.path.getmtime(full_path)  # Get last modified time of the file
                
                # If this file is newer, update the latest file
                if file_time > latest_time:
                    latest_time = file_time
                    latest_file = full_path

    return latest_file
