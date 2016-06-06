import os
import glob
from PIL import Image

target_WIDTH = 300;
target_HEIGHT = 225;
target_ratio = target_WIDTH/target_HEIGHT;

def preprocess_AVA():
    file_list = glob.glob("../trainingset/original/*.jpg")
    for filename in file_list:
        with Image.open(filename) as im:
            width, height = im.size
            WH_ratio = width/height

            #resize and crop to target_WIDTH x target_HEIGHT
            if (WH_ratio > target_ratio):
                new_width = int(WH_ratio*target_HEIGHT)
                im = im.resize((new_width,target_HEIGHT),Image.ANTIALIAS)
                margin_width = int((new_width-target_WIDTH)/2)
                im = im.crop((margin_width,0,margin_width + target_WIDTH,target_HEIGHT))
            else:
                new_height = int(target_WIDTH/WH_ratio)
                im = im.resize((target_WIDTH,new_height),Image.ANTIALIAS)
                margin_height = int((new_height-target_HEIGHT)/2)
                im = im.crop((0,margin_height, target_WIDTH, margin_height + target_HEIGHT))
            W,H = im.size
            #print(width,height,W,H)

            #save the preprocessed image
            parts = filename.split("\\")
            new_filename = "../trainingset/preprocesed/"+parts[1]
            im.save(new_filename)

    return

preprocess_AVA()