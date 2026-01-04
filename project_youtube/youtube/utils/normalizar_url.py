from script_youtube_imports import video_id
from youtube.models import Video

BASE_URL = "https://www.youtube.com/watch?v="

def normalizar_url(url):
        return f"{BASE_URL}{video_id}"


