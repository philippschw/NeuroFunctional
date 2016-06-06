import os
import os.path
import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request

def download_AVA_images():
# download all AVA images with imageID in download_list.txt

    #get list of imageID
    download_list_file = open('download_list.txt','r')
    lines = download_list_file.read().splitlines()
    download_list_file.close()

    for line in lines:
        imageID = line
        imageFilename = "../trainingset/original/"+imageID+".jpg"
        if not(os.path.isfile(imageFilename)):
            # if file is already exists, skip. otherwise, download it
            # get the image url
            AVA_url = "http://www.dpchallenge.com/image.php?IMAGE_ID="+imageID
            r = requests.get(AVA_url)
            soup = BeautifulSoup(r.text)
            image_container = soup.select("#img_container img")
            image_AVA_url = image_container[1]["src"]
            print("downloading "+image_AVA_url)

            #download and save the image
            f = open(imageFilename, 'wb')
            f.write(request.urlopen(image_AVA_url).read())
            f.close()
    return

download_AVA_images()


