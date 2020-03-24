# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import youtube_wrapper

playlist_names = [
    "Alle Projekte des #wirvsvirushack",
    "Forschung und Tests",
    "Medizinische Versorgung",
    "Mentale Gesundheit",
    "Kreativer Gesundheitsschutz",
    "Datennutzung",
    "Lebensmittelversorgung",
    "Distributionsplattformen",
    "Nachbarschaftshilfe",
    "Unterstützung besonderer Gruppen",
    "Home Office",
    "Bildung",
    "e-Unterhaltung",
    "Kommunikation",
    "Öffentliche Verwaltung und Gesellschaft",
    "Wirtschaft und Staatliche Unterstützung"
]

def run_insert(client):

    for name in playlist_names:
        client.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": name,
                    "defaultLanguage": "de",
                },
                "status": {"privacyStatus": "unlisted"},
            },
        ).execute()

    return "Done"


def main():
    client = youtube_wrapper.get_authenticated_service()

    response = run_insert(client)

    print(response)


if __name__ == "__main__":
    main()
