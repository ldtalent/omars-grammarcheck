import os
from turtle import update
import shutil 
import requests
#curDir = os.getcwd()

#print(curDir)
inputDir = 'inputimages/'
outputDir = 'outputimages/'
from os import listdir
api_key = input("Enter API Key:")
for img in os.listdir(inputDir):
    if (img.endswith(".png") or img.endswith(".jpg") or img.endswith(".jpeg")):
        img_path = os.path.join(os.path.realpath(inputDir), img)
        updated_outputDir = os.path.join(os.path.realpath(outputDir), img)
        #shutil.copy(img_path, updated_outputDir)
        dec = input(f"Shall I remove background for file {img} ?")
        if(dec != 'N'):
            print(f"removing {img} background")
            response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(img_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key},
            
            )
            if response.status_code == requests.codes.ok:
                with open(img, 'wb') as out:
                    out.write(response.content)
                shutil.move(img, updated_outputDir)    
            else:
                print("Error:", response.status_code, response.text)
        else:
            print(f"Will not remove {img} background")
print(f"finished looping over all the images")

        #print(img_path)

