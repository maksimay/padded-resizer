from PIL import Image, ImageOps
import cv2
import glob
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-src", "--source", default="test", help="")
parser.add_argument("-des", "--destination", default="newwww", help="")
parser.add_argument("-d", "--dimensions", default=512, help="")
args = parser.parse_args()

desired_size = int(args.dimensions)
inputFolder = str(args.source)
output_folder = str(args.destination)
counter = 0
i = 0


print("loading images from..." + str(inputFolder))

os.mkdir(output_folder)
print("created directory:"+ " " + str(output_folder)) 



for img in glob.glob(inputFolder + "/*.jpg"):
    try:
        counter +=1
        im = cv2.imread(img)
        old_size = im.shape[:2] # old_size is in (height, width) format
        ratio = float(desired_size)/max(old_size)
        new_size = tuple([int(x*ratio) for x in old_size])
        img_count = str(counter).zfill(4)

       # new_size 
        im = cv2.resize(im, (new_size[1], new_size[0])) 

        delta_w = desired_size - new_size[1]
        delta_h = desired_size - new_size[0]
        top, bottom = delta_h//2, delta_h-(delta_h//2)
        left, right = delta_w//2, delta_w-(delta_w//2)

        color = [255, 255, 255]
        new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)

        cv2.imwrite(str(output_folder) + "/" + "resized" + "_" + str(desired_size) +"_" + "%04i.jpg" %i, new_im)
        i+=1
        print("resizing images in progress... ")
        print(str(img_count))
    except:
        print('ERROR: File no. ' + str(counter) + 'could not be resized due to an unknown ERROR, we are SORRY :(' )
    
print("Resizing succesfully completed!!")
        
cv2.waitKey(0)
cv2.destroyAllWindows()