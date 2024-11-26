# Spotify to YouTube Music Playlist Migrator

This Python project allows you to transfer a playlist from Spotify to YouTube Music. Using Spotify's API and YouTube Music's API, the program fetches tracks from a Spotify playlist and creates a new playlist on YouTube Music with the same tracks.

---

## Features

- Fetch all tracks from a Spotify playlist.
- Search and add tracks to a new YouTube Music playlist.
- Automate playlist migration between platforms.

---

## Prerequisites

1. **Python**: Ensure Python 3.6 or higher is installed on your machine.
2. **Spotify API Credentials**:
   - Create a developer app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Obtain the `client_id` and `client_secret`.

3. **YouTube Music API Authentication**:
   - Install and configure `ytmusicapi` following [these steps](https://ytmusicapi.readthedocs.io/en/latest/setup.html).
   - Generate a `headers_auth.json` file for authentication.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ak18akashrajr/Spotify-to-YouTube-Playlist.git
   cd Spotify-to-YouTube-Playlist
