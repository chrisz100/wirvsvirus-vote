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

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret_youtube.json"

videos = ["aMkiOjj8Vnc"]


def get_authenticated_service():
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_console()
    youtube = build(api_service_name, api_version, credentials=credentials)
    return youtube


def run_insert(client):

    for video in videos:
        client.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": "PLFxt3hgAGmJWx5N1uJ7Ka0xByzCm4y_La",
                    "position": 0,
                    "resourceId": {"kind": "youtube#video", "videoId": video},
                }
            },
        ).execute()

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
