import requests

def get_zoom_recording(meeting_id, access_token):
    url = f"https://api.zoom.us/v2/meetings/{meeting_id}/recordings"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # Find M4A audio file
    for file in data.get('recording_files', []):
        if file['file_type'] == 'M4A':
            return {'download_url': file['download_url']}

    # Fallback to first file
    if data.get('recording_files'):
        return {'download_url': data['recording_files'][0]['download_url']}
    
    return None
