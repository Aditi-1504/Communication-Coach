import requests

ASSEMBLYAI_API_KEY = 'c14b80f7ca714bb9954526beeed76f5c'

def upload_file(file_path):
    CHUNK_SIZE = 5_242_880  # ~5MB
    headers = {'authorization': ASSEMBLYAI_API_KEY}

    def read_file(file_path):
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    response = requests.post(
        'https://api.assemblyai.com/v2/upload',
        headers=headers,
        data=read_file(file_path)
    )

    return response.json()['upload_url']


def transcribe(file_path):
    audio_url = upload_file(file_path)
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = { "audio_url": audio_url }
    headers = { "authorization": ASSEMBLYAI_API_KEY }
    response = requests.post(endpoint, json=json, headers=headers)
    return response.json()['id']

def get_transcript_result(transcript_id):
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    headers = { "authorization": ASSEMBLYAI_API_KEY }
    response = requests.get(endpoint, headers=headers)
    return response.json()
