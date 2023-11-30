import webbrowser
from speak import speak

def play_music_on_youtube(song_name):
    try:
        search_query = f"youtube.com/results?search_query={song_name}"
        webbrowser.open(search_query)
        speak(f"Searching for '{song_name}' on YouTube...")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")
