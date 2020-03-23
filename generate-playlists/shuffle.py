# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.update
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

from random import randint
from time import sleep

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = os.environ["SECRET"]

# TODO: Enter Playlist IDs
playlist_ids = ["12345"]


def get_authenticated_service():
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_console()
    youtube = build(api_service_name, api_version, credentials=credentials)
    return youtube


def run_shuffle(client):

    # Go through all playlists in a first loop
    for my_playlist_id in playlist_ids:
        playlist_response = (
            client.playlistItems()
            .list(
                part="id,snippet",
                # part="snippet,contentDetails",
                # maxResults=25,
                playlistId=my_playlist_id,
            )
            .execute()
        )

        # We need only the items out of this response
        # Structure of response can be found here:
        # https://developers.google.com/youtube/v3/docs/playlistItems/list#response_1
        playlist_items = playlist_response.items

        playlist_size = len(playlist_items)

        # For each item in this playlist, update the position with a random number
        for my_playlist_item in playlist_items:
            client.playlistItems().update(
                part="snippet",
                body={
                    "id": my_playlist_item.id,
                    "snippet": {
                        "playlistId": my_playlist_id,
                        "position": randint(0, playlist_size - 1),
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": my_playlist_item.snippet.resourceId.videoId,
                        },
                    },
                },
            ).execute()
        # Wait 50 ms after each shuffle
        sleep(0.05)

    return "Shuffle done"


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client = get_authenticated_service()

    response = run_shuffle(client)

    print(response)


if __name__ == "__main__":
    main()
