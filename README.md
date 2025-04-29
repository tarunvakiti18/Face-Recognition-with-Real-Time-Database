# 👤 Face Recognition with Real-Time Database

This project implements a real-time face recognition system using Python, OpenCV, and Firebase. It captures live video input, detects and recognizes faces, and logs attendance data to a Firebase real-time database. The system is designed for applications like automated attendance tracking and access control.

---

## 🚀 Features

- **Live Face Detection & Recognition** – Uses OpenCV and face_recognition to identify faces via webcam.
- **Firebase Integration** – Attendance and user data are stored in Firebase Realtime Database.
- **Encoding Generator** – Preprocesses known faces for faster recognition.
- **Modular Scripts** – Organized code for managing database, encoding, and main application.

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **face_recognition**
- **Firebase Admin SDK**
- **Firebase Realtime Database**

---

## 📁 Project Structure

Face-Recognition-with-Real-Time-Database/ ├── AddDatatoDatabase.py # Adds user data to Firebase ├── EncodeFile.p # Stored face encodings ├── EncodeGenerator.py # Creates face encodings ├── main.py # Main real-time face recognition script ├── serviceAccountKey.json # Firebase credentials ├── images/ # Directory with user face images └── tempCodeRunnerFile.py # Temp script file

---

## ⚙️ Getting Started

### 1. Clone the Repository
git clone https://github.com/tarunvakiti18/Face-Recognition-with-Real-Time-Database.git
cd Face-Recognition-with-Real-Time-Database
2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
Make sure your requirements.txt includes OpenCV, face_recognition, firebase-admin, etc.

4. Set Up Firebase
Create a Firebase project at Firebase Console

Navigate to Project Settings > Service Accounts

Generate a private key and download serviceAccountKey.json

Place it in your project root directory

🖼️ Add User Images
Organize images as follows:

images/
├── Alice/
│   ├── 1.jpg
│   └── 2.jpg
└── Bob/
    ├── 1.jpg
    └── 2.jpg
Each folder name represents a user, and files are their face images.

🧪 Running the Project
Step 1: Generate Encodings
bash
Copy
Edit
python EncodeGenerator.py
Step 2: Start Real-Time Recognition
python main.py
The webcam will activate, and attendance will be logged into Firebase in real-time.

📌 Notes
Ensure internet connectivity for Firebase.

Use clear, front-facing images for accuracy.

Improve security if deploying this in production.

🤝 Contributing
Feel free to fork and submit pull requests to improve the project.

📄 License
MIT License

📬 Contact
Created by tarunvakiti18


Let me know if you'd like a badge header, project logo, or visual section added to this.


