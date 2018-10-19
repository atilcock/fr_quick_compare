import face_recognition
import time
import json
import os.path
import uuid

known = "images/kazan/Kazan.jpg"
known2 = './images/kazan/kazan2.jpg'
tilcock = './images/tilcock/atilcock.jpg'

known_image = face_recognition.load_image_file(known)
known_image2 = face_recognition.load_image_file(known2)
tilcock_image = face_recognition.load_image_file(tilcock)

known_encoding = face_recognition.face_encodings(known_image)[0]
known_encoding2 = face_recognition.face_encodings(known_image2)[0]
tilcock_encoding = face_recognition.face_encodings(tilcock_image)[0]

# First lets compare the two known faces together

known_encodings = [
	known_encoding
]

# load current 'unknown' encodings from file if it exists

current_known_file = "Current/current.json"
current_known_list = []

if (os.path.isfile(current_known_file)):
	with open(current_known_file, 'r') as f:
		current_known_list = json.loads(f)
else:

	# create a default file
	current_known_item = {}
	current_known_item['date'] = time.time()
	current_known_item['id'] = str(uuid.uuid4())
	current_known_item['encoding'] = str(tilcock_encoding)
	current_known_list.append(current_known_item)
	file_output=json.dumps(current_known_list)
	f=open(current_known_file, 'w')
	f.write(json.dumps(current_known_list))

# start camera

# create loop

# capture face/s

# check if face is known
# optional send face to gateway to check if face is known (in list of current known faces) and capture 'start of dwell time'

# if not known create a new UID and update persisted values

# loop until face changes/person leaves

# optionally let the gateway / cloud know when the person has gone. (to flag end of  dwell time).
# send 'person gone' event with last image to the gateway .

