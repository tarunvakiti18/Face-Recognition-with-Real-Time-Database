import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-real-ti-fc173-default-rtdb.firebaseio.com/"
    
})

ref = db.reference('Students')

data = {
        "245320733113":
        {
            "name": "Tarun Vakiti",
            "major": "Cse",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-05-21 00:54:34"

        },
        "245320733115":
        {
            "name": "Karthik Varanasi",
            "major": "Cse",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-05-21 00:54:34"
        },"245320733106":
        {
            "name": "Shivtej",
            "major": "Cse",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-05-21 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)