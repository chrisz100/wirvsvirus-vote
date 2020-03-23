# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import csv
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
import logging
import os
from random import shuffle
from time import sleep

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s:%(message)s',
                    level=logging.INFO)

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = os.environ["SECRET"]
mapping_file = os.environ["VIDEO_MAPPING"]

playlist_prefix = '#wirvsvirushack Alle Projekte #'

playlists_all_videos = []

def get_authenticated_service(secrets_file):
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        secrets_file, scopes
    )
    credentials = flow.run_console()
    youtube = build(api_service_name, api_version, credentials=credentials)
    return youtube


def run_insert(args):
    client, playlist = args

    # # Create new playlist
    # request = client_playlist.playlists().insert(
    #     part="snippet,status",
    #     body={
    #       "snippet": {
    #         "title": f"{playlist_prefix}{position}",
    #         "description": f"{playlist_prefix}{position}",
    #         "tags": [
    #           "#WeVsVirus",
    #           "Hackathon"
    #         ],
    #         "defaultLanguage": "de"
    #       },
    #       "status": {
    #         "privacyStatus": "unlisted"
    #       }
    #     }
    # )
    # try:
    #     playlist = request.execute()
    # except BaseException as e:
    #     logging.error('Failed creating playlist: %s', e)
    #     backoff_time = 1.5**backoff * 60
    #     logging.info('Sleeping for %ss', backoff_time)
    #     sleep(backoff_time)
    #     return run_insert((client_playlist, client, position, backoff + 1))
    # else:
    #     logging.info('Created playlist: %s', playlist)

    # First, we read the values from a file into our dictionary
    with open(mapping_file) as f:
        video_array = [line.rstrip("\n") for line in f]
    shuffle(video_array)

    # Then loop over the dictionary and add videos to playlists
    for video_id in video_array:
        try:
            response = client.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist,
                        "position": 0,
                        "resourceId": {"kind": "youtube#video", "videoId": video_id},
                    },
                },
            ).execute()
            logging.info('Inserted video into playlist %s: %s', playlist['id'], response)
        except:
            logging.error('Inserting video failed: %s', video_id)

    return playlist


def main():
    print('_________ Video Client _________')
    client_video = get_authenticated_service(client_secrets_file)

    with ProcessPoolExecutor() as executor:
        playlists = executor.map(run_insert, zip(repeat(client_video), playlists_all_videos))

    playlist_ids = [playlist['id'] for playlist in playlists]
    logging.info('Done! playlists: %s', playlist_ids)

if __name__ == "__main__":
    main()
