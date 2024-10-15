from googleapiclient.discovery import build
import random
# YouTube API anahtarınızı buraya ekleyin
api_key = ''
#Aranacak Kelime
word = ''

youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    )
    while request:
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            if word in comment:
                comments.append((author,comment))
        request = youtube.commentThreads().list_next(request, response)

    return comments

# Video ID'sini buraya ekleyin
video_id = ''

# Yorumları al
video_comments = get_video_comments(video_id)


# for author, comment in video_comments:
#      print(f"Kullanıcı: {author} - Yorum: {comment}")

# i=1
# for yorum in video_comments:
#     print(f"{i}.{yorum}\n")
#     i= i+1
katilimci_Sayisi= len(video_comments)
random_comment = random.choice(video_comments)
kazanan_kullanici = random_comment[0]
print(f"Katilimci Sayisi: {katilimci_Sayisi}\n")
print(f"Kazanan: {kazanan_kullanici}")

