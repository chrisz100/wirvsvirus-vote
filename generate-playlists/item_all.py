# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

from time import sleep
import csv

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = os.environ["SECRET"]

mapping_file = os.environ["VIDEO_MAPPING"]
# video_dictionary = {}
video_array = []


def get_authenticated_service():
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_console()
    youtube = build(api_service_name, api_version, credentials=credentials)
    return youtube


def run_insert(client):
    # First, we read the values from a file into our dictionary
    with open(mapping_file) as f:
        video_array = [line.rstrip("\n") for line in f]

    # Then loop over the dictionary and add videos to playlists
    for video_id in video_array:
        client.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    # We are putting all videos into the full playlist, hence hard coding the ID
                    "playlistId": "PLYGe9q9_Jo3AhwDdN4qvhvqTSgfCdYRGD",
                    "position": 0,
                    "resourceId": {"kind": "youtube#video", "videoId": video_id},
                }
            },
        ).execute()
        ## Wait 50 ms after each insert
        # sleep(0.05)

    return "Done"


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client = get_authenticated_service()

    response = run_insert(client)

    print(response)


if __name__ == "__main__":
    main()
