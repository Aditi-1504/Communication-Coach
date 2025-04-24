def save_report_html(data):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Communication Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background: #f5f6fa;
                color: #333;
            }}
            h1 {{ color: #2c3e50; }}
            h2 {{ color: #34495e; margin-top: 20px; }}
            ul {{ padding-left: 20px; }}
            li {{ margin-bottom: 5px; }}
        </style>
    </head>
    <body>
        <h1>🚀 Communication Report</h1>

        <h2>Speaking Time</h2>
        <ul>
            {''.join(f'<li>{speaker}: {time} seconds</li>' for speaker, time in data['speaking_time'].items())}
        </ul>

        <h2>Top Mistakes</h2>
        <ul>
            {''.join(f'<li>{mistake}</li>' for mistake in data['top_mistakes'])}
        </ul>

        <h2>Tone</h2>
        <p>{data['tone_professionalism']}</p>

        <h2>Pitch Feedback</h2>
        <p>{data['pitch_feedback']}</p>

        <h2>Soft Skills</h2>
        <p>{data['soft_skills']}</p>

        <h2>Vocabulary Tips</h2>
        <ul>
            {''.join(f'<li>{tip}</li>' for tip in data['vocabulary_tips'])}
        </ul>

        <h2>Overall Sentiment</h2>
        <p>{data['overall_sentiment']}</p>
    </body>
    </html>
    """

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)
