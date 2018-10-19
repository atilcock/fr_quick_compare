import face_recognition

known="images/kazan/Kazan.jpg"
known2='./images/kazan/kazan2.jpg'
test1='./images/kazan/kazan_test.jpeg'
test2='./images/kazan/kazan_test2.jpeg'
test3='./images/unknown/not_zoe.jpg'
test4='./images/kazan_2/zoe kazan 2.jpg'
test5='./images/unknown/not_zoe2.jpg'
test6='./images/unknown/not_zoe3.jpg'
tilcock='./images/tilcock/atilcock.jpg'

known_image=face_recognition.load_image_file(known)
known_image2=face_recognition.load_image_file(known2)
test1_image=face_recognition.load_image_file(test1)
test2_image=face_recognition.load_image_file(test2)
test3_image=face_recognition.load_image_file(test3)
test4_image=face_recognition.load_image_file(test4)
tilcock_image=face_recognition.load_image_file(tilcock)
test5_image=face_recognition.load_image_file(test5)
test6_image=face_recognition.load_image_file(test6)

known_encoding=face_recognition.face_encodings(known_image)[0]
known_encoding2=face_recognition.face_encodings(known_image2)[0]

test1_encoding=face_recognition.face_encodings(test1_image)[0]
test2_encoding=face_recognition.face_encodings(test2_image)[0]
test3_encoding=face_recognition.face_encodings(test3_image)[0]
test4_encodingA=face_recognition.face_encodings(test4_image)[0]
test4_encodingB=face_recognition.face_encodings(test4_image)[1]
test5_encoding=face_recognition.face_encodings(test5_image)[0]
test6_encoding=face_recognition.face_encodings(test6_image)[0]
tilcock_encoding=face_recognition.face_encodings(tilcock_image)[0]


# First lets compare the two known faces together

known_encodings = [
    known_encoding
]

face_distances = face_recognition.face_distance(known_encodings,known_encoding2)

for i, face_distance in enumerate(face_distances):
    print("The second known image has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()


known_encodings = [
    known_encoding,
    known_encoding2,
]

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings,test1_encoding)

for i, face_distance in enumerate(face_distances):
    print("The first test image (of zoe kazan wearing glasses) has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings,test2_encoding)

for i, face_distance in enumerate(face_distances):
    print("The second test image (of zoe kazan wearing sunglasses) has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings,test3_encoding)

for i, face_distance in enumerate(face_distances):
    print("The third test image (female but wearing glasses but not kazan ) has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings,test4_encodingA)

for i, face_distance in enumerate(face_distances):
    print("The fourth test image (female with Kazan ) has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()


# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings,test5_encoding)

for i, face_distance in enumerate(face_distances):
    print("The fifth test image (female not Kazan ) has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings,test6_encoding)

for i, face_distance in enumerate(face_distances):
    print("The sixth test image (female not Kazan) has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()

# for fun - lets compare Kazan to your's truly
face_distances = face_recognition.face_distance(known_encodings,tilcock_encoding)

for i, face_distance in enumerate(face_distances):
    print("The  test image of (tilcock - male and definately not kazan )has a distance of {:.2} from known image #{}".format(face_distance, i+1))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()


