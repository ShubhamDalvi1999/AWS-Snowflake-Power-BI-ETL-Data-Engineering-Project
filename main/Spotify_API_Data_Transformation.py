import json
import boto3
import pprint
from datetime import datetime
import pandas as pd
from io import StringIO
import helper_check

def album(data):
    album_list = []
    for row in data['items']:
        album_id = row['track']['album']['id' ]
        album_name = row['track']['album']['name']
        album_release_date = row['track']['album']['release_date']
        album_total_tracks = row['track']['album' ]['total_tracks']
        album_url = row['track']['album']['external_urls']['spotify']
        album_element = {'album_id':album_id, 'name':album_name, 'release date':album_release_date,
                        'total_tracks': album_total_tracks, 'url':album_url}
        album_list.append(album_element)
    return album_list

def artist(data):
    artist_list=[]
    for row in data['items']:
        for key,value in row.items():
            if key == "track":
                for artist in value['artists']:
                    artist_dict = {'artist_id':artist['id'],
                                'artist_name':artist['name'],
                                'external_url':artist['href']}
                    artist_list.append(artist_dict)
    return artist_list

def songs(data):
    song_list = []

    for row in data['items']:
        song_id = row['track']['id']
        song_name = row['track' ]['name']
        song_duration= row['track']['duration_ms']
        song_url = row['track']['external_urls']['spotify']
        song_popularity = row['track']['popularity']
        song_added = row['added_at']     
        album_id = row['track']['album']['id']
        artist_id = row['track']['album']['artists'][0]['id']
        song_element = { 'song_id':song_id,
                        'song_name': song_name,
                        'duration_ms':song_duration, 
                        'url': song_url,
                        'popularity' : song_popularity, 
                        'song_added': song_added,
                        'album_id':album_id,
                        'artist_id':artist_id
                    }
        song_list.append(song_element)

    return song_list

def lambda_handler(event, context):
    
    # result = helper_check.check_function()
    # getting the files to transform 
    s3 = boto3.client("s3")
    Bucket = "spotify-aws-etl-project-190"
    Key = "raw_data/to_process_data/"

    spotify_data = []
    spotify_keys = []
    for file in s3.list_objects(Bucket = Bucket, Prefix = Key)['Contents']:
        file_key = file['Key']  # gets the file name from the s3 list of objects
        
        # only processing the json files
        if file_key.split('.')[-1] == "json":
            response = s3.get_object(Bucket = Bucket, Key = file_key)
            content = response['Body']
            jsonObject = json.loads(content.read())
            #storing the data from each file and its file name for future use
            spotify_data.append(jsonObject)
            spotify_keys.append(file_key)

    # "Transform" data from each file and store it in different file in transformed bucket 
    for data in spotify_data:
        album_list = album(data)
        artist_list = artist(data)
        song_list = songs(data)

        #Album Dataframe
        album_df = pd.DataFrame.from_dict(album_list)
        album_df = album_df.drop_duplicates( subset =['album_id'])

        #Artist Dataframe
        artist_df = pd.DataFrame.from_dict(artist_list)
        artist_df = artist_df.drop_duplicates( subset =['artist_id'])

        #Song Dataframe
        song_df = pd.DataFrame.from_dict(song_list)

        #Transformations
        song_df['song_added'] = pd.to_datetime(song_df['song_added'],errors='coerce') 
        album_df['release date'] = pd.to_datetime(album_df['release date'],errors='coerce')

        #Storing the transformed song df in transformed bucket
        song_key = "transformed_data/s_song/song_transformed_"+str(datetime.now())+".csv"
        song_buffer = StringIO()
        song_df.to_csv(song_buffer, index= False)
        song_content = song_buffer.getvalue()
        s3.put_object(Bucket = Bucket, Key = song_key , Body= song_content)

        #Storing the transformed album df in transformed bucket
        album_key = "transformed_data/s_album/album_transformed_"+str(datetime.now())+".csv"
        album_buffer = StringIO()
        album_df.to_csv(album_buffer, index= False)
        album_content = album_buffer.getvalue()
        s3.put_object(Bucket = Bucket, Key = album_key , Body= album_content)

        #Storing the transformed artist df in transformed bucket
        artist_key = "transformed_data/s_artist/artist_transformed_"+str(datetime.now())+".csv"
        artist_buffer = StringIO()
        artist_df.to_csv(artist_buffer,index= False)
        artist_content = artist_buffer.getvalue()
        s3.put_object(Bucket = Bucket, Key = artist_key , Body= artist_content)

    # Moving files from the "processing bucket" to the "processed bucket"
    s3_resource = boto3.resource("s3")
    
    for key in spotify_keys:
        copy_source = {
            'Bucket': Bucket,
            'Key': key
        }
        
        # Copy the object to the new location
        new_key = 'raw_data/processed_raw_data/' + key.split("/")[-1]
        s3_resource.Bucket(Bucket).copy(copy_source, new_key)
        
        # Delete the original object
        s3_resource.Object(Bucket, key).delete()

    #returning the acknowledgement of correctly runing the data
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
