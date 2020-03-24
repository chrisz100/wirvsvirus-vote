# -*- coding: utf-8 -*-

# Generate and populate 100 playlists on youtube

import csv
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
import logging
import os
from random import shuffle
from time import sleep

import youtube_wrapper

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s:%(message)s',
                    level=logging.INFO)

mapping_file = os.environ["VIDEO_MAPPING"]
output_file = os.environ["OUTPUT_FILE"]
playlist_prefix = '#wirvsvirushack Alle Projekte #'

def run_insert(args):
    client, position, backoff = args

    # Create new playlist
    request = client.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": f"{playlist_prefix}{position}",
            "description": f"{playlist_prefix}{position}",
            "tags": [
              "#WeVsVirus",
              "Hackathon"
            ],
            "defaultLanguage": "de"
          },
          "status": {
            "privacyStatus": "unlisted"
          }
        }
    )
    try:
        playlist = request.execute()
    except BaseException as e:
        logging.error('Failed creating playlist: %s', e)
        backoff_time = 1.5**backoff * 60
        logging.info('Sleeping for %ss', backoff_time)
        sleep(backoff_time)
        return run_insert((client, position, backoff + 1))
    else:
        logging.info('Created playlist: %s', playlist)

        # First, we read the values from a file into our dictionary
        with open(mapping_file) as f:
            video_array = [line.rstrip("\n") for line in f]
        shuffle(video_array)

        # Then loop over the dictionary and add videos to playlists
        for i, video_id in enumerate(video_array):
            try:
                response = client.playlistItems().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": playlist['id'],
                            "position": i,
                            "resourceId": {"kind": "youtube#video", "videoId": video_id},
                        },
                    },
                ).execute()
                logging.info('Inserted video %s into playlist %s', video_id, playlist['id'])
            except:
                logging.error('Inserting video failed: %s: %s', video_id, playlist['id'])

        return playlist


def main():
    client = youtube_wrapper.get_authenticated_service()

    with ProcessPoolExecutor() as executor:
        playlists = executor.map(run_insert, zip(repeat(client), range(100), repeat(1)))

    playlist_ids = [playlist['id'] for playlist in playlists]
    logging.info('Done! playlists: %s', playlist_ids)

    with open(output_file, 'w') as f:
        f.write(str(playlist_ids))

if __name__ == "__main__":
    main()
