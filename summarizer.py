from youtube_transcript_api import YouTubeTranscriptApi

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video_id = "dQw4w9WgXcQ" # You need to extract this ID from the URL

try:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

    # Combine the dictionary text into a single string for your summarizer
    full_text = " ".join([t['text'] for t in transcript_list])
    print(full_text)

except Exception as e:
    print(f"Error: {e}")