import time
from transcription import transcribe, get_transcript_result
from analysis import generate_report
from zoom_utils import find_latest_audio_recording
from report_writer import save_report_html
import webbrowser

def process_zoom_audio():
    print("🔍 Watching for new Zoom recordings...")

    latest_file = find_latest_audio_recording("C:/Users/Aditi Agarwal/Documents/Zoom")
    if not latest_file:
        print("No audio files found.")
        return

    print(f"🎙️ New audio found: {latest_file}")

    # Step 1: Transcribe
    transcript_id = transcribe(latest_file)
    print(f"📝 Transcription started... ID: {transcript_id}")

    # Step 2: Poll for results
    while True:
        result = get_transcript_result(transcript_id)
        if result['status'] == 'completed':
            print("✅ Transcription complete!")
            transcript_text = result['text']
            break
        elif result['status'] == 'failed':
            print("❌ Transcription failed.")
            return
        time.sleep(2)

    # Step 3: Generate Report
    report = generate_report(transcript_text)

    # Step 4: Output
    print("\n📊 Communication Report:")
    for key, value in report.items():
        print(f"{key}: {value}")

    # Step 5: Save and open HTML report automatically
    save_report_html(report)
    print("\n📄 HTML report saved as 'report.html'. Opening in browser...")
    webbrowser.open("report.html")

if __name__ == "__main__":
    process_zoom_audio()
