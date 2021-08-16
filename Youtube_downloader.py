from pytube import YouTube
import time


link_of_video = input("Please Enter the link of video you wish to download:  ")
video = YouTube(link_of_video)

print("Some Information About The Video")
print("********************************************************")
print("Title: ",video.title)
print("********************************************************")
print("Views: ",video.views)
print("********************************************************")
print("Length of Video: ",video.length)
print("********************************************************")
print("Video Rating: ",video.rating)
print("********************************************************")
print("Captions available: ",video.captions)
print("********************************************************")
print("Please enter a string for the type of stream you want.")
sq = input("Stream available: 'prog' progressive streams, 'adap' adaptive stream, 'audo' audio only streams. 'mp4s' MP4 stream: ")
if (sq == 'prog'):
    print(video.streams.filter(progressive=True))
elif (sq == 'adap'):
    print(video.streams.filter(adaptive=True))
elif (sq == 'audo'):
    print(video.streams.filter(only_audio=True))
else:
    print(video.streams.filter(file_extension='mp4'))
print("********************************************************")
print("If you wish to download the stream with highest resolution type h")
want = input("OR Please Enter the itag of the stream you wish to be downloaded:   ")

if (want == 'h'):
    get_high_res = video.streams.get_highest_resolution()
else:
    get_high_res = video.streams.get_by_itag(want)


print("********************************************************")
print("Downloading...    !Please Wait!")
start = time.time()
get_high_res.download()
end = time.time()
print("Time it took to download:  ",end - start," seconds.")
print("Download completed!!")

