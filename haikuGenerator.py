import openai
import io
import os
from google.cloud import vision
from google.oauth2 import service_account
import numpy as np
import cv2




def classifyImage():
    googleCredentials = service_account.Credentials.from_service_account_file('/Users/gidirubin/PycharmProjects/3dPrinterPoet/googleCloudKey.json')

    # Instantiates a client
    client = vision.ImageAnnotatorClient(
       credentials=googleCredentials,
    )

    # The name of the image file to annotate
    try:
        file_name = os.path.abspath('drawing.png')
    except:
        file_name = os.path.abspath('drawing.png')


    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations


    print('Labels:')
    labelDescriptions=[]
    prompt = ""
    for label in labels:
        labelDescriptions.append(label.description)
    print(labelDescriptions)

    if len(labelDescriptions)>5:
        labelDescriptions=labelDescriptions[1:4]
    if len(labelDescriptions)==1:
        prompt = labelDescriptions[0]
    else:
        for i in range(len(labelDescriptions)):
            if i<len(labelDescriptions)-1:
                prompt+=labelDescriptions[i]+", "
            else:
                prompt+="and "+labelDescriptions[i]+"."
    print(prompt)
    return prompt

def getConversation(topic):

    prompt="My friend wrote some poems: ''' An old silent pond... A frog jumps into the pond, splash! Silence again. Autumn moonlight- a worm digs silently into the chestnut. In the twilight rain these brilliant-hued hibiscus - A lovely sunset. I want to sleep Swat the flies Softly, please. After killing a spider, how lonely I feel in the cold of night! For love and for hate I swat a fly and offer it to an ant. A mountain village under the piled-up snow the sound of water. Night; and once again, the while I wait for you, cold wind turns into rain. The summer river: although there is a bridge, my horse goes through the water. A lightning flash: between the forest trees I have seen water. ''' I wrote a 20 word poem about "+topic+ ":'''"
    openai.api_key='YOUR_OPEN_API_KEY'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=80,
        top_p=0.7,
        frequency_penalty=0.7,
        presence_penalty=0.6,
        stop=["'''"]
    )
    poem=response['choices'][0]['text']
    print(splitMe(poem))
    return splitMe(poem)


def splitMe(word, n=3):
    simpleList = []
    sentence = word.split()
    if len(sentence)>5:
        if len(sentence) > 21:
            sentence = sentence[0:21]
        splitList = np.array_split(sentence, n)
        for i in range(len(splitList)):
            line = ""
            for j in range(len(splitList[i])):
                line+=splitList[i][j]+" "
            if i==2:
                if ("." in line or "," in line):
                    line=line.split(".")
                    simpleList.append(line)
                else:
                    simpleList.append(line+'...')
            else:
                simpleList.append(line)
    else:
        simpleList.append("I am not feeling creative.")
    return simpleList

def takeSelfie(fileName):
    url = 'https://192.168.1.104:8080/photo.jpg'
    camera = cv2.VideoCapture(url)
    try:
        return_value, image = camera.read()
        cv2.imwrite(fileName, image)
    except:
        print('couldnt process selfie')