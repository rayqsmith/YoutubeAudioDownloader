# Youtube Audio downloader
# Ray Smith 

import os
import pytube


url = ""
dir = ""
final_location = ""


def getUserInput():

    title = "Youtube Video to Audio"
    title = title.center(len(title))

    print()
    print(title)

    url = input("Enter the video url: ")
    dir = getUserDirectory()
    return(url, dir )
    
    


def getUserDirectory():
    advance = False
    while (not advance):
        dir = input("Enter the save directory: ")
        if (os.path.isdir(dir)):
            return(dir)

        print("Directory is invalid, Try Again", end='\r')
        
    


def videoConversion():
    #get video_name
    video_name = pytube.extract.video_id(url)
    video_savename = video_name +  '.mp4'
    pytube.YouTube(url).streams.filter(only_audio=True).first().download(filename=video_savename)
    source = os.getcwd() + '/' + video_savename
    save_to = dir + '/'+ video_name + '.mp3'
    final_location = save_to
    
    #movie file to destination and save as mp3
    os.system ('mv {0} {1}'.format(source,save_to))
    return final_location


if __name__ == '__main__':
    info = getUserInput()
    url = info[0]
    dir = info[1]

    final_location = videoConversion()
    
    print()
    print( "*" * 50)
    
    print("Video Converted to MP3 and downloaded")
    print("Destination file located at {0}".format(final_location))
    print()
    
    






