import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials, db, storage

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-real-ti-fc173-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-real-ti-fc173.appspot.com"
})

# Function to upload image to Firebase Storage
def upload_image_to_firebase(file_path, bucket):
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)

# Function to find encodings for a list of images
def find_encodings(images_list):
    encode_list = []
    for img in images_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encode_list.append(encodings[0])
        else:
            print("No face found in image.")
    return encode_list

# Load images and student IDs
folder_path = 'Images'
path_list = os.listdir(folder_path)
print(path_list)

img_list = []
student_ids = []
bucket = storage.bucket()

for path in path_list:
    img = cv2.imread(os.path.join(folder_path, path))
    if img is not None:
        img_list.append(img)
        student_ids.append(os.path.splitext(path)[0])
        file_name = f'{folder_path}/{path}'
        upload_image_to_firebase(file_name, bucket)
    else:
        print(f"Failed to load image: {path}")

print(student_ids)

# Find encodings for loaded images
print("Encoding Started ...")
encode_list_known = find_encodings(img_list)
encode_list_known_with_ids = [encode_list_known, student_ids]
print("Encoding Complete")

# Save encodings to a file
with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encode_list_known_with_ids, file)

print("File Saved")
