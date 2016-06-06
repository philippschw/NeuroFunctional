import os
import glob
from PIL import Image

def summarize_AVA():
# summarize the info of each AVA images to DATASET_SUMMARY.txt
# format:  imageID;width;length;class (1=beautiful, 0=not beautiful)

    summary_file = open('DATASET_SUMMARY.txt','w')

    rating_map = get_ratings()
    file_list = glob.glob("../trainingset/original/*.jpg")
    for filename in file_list:
        parts = filename.split("\\")
        im_name = parts[1].split(".")
        imageID = im_name[0]

        if(imageID in rating_map):
            ratings = rating_map[imageID]
            cls = compute_class(ratings)
            with Image.open(filename) as im:
                width, height = im.size
                record = imageID+";"+str(width)+";"+str(height)+";"+str(cls)
                print(record)
                summary_file.write(record+"\n")
    return

def get_ratings():
# get the rating informations of each imageID
    ratings = {}
    AVA_file = open('AVA.txt', 'r')
    lines = AVA_file.read().splitlines()
    AVA_file.close()

    for line in lines:
        fields = line.split(' ')
        imageID = fields[1]
        # print(imageID)
        ratings[imageID] = [int(i) for i in fields[2:12]]
    return ratings

def compute_class(ratings):
# determine the class based on the rating
    pos = sum(ratings[5:11])
    neg = sum(ratings[0:5])

    if(pos > neg):
        # image is beautiful if positive ratings > negative ratings
        return 1
    else:
        return 0

summarize_AVA()