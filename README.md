# 🛡️ AI Proctoring System

An AI-powered proctoring system developed using **Python, OpenCV, and MediaPipe** to monitor candidates during online examinations. The application uses a webcam to detect faces in real time and identifies suspicious activities such as the absence of a face, multiple faces, and looking away from the screen. It also records these events in a report with timestamps for future reference.

---

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20Detection-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)


## 📌 Project Overview

Online examinations require an effective way to monitor candidates and maintain exam integrity. This project provides a simple AI-based proctoring solution that continuously analyzes webcam input and detects common violations.

Whenever a violation is detected, the system:

- Displays a warning on the screen
- Saves the event in a report file
- Captures a screenshot of the violation
- Maintains a summary of all detected violations

---

## ✨ Features

- ✅ Real-time Face Detection
- ✅ No Face Detection
- ✅ Multiple Face Detection
- ✅ Looking Away Detection
- ✅ Live Webcam Monitoring
- ✅ Face Bounding Box
- ✅ Live Status Display
- ✅ Face Counter
- ✅ Violation Counters
- ✅ Automatic Screenshot Capture
- ✅ Timestamped Report Generation
- ✅ Session Summary Report
- ✅ User-friendly Interface

---

## 🛠️ Technologies Used

- Python 3.12.2
- OpenCV
- MediaPipe
- DateTime
- Time
- OS Module

---

## 📂 Project Structure

```
AI-Proctoring-System/
│
├── proctor.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── screenshots/
│   ├── face_detected.png
│   ├── no_face.png
│   ├── multiple_faces.png
│   ├── looking_away.png
│
├── reports/
│   └── report_13-07-2026_18-40-25.txt
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/kaurrrgurleen/AI-Proctoring-System.git
```

### Move into the project directory

```bash
cd AI-Proctoring-System
```

### Install the required libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the following command:

```bash
python proctor.py
```

Press **Q** to close the application.

---

## 📸 Project Screenshots

### Face Detected

<img width="625" height="508" alt="Screenshot 1" src="https://github.com/user-attachments/assets/01836939-25c3-4249-aad1-f7a20d146397" />

---

### No Face Detected

<img width="640" height="480" alt="no_face_19-21-15" src="https://github.com/user-attachments/assets/57d10114-ca72-46a6-a587-7837809f75c6" />


---

### Multiple Faces Detected

<img width="640" height="480" alt="looking_away_19-28-05" src="https://github.com/user-attachments/assets/a67626c6-8b91-4daa-977f-dc6e6d6cd2db" />


---

### Looking Away Detection

<img width="640" height="480" alt="looking_away_19-27-38" src="https://github.com/user-attachments/assets/096f72aa-97b3-4555-9369-499e554c4723" />


---

### Report File

<img width="467" height="362" alt="image" src="https://github.com/user-attachments/assets/10805e84-bcb4-4a86-a0cc-e0785132d625" />

---

## 📊 Output

The system automatically generates:

- Timestamped report files
- Screenshots for every detected violation
- Summary of violations after the session ends

Example:

```
==================================================
AI PROCTORING SYSTEM REPORT
==================================================

Session Started : 13-07-2026 18:42:05

[13-07-2026 18:43:12] No face detected
[13-07-2026 18:44:08] User looked away
[13-07-2026 18:45:31] Multiple faces detected

==================================================
SUMMARY
==================================================
Total No Face Violations      : 1
Total Looking Away Violations : 2
Total Multiple Face Events    : 1

Session Ended : 13-07-2026 18:47:10
```

---

---

# 📈 Results

The AI Proctoring System was successfully implemented and tested using a live webcam. The application was able to monitor the user's activity in real time and accurately identify different scenarios during testing.

### Test Results

| Feature | Result |
|---------|--------|
| Face Detection | ✅ Successfully detected a single face |
| No Face Detection | ✅ Detected when the user left the camera view for more than 3 seconds |
| Multiple Face Detection | ✅ Successfully detected more than one face in the frame |
| Looking Away Detection | ✅ Identified when the user looked away from the screen for more than 3 seconds |
| Event Logging | ✅ All violations were recorded with timestamps in the report file |
| Screenshot Capture | ✅ Screenshots were automatically saved whenever a violation occurred |
| Summary Generation | ✅ Total number of violations was displayed at the end of the session |

### Overall Outcome

The project successfully demonstrates how Computer Vision techniques can be used to build a simple AI-based online proctoring system. It performs real-time monitoring of webcam input and detects common examination violations while maintaining a detailed log of events. The system is lightweight, easy to use, and serves as a good foundation for more advanced online examination monitoring applications.

---
## 🚀 Future Enhancements

- Eye Gaze Tracking
- Mobile Phone Detection
- Head Pose Estimation
- Face Recognition for Candidate Verification
- Audio Activity Monitoring
- Email Alerts for Violations
- Automatic Exam Report Generation
- Web-Based Dashboard

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Computer Vision using OpenCV
- Face Detection using MediaPipe
- Real-time Webcam Processing
- File Handling in Python
- Event Logging
- AI-based Monitoring Systems
- Git & GitHub Project Management

---

## 👨‍💻 Author

**Gurleen Kaur**

If you found this project useful, feel free to ⭐ the repository.

---

## 📜 License

This project is developed for educational and learning purposes.
