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
print("Stream quality available: ",video.streams)
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

