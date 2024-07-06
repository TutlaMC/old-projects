import face_recognition as fr
import os
import shutil
import cv2
import face_recognition
import numpy as np
from time import sleep

from numpy.core.numeric import ascontiguousarray


def get_encoded_faces():

    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

def unknown_image_encoded(img):

    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):

    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    img = cv2.resize(img, (0, 0), fx=1, fy=1)
    #img = img[:,:,::-1]
 
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:

        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unkown"


        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
        b = face_names[0]
        a = face_distances[0]
        print(face_distances)
        if a < 0.7:
            ask = input(f'Is the face {b} y/n: ')
            if ask == 'y':
                print(b)
            else:
                global ans
                ans = input('who is it? (Full name reccomended): ')
                global nnn
                nnn = 0
                def fcheck(num):
                    global ans
                    if os.path.exists(f'faces/{ans}{num}'):
                        return True
                        
                
                def frun():
                    global nnn
                    global ans
                    if fcheck(nnn):
                        nnn +=1
                        if fcheck(nnn):
                            frun()
                        shutil.copy('test.jpeg','hash.jpg')
                        os.rename('hash.jpg','C:\\Users\\ayaan\\Desktop\\Tutla\\PythonProjects\\face_rec\\faces\\hash.jpg')
                        os.rename('faces/hash.jpg',f'faces/{ans} ({nnn}).jpg')
                    else:
                        shutil.copy('test.jpeg','hash.jpg')
                        os.rename('hash.jpg','C:\\Users\\ayaan\\Desktop\\Tutla\\PythonProjects\\face_rec\\faces\\hash.jpg')
                        os.rename('faces/hash.jpg',f'faces/{ans}.jpg')
                    classify_face()
                frun()

        
        for (top, right, bottom, left), name in zip(face_locations, face_names):

            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)


            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


    while True:

        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names 


print(classify_face("test.jpeg"))