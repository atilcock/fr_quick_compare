import requests
import json
import base64
from os.path import expanduser

#  this script will demonstrate the ability for Azure face API to identify faces -
#  primarily it will outline the challenge of
#  handling images of the same person with and without glasses
#  and will determine the threshold setting (positive/negative recall) necessary for returning a match.


# NOTE the Azure implementation provides the ability to create face groups with multiple images of the same person
# which will enable increasingly better recall values.   This service essentially performs a machine training/learning
# process on the group of individuals based on the provided labels.   This service would be appropriate for the type
# of scenario that is being tested in this repo however for the purposes of consistency it is not being implemented
# and this repo will focus on comparing the image comparison capabilities of Azure relative to the open source
# and other cloud (AWS/Google) implementations

# required Azure FACE API key

subscription_key = "50392a16c9884f71bbe54b9fa1e1f8cf"
assert subscription_key
# required - region based url
face_api_url = 'https://westus2.api.cognitive.microsoft.com/face/v1.0/'

# implement face verify to compare one image to another and determine if it is the same person

image1="./images/kazan/Kazan.jpg"  # head/shoulder pic of Kazan without glasses
image2="images/kazan/Kazan2.jpg"  # head/shoulder pic of Kazan with large round glasses with blue frames
image3="images/kazan/Kazan_test.jpeg"  # full torso pic of Kazan with large round glasses with brown frames
image4="images/kazan/Kazan_test2.jpeg"  # head/shoulder pic of Kazan with large round tinted glasses with blue frames

headers_octet = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type':'application/octet-stream'}
headers_json = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type':'application/json'}

params_identify = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}

# Set image_url to the URL of an image that you want to analyze.

image = open(image1, 'rb')
response = requests.post(face_api_url+'detect', data=image, headers=headers_octet,params=params_identify)
faces = response.json()
image1id=faces[0]['faceId']

image = open(image2, 'rb')
response = requests.post(face_api_url+'detect', data=image, headers=headers_octet,params=params_identify)
faces = response.json()
image2id=faces[0]['faceId']

image = open(image3, 'rb')
response = requests.post(face_api_url+'detect', data=image, headers=headers_octet,params=params_identify)
faces = response.json()
image3id=faces[0]['faceId']

image = open(image4, 'rb')
response = requests.post(face_api_url+'detect', data=image, headers=headers_octet,params=params_identify)
faces = response.json()
image4id=faces[0]['faceId']

# now compare the images

body={
    "faceId1": image1id,
    "faceId2": image2id
}

response = requests.post(face_api_url+'verify', json=body, headers=headers_json,params="")
verify = response.json()

print ("Comparing image1 to image2 returned a confidence of  " + str(verify['confidence']) + ' that they are the same person')

body={
    "faceId1": image1id,
    "faceId2": image3id
}

response = requests.post(face_api_url+'verify', json=body, headers=headers_json,params="")
verify = response.json()

print ("Comparing image1 to image3 returned a confidence of  " + str(verify['confidence']) + ' that they are the same person')

body={
    "faceId1": image1id,
    "faceId2": image4id
}

response = requests.post(face_api_url+'verify', json=body, headers=headers_json,params="")
verify = response.json()

print ("Comparing image1 to image4 returned a confidence of  " + str(verify['confidence']) + ' that they are the same person')


body={
    "faceId1": image2id,
    "faceId2": image3id
}

response = requests.post(face_api_url+'verify', json=body, headers=headers_json,params="")
verify = response.json()

print ("Comparing image2 to image3 returned a confidence of  " + str(verify['confidence']) + ' that they are the same person')

body={
    "faceId1": image2id,
    "faceId2": image4id
}

response = requests.post(face_api_url+'verify', json=body, headers=headers_json,params="")
verify = response.json()

print ("Comparing image2 to image4 returned a confidence of  " + str(verify['confidence']) + ' that they are the same person')


body={
    "faceId1": image3id,
    "faceId2": image4id
}

response = requests.post(face_api_url+'verify', json=body, headers=headers_json,params="")
verify = response.json()

print ("Comparing image3 to image4 returned a confidence of  " + str(verify['confidence']) + ' that they are the same person')

