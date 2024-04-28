#Jared Keklak INFO 762 Dr.Walters API Project
import googleapiclient
from googleapiclient.discovery import build

import INFOproj_GLOBALS as G

#this will query youtube based on a subject string, a API key, and a number of results you can specify.
def get_youtube_videos(subject: str):
        api_service_name = "youtube"
        api_version = "v3"

        # API client
        youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey=G.API_KEY_Youtube)

        # Request body
        request = youtube.search().list(
                part="snippet",
                type='video',
                q=subject,
                videoDuration='short',
                videoDefinition='high',
                maxResults=1
        )
        # Request execution, returns a dictionary of results
        response = request.execute()
        results_list = response['items']

        video_Ids = []
        for r in results_list:
                video_Ids.append(r['id']['videoId'])

        return "https://www.youtube.com/watch?v=" + video_Ids[0]

def get_youtube_videos_test():
        print("get youtube videos was triggered")


#video = get_youtube_videos("Siamese Cat", G.API_KEY_Youtube)
#print(video)