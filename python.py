import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic

# Spotify Credentials
SPOTIFY_CLIENT_ID = 'your_spotify_client_id'
SPOTIFY_CLIENT_SECRET = 'your_spotify_client_secret'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

def get_spotify_playlist_tracks(playlist_url):
    """Retrieve tracks from a Spotify playlist."""
    results = sp.playlist_tracks(playlist_url)
    tracks = []
    for item in results['items']:
        track = item['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        tracks.append(f"{track_name} {artist_name}")
    return tracks

# YouTube Music Authentication
ytmusic = YTMusic('headers_auth.json')  # Download 'headers_auth.json' using ytmusicapi setup

def create_youtube_playlist(playlist_name, description, tracks):
    """Create a YouTube Music playlist and add tracks."""
    playlist_id = ytmusic.create_playlist(playlist_name, description)
    for track in tracks:
        search_results = ytmusic.search(track, filter="songs")
        if search_results:
            song_id = search_results[0]['videoId']
            ytmusic.add_playlist_items(playlist_id, [song_id])
    return playlist_id

# Main Process
if __name__ == "__main__":
    spotify_playlist_url = "your_spotify_playlist_url"  # Replace with your Spotify playlist URL
    playlist_name = "Your New Playlist"  # Name for the new YouTube Music playlist
    playlist_description = "Playlist migrated from Spotify"

    print("Fetching Spotify playlist tracks...")
    spotify_tracks = get_spotify_playlist_tracks(spotify_playlist_url)

    print("Creating YouTube Music playlist and adding tracks...")
    youtube_playlist_id = create_youtube_playlist(playlist_name, playlist_description, spotify_tracks)

    print(f"Playlist created successfully on YouTube Music! Playlist ID: {youtube_playlist_id}")
