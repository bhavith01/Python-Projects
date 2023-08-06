from dotenv import load_dotenv
import os,base64,json,re,psutil
import pytube as pt
from requests import post,get
import requests
from pathlib import Path
from youtubesearchpython import VideosSearch
#########################################33333333

song_list=''

load_dotenv()

image_arr=[]
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8") 
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"

    header = {

        "Authorization": "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"

    }

    data ={ "grant_type": "client_credentials"}
    result = post(url, headers=header, data=data)
    json_result = json.loads(result. content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization":"Bearer " + token}


#####################################################################3

def extract_playlist_id(playlist_link):
    pattern = r"playlist\/(\w+)"
    match = re.search(pattern, playlist_link)

    if match:
        return match.group(1)
    




def get_song_list(token,playlist):
    
    playlist_id=extract_playlist_id(playlist)

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers=get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)
    song_list=json_result["items"]
    #print(song_list)
    
    max =0
    for idx, song in enumerate(song_list):
        track_name = song['track']['name']
        if(len(track_name)>max):
            max = len(track_name)+10

    
    for idx, song in enumerate(song_list):
        track_name = song['track']['name']
        artist_name = song['track']['artists'][0]['name']
        no_of_artist = len(song['track']['artists'])
        image_png = song['track']['album']['images'][0]['url']
        print(image_png)
        image_arr_temp=requests.get(image_png).content
        image_arr.append(image_arr_temp)
        path2=f"image{idx}.jpg"
        print(path2)
        f=open(path2,'wb')
        # f = open(path2,'wb')
        f.write(image_arr[idx-1])
        

        
       

        space = max-len(track_name)

       # app.write(f"{idx+1}. {track_name}")
        app.write(f"{track_name}")
        #app.write(" "*space)
        app.write(" By ")
        for i in song['track']['artists']:
            app.write(f"{i['name']}")
        app.write("\n")
         

    

app=open('resulted list.txt','w')




token = get_token()
get_song_list(token,"https://open.spotify.com/playlist/37i9dQZF1EQntZpEGgfBif?si=e7111499615b495c")
app.close()


# rFile = open('resulted list.txt',"r")

# rFileLines = rFile.readlines()
# os.chdir('C:/Users/bhavi/Music/soul')

# for line in rFileLines:
#     fris = VideosSearch(line,limit = 1)
#     obj=fris.result()
#     linkkk=obj["result"][0]["link"]
#     print(obj["result"][0]["link"])
#     yt = pt.YouTube(linkkk)
#     audio_stream = yt.streams.filter(only_audio=True).first()

#     download_folder = "C:/Users/bhavi/Music/soul"  
#     if not os.path.exists(download_folder):
#         os.makedirs(download_folder)
        
#     downloaded_file_path = audio_stream.download()
#     new_file_path = os.path.join(download_folder, audio_stream.default_filename)
    

    
    


    



    




#get_song_list(token,input())


##########################################33 
#youtube download












# dir_path = Path(os.path.join(downloaded_file_path, os.pardir))
# print(dir_path)

# for text_file in dir_path.glob("*.mp4"):
#     try:
#         new_file_path = text_file.rename(text_file.with_suffix(".mp3"))
#     except FileExistsError:
#         print(f"Error: '{text_file.with_suffix('.mp3').name}' already exists.")
    