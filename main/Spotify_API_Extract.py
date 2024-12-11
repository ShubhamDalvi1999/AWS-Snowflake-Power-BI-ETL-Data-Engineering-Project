import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime


def lambda_handler(event, context):
    # Retrieve Spotify credentials from environment variables
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    # Initialize Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Define the Spotify playlist URI
    playlist_link = "https://open.spotify.com/playlist/2a4YYkZa1c4ah4KFSGw5u5"
    playlist_URI = playlist_link.split("/")[-1]  # Extract URI
    
    # Fetch playlist data
    spotify_data = sp.playlist_tracks(playlist_URI)
    
    # Initialize S3 client
    s3_client = boto3.client('s3')

    filename = "spotify_raw_"+str(datetime.now())+".json"

    # Upload data to S3
    s3_client.put_object(
        Bucket="spotify-aws-etl-project-190",  # Replace with your bucket name
        Key="raw_data/to_process_data/"+ filename ,
        Body=json.dumps(spotify_data)
    )
    
    return {
        'body': json.dumps('Data uploaded successfully!')
    }
