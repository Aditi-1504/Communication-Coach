from textblob import TextBlob
import random

def generate_report(transcript_text):
    return {
        "speaking_time": {"Speaker 1": 300, "Speaker 2": 200, "Speaker 3": 100},
        "top_mistakes": ["Used 'um' 12 times", "Interrupted others"],
        "tone_professionalism": "Professional mostly, slight casualness detected",
        "pitch_feedback": "Good energy, but too many buzzwords",
        "soft_skills": "Polite and responsive",
        "vocabulary_tips": ["Replace 'awesome' with 'exceptional'"],
        "overall_sentiment": random.choice(["Positive", "Neutral", "Negative"])
    }