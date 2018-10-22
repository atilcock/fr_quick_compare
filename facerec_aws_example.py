import boto3
import os
import base64

#  this script will demonstrate the ability for AWS Rekognition to identify faces -
#  primarily it will outline the challenge of
#  handling images of the same person with and without glasses
#  and will determine the threshold setting (positive/negative recall) necessary for returning a match.

COLLECTION_NAME=os.getenv('COLLECTION_NAME')
ACCESS_KEY=os.getenv('ACCESS_KEY')
SECRET_KEY=os.getenv('SECRET_KEY')


# create a connection to AWS Rekogntion

client = boto3.client('rekognition',
                           aws_access_key_id=ACCESS_KEY,
                           aws_secret_access_key=SECRET_KEY
                           )

try :
	response = client.delete_collection(
	    CollectionId=COLLECTION_NAME
	)
except :
	print('Unable to delete collection ' + COLLECTION_NAME)

response = client.create_collection(
    CollectionId=COLLECTION_NAME
)

image1="images/kazan/Kazan.jpg"  # head/shoulder pic of Kazan without glasses
image2="images/kazan/Kazan2.jpg"  # head/shoulder pic of Kazan with large round glasses with blue frames
image3="images/kazan/Kazan_test.jpeg"  # full torso pic of Kazan with large round glasses with brown frames
image4="images/kazan/Kazan_test2.jpeg"  # head/shoulder pic of Kazan with large round tinted glasses with blue frames


imageID=""
imageID2=""
imageID3=""
imageID4=""


# load first image of Kazan and put it into a collection
with open('images/kazan/Kazan.jpg','rb') as f:
	known_image = f.read()

	# send to rekognition and add to index
	response = client.index_faces(
		CollectionId=COLLECTION_NAME,
		Image={
			'Bytes': known_image}
		,
		DetectionAttributes=[
			 'ALL'
		],
		MaxFaces=1,
		QualityFilter='AUTO'
	)

	imageID=response['FaceRecords'][0]['Face']['ImageId']

	print (imageID)

f.close()

# load known image2
with open('images/kazan/Kazan2.jpg', 'rb') as f:
	known_image2 = f.read()

	response = client.search_faces_by_image(
		CollectionId=COLLECTION_NAME,
		Image={
			'Bytes': known_image2
		},
		MaxFaces=4
	)

	if (response['FaceMatches']==[]):
		print ("Image 2 face not matched - adding to index")
		response = client.index_faces(
			CollectionId=COLLECTION_NAME,
			Image={
				'Bytes': known_image2}
			,
			DetectionAttributes=[
				'ALL'
			],
			MaxFaces=1,
			QualityFilter='AUTO'
		)

		imageID2 = response['FaceRecords'][0]['Face']['ImageId']

		print(imageID2)

f.close()

# load known image3
with open('images/kazan/Kazan_test.jpeg', 'rb') as f:
	known_image3 = f.read()

	response = client.search_faces_by_image(
		CollectionId=COLLECTION_NAME,
		Image={
			'Bytes': known_image3
		},
		MaxFaces=4
	)

	if (response['FaceMatches']==[]):
		print ("Image 3 face not matched - adding to index")
		response = client.index_faces(
			CollectionId=COLLECTION_NAME,
			Image={
				'Bytes': known_image3}
			,
			DetectionAttributes=[
				'ALL'
			],
			MaxFaces=1,
			QualityFilter='AUTO'
		)

		imageID3 = response['FaceRecords'][0]['Face']['ImageId']

		print(imageID3)
	else:
		matchedID=response['FaceMatches'][0]['Face']['ImageId']
		if (matchedID==imageID):
			print('Image 3 matched image 1 with similarity of ' + str(response['FaceMatches'][0]['Similarity']))
		else:
			print('Image 3 matched image 2 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )

f.close()

# load known image4
with open('images/kazan/Kazan_test2.jpeg', 'rb') as f:
	known_image4 = f.read()

	response = client.search_faces_by_image(
		CollectionId=COLLECTION_NAME,
		Image={
			'Bytes': known_image4
		},
		MaxFaces=4
	)

	if (response['FaceMatches'] == []):
		print("Image 4 face not matched - adding to index")
		response = client.index_faces(
			CollectionId=COLLECTION_NAME,
			Image={
				'Bytes': known_image4}
			,
			DetectionAttributes=[
				'ALL'
			],
			MaxFaces=1,
			QualityFilter='AUTO'
		)

		imageID4 = response['FaceRecords'][0]['Face']['ImageId']

		print(imageID4)

	else:
		matchedID=response['FaceMatches'][0]['Face']['ImageId']
		if (matchedID==imageID):
			print('Image 4 matched image 1 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )
		if (matchedID==imageID2):
			print('Image 4 matched image 2 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )
		if (matchedID==imageID3):
			print('Image 4 matched image 3 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )

f.close()

# at this point we should see a match for all the images with Kazan wearing glasses
# as a final test we take the image with 2 people (one of them being Kazan without glasses) and see if it matches either of the known faces
# load known image4
with open('images/kazan_2/zoe kazan 2.jpg', 'rb') as f:
	known_image5 = f.read()

	response = client.search_faces_by_image(
		CollectionId=COLLECTION_NAME,
		Image={
			'Bytes': known_image5
		},
		MaxFaces=4
	)

	if (response['FaceMatches'] != []):

		matchedID=response['FaceMatches'][0]['Face']['ImageId']
		if (matchedID==imageID):
			print('Image 5 matched image 1 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )
		if (matchedID==imageID2):
			print('Image 5 matched image 2 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )
		if (matchedID==imageID3):
			print('Image 5 matched image 3 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )
		if (matchedID==imageID4):
			print('Image 5 matched image 4 with similarity of ' + str(response['FaceMatches'][0]['Similarity']) )

f.close()


# for a 2nd test - run the compare faces function between the images
# create a function to perform the call

def call_compare_faces(source,target,threshold=90):

	response = client.compare_faces(
		SourceImage={
			'Bytes': source

		},
		TargetImage={
			'Bytes': target
		},
		SimilarityThreshold=threshold
	)

	if (response['FaceMatches']==[]):
		return "Not Matched"
	else:
		return "Matched"

# now loop through using reducing threshold
thresholds=[90,80,70,60]

for threshold in thresholds :
	print ("using threshold " + str(threshold))
	print ("Compare image 1 to image 2 = "  + call_compare_faces(known_image,known_image2,threshold))
	print ("Compare image 1 to image 3 = " + call_compare_faces(known_image,known_image3,threshold))
	print ("Compare image 1 to image 4 = " + call_compare_faces(known_image,known_image4,threshold))
	print ("Compare image 2 to image 3 = " + call_compare_faces(known_image2,known_image3,threshold))
	print ("Compare image 2 to image 4 = " + call_compare_faces(known_image2,known_image4,threshold))
	print ("Compare image 3 to image 4 = " + call_compare_faces(known_image3,known_image4,threshold))

print ("done")