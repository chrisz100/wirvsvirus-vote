import random
from flask import redirect

def random_video(request):
    playlists = []

    try:
        playlist_identifier = playlists[random.randrange(0, len(playlists))]
        return redirect('https://www.youtube.com/playlist?list={playlist}'.format(playlist=playlist_identifier))
    except:
        return f'Playlist not found'

    