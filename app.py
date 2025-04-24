from flask import Flask, request, jsonify
from analysis import generate_report
from zoom_handler import get_zoom_recording
from transcription import transcribe, get_transcript_result
import time

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def home():
    return "✅ Flask App Running. Waiting for Zoom to send data..."
def webhook():
    data = request.json
    print("Webhook Received!", data)

    meeting_id = data['payload']['object']['id']
    print(f"Meeting ID received from webhook: {meeting_id}")

    # 1. Get the Zoom Recording
    access_token = 'eyJzdiI6IjAwMDAwMiIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6IjBjMjRhZmQ2LTlhZWYtNDdiYi1iNjFiLWY2YWE3NDJiZGVjOCJ9.eyJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJCZ21xVF9kRVM3ZUIzMFRodEJxUzZRIiwidmVyIjoxMCwiYXVpZCI6IjlhOWY1OGJlOWFiNGMzNTBjZjRmYTllYWI5YzA4ODEyYjMwZGU0ZDMzMmM1NDllMDcyYmQ3ODc4ZmRhOGY2OTkiLCJuYmYiOjE3NDU0MjI1MjIsImNvZGUiOiJ5MDR2M0FsU1N4Q09jMlN2c3JRUGFRekJWcDAzdTVMQjUiLCJpc3MiOiJ6bTpjaWQ6cEJPb3FnakZTS21hYm5JS05mV2lhdyIsImdubyI6MCwiZXhwIjoxNzQ1NDI2MTIyLCJ0eXBlIjozLCJpYXQiOjE3NDU0MjI1MjIsImFpZCI6InR5ZEZJcWx0UmwtV1AtSEF1ZUZ3OVEifQ.AzjxDj0oeUE2ll1LNUbUUeJnLCjUW3XPmGJm9WDQAqCpLb_49DxmAqTtk0stOX0YRa8AVekbfhvdTOLB5TxMOw'  
    recording_info = get_zoom_recording(meeting_id, access_token)

    if not recording_info:
        return jsonify({'error': 'No recording found'}), 400

    audio_download_link = recording_info['download_url']

    # 2. Send audio to AssemblyAI
    transcript_id = transcribe(audio_download_link)

    # 3. Poll for transcript result
    while True:
        result = get_transcript_result(transcript_id)
        if result['status'] == 'completed':
            print("Transcript Ready!")
            transcript_text = result['text']
            break
        elif result['status'] == 'failed':
            print("Transcript Failed!")
            return jsonify({'error': 'Transcription failed'}), 500
        time.sleep(5)  # wait 5 seconds

    # 4. Generate report
    report_data = generate_report(transcript_text)
    
    # For now just print the report
    print("Generated Report:", report_data)

    return jsonify({'message': 'Report generated successfully!'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
