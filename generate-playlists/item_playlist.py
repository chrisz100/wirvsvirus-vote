# -*- coding: utf-8 -*-

# Populate youtube playlists with videos matched in VIDEO_MAPPING file

from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
import csv
from itertools import repeat
import logging
import os
from random import shuffle
from time import sleep

import youtube_wrapper

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s:%(message)s',
                    level=logging.INFO)

mapping_file = os.environ["VIDEO_MAPPING"]

def get_playlist_items(playlist_id, client):
    logging.info('Getting playlist items for playlist %s', playlist_id)
    playlist_response = (
        client.playlistItems()
        .list(
            part="snippet",
            maxResults=50,
            playlistId=playlist_id,
        )
        .execute()
    )
    items = playlist_response["items"]

    nextPageToken = playlist_response.get("nextPageToken")
    while nextPageToken:
        playlist_response = (
            client.playlistItems()
            .list(
                part="snippet",
                playlistId=playlist_id,
                maxResults="50",
                pageToken=nextPageToken,
            )
            .execute()
        )
        items.extend(playlist_response["items"])
        nextPageToken = playlist_response.get("nextPageToken")
    
    return [item['snippet']['resourceId']['videoId'] for item in items]

def run_insert(args):
    client, (playlist, videos) = args
    logging.info("Adding up to %d videos to playlist %s", len(videos), playlist)

    # check if video is already in list
    existing_videos = get_playlist_items(playlist, client)

    for video in videos:    
        if video in existing_videos:
            logging.warning('Not adding %s to playlist %s', video, playlist)
            continue

        logging.info('Adding %s to playlist %s', video, playlist)

        try:
            response = client.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist,
                        "position": 0,
                        "resourceId": {"kind": "youtube#video", "videoId": video},
                    },
                },
            ).execute()
            logging.info('Inserted video %s into playlist %s', video, playlist)
        except BaseException as e:
            logging.error('Inserting video %s failed: %s', video, e)

    return response


def main():
    client = youtube_wrapper.get_authenticated_service()

    with open(mapping_file, newline='') as f:
        data = csv.reader(f, delimiter='\t')
        playlist_array = list(data)

    # Group videos by playlist
    playlists = defaultdict(list)
    for video, playlist in playlist_array:
        playlists[playlist].append(video)
        
    with ProcessPoolExecutor() as executor:
        playlists = executor.map(run_insert, zip(repeat(client), playlists.items()))

    logging.info('Finished')

if __name__ == "__main__":
    main()
