
# About
An adaptation of the traditional photobooth, using Natural Language Processing and Computer Vision to extract poetry from 'selfies' and write them out on paper using a 3D printer. 
<p/>In contrast with traditional photobooths, it produces a physical artifact, dynamically writing poetry through generated gcode, expressing an interpretation of what the program 'sees'.
<p/>
<img src="/images/img.png" alt="" />

# To Run application
- pip install requirements.txt.
- run FlaskApp/app.py

## Checklist
1. In the main directory, add open ai GPT3 key in haikuGenerator on line 61. Also add a googleCloudKey.json file with your google cloud api details.
2. Check Cura's usb driver value once printer is plugged in in the <i>monitoring</i> tab.
3. Check Computer's public IPV4 address, ensure that phone app connects to the right address. 
4. Turn on IPCam app from your phone and mount to 3d printer using it as a camera, check local ipv4 address and update it in the app. In your phone browser enter the ipv4address and port 5000 to run from your phone.
5. With the IPCam running in the background (ensure front facing camera is activated), you can take a selfie that will be sent to your computer and processed, then sent to the printer to write.
6. Ensure that there is a pen mounted to the 3d printer (you can use any standard pen mount) and that it makes contact with the build platform when levelled.
