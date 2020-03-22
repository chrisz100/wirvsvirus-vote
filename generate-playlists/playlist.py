# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.insert
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
client_secrets_file = os.environ['SECRET']

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


def get_authenticated_service():
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_console()
    youtube = build(api_service_name, api_version, credentials=credentials)
    return youtube


def run_insert(client):

    for name in playlist_names:
        client.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": name,
                    # "description": "Bulk testing.",
                    # "tags": ["sample playlist", "API call"],
                    "defaultLanguage": "de",
                },
                "status": {"privacyStatus": "unlisted"},
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
