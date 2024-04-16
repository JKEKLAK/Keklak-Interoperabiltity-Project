#Jared Keklak INFO 762 Dr.Walters API Project
import googleapiclient
from googleapiclient.discovery import build

#this will query youtube based on a subject string, a API key, and a number of results you can specify.
def get_youtube_videos(subject: str, api_key: str, results: int):

        # API information
        api_service_name = "youtube"
        api_version = "v3"

        # API client
        youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey = API_key)

        # Request body
        request = youtube.search().list(
                part="id,snippet",
                type='video',
                q=subject,
                videoDuration='short',
                videoDefinition='high',
                maxResults= results
        )
        # Request execution
        response = request.execute()
        return response.txt
