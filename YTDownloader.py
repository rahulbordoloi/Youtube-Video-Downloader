import os
import time
from pytube import YouTube

# url = 'https://youtu.be/xl8zdCY-abw' # Narcos-Trailer
# url = 'https://www.youtube.com/watch?v=cq2iTHoLrt0' # Dark S3 Trailer

print("Enter the Youtube URL of the Video you want to Download : ")
url = input()
youtube = YouTube(url)

print('-----------------------------------')

# Information of the Video of the Given URL
print('Title : ', youtube.title)
print('Views : ', youtube.views)
print('Length : ' , youtube.length, 'seconds')
print('Description : ', youtube.description)
print('Rating : ', youtube.rating) 

print('-----------------------------------')

'''
# Streams
streams = youtube.streams.all()
for i in streams:
    print(i)
'''

# print(youtube.streams)

# Print the Audio Streams
# print(youtube.streams.filter(only_audio = True))

# Print the Video Streams
# print(youtube.streams.filter(only_video = True))

'''
YouTube uses Dash streams for higher-quality rendering.
Progressive streams are limited to 720p and it contains both audio and video codec files while Dash streams 
have higher quality but only have video codecs.
Here, I've used Progressive Streams Only
'''

# Get all the Progressive Streams
# print(youtube.streams.filter(progressive = True))

'''
# Choose any Stream by the help of its itag.
ystream = youtube.streams.get_by_itag('22')
'''

# Get the Highest Quality Progressive Stream
ystream = youtube.streams.get_highest_resolution()

# Downloading the File
print('Starting Download ...')
start = time.time()
ystream.download()  # download()
end = time.time()
print('Download Successful, You can find your File at :', os.getcwd())
print('Time Elapsed : ', round(end - start , 2), 'seconds')
