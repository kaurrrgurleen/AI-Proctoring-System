# Part 1 - Imports, setup, Helper Functions & variables

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from datetime import datetime
import cv2
import mediapipe as mp
import time
import os

# ----------------------------
# Create folders
# ----------------------------
os.makedirs("reports", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

# ----------------------------
# Report File
# ----------------------------
report_name = datetime.now().strftime("reports/report_%d-%m-%Y_%H-%M-%S.txt")
report = open(report_name, "w")
report.write("=" * 50 + "\n")
report.write("        AI PROCTORING SYSTEM REPORT\n")
report.write("=" * 50 + "\n\n")

# ----------------------------
# MediaPipe Face Mesh
# ----------------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=2,
    refine_landmarks=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# ----------------------------
# Webcam
# ----------------------------
cap = cv2.VideoCapture(0)

# ----------------------------
# Timers
# ----------------------------
look_start = None
no_face_start = None

# ----------------------------
# Flags
# ----------------------------
look_logged = False
no_face_logged = False
multiple_logged = False

# ----------------------------
# Counters
# ----------------------------
look_count = 0
no_face_count = 0
multiple_count = 0

# ----------------------------
# Status
# ----------------------------
status = "NORMAL"

# ----------------------------
# Helper Function
# ----------------------------
def log_event(message, frame, filename):
    global look_count
    global no_face_count
    global multiple_count
    current = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    report.write(f"[{current}] {message}\n")
    report.flush()
    
    cv2.imwrite(f"screenshots/{filename}_{datetime.now().strftime('%H-%M-%S')}.jpg",frame)

    if message == "User looked away":
        look_count += 1
    elif message == "No face detected":
        no_face_count += 1
    elif message == "Multiple faces detected":
        multiple_count += 1

# ----------------------------
# Main Loop
# ----------------------------
face_count = 0
while True:
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)
    h, w, _ = frame.shape
    status = "NORMAL"

    # PART 2 – Detection Logic
    # =====================================================
    # NO FACE DETECTED
    # =====================================================

    if not results.multi_face_landmarks:
        status = "WARNING"
        cv2.putText(frame, "No Face Detected", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        if no_face_start is None:
            no_face_start = time.time()
        else:
            elapsed = time.time() - no_face_start
            if elapsed >= 3 and not no_face_logged:
                log_event("No face detected", frame, "no_face")
                no_face_logged = True
        look_start = None
        look_logged = False
        multiple_logged = False
    else:
        no_face_start = None
        no_face_logged = False
        face_count = len(results.multi_face_landmarks)

        # =====================================================
        # FACE COUNT
        # =====================================================

        if face_count > 1:
            status = "WARNING"
            cv2.putText(frame, "Multiple Faces Detected", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            if not multiple_logged:
                log_event("Multiple faces detected", frame, "multiple_faces")
                multiple_logged = True
        else:
            multiple_logged = False
            cv2.putText(frame, "Face Detected", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        # =====================================================
        # DRAW FACE BOX
        # =====================================================

        landmarks = results.multi_face_landmarks[0]
        xs = []
        ys = []
        for point in landmarks.landmark:
            xs.append(int(point.x * w))
            ys.append(int(point.y * h))
        x1 = min(xs)
        y1 = min(ys)
        x2 = max(xs)
        y2 = max(ys)
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

        # =====================================================
        # LOOKING AWAY
        # =====================================================

        nose = landmarks.landmark[1]
        nose_x = int(nose.x * w)
        center = w // 2
        if abs(nose_x - center) > 120:
            status = "WARNING"
            if look_start is None:
                look_start = time.time()
            else:
                elapsed = time.time() - look_start
                if elapsed >= 3 and not look_logged:
                    cv2.putText(frame, "Looking Away!", (20,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    log_event("User looked away", frame, "looking_away")
                    look_logged = True
        else:
            look_start = None
            look_logged = False

    # =====================================================
    # PROJECT TITLE
    # =====================================================

    cv2.putText(frame, "AI PROCTORING SYSTEM", (120,25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

    # =====================================================
    # LIVE TIME
    # =====================================================

    current_time = datetime.now().strftime("%H:%M:%S")
    cv2.putText(frame, current_time, (500,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    # =====================================================
    # STATUS
    # =====================================================

    status_color = (0,255,0)
    if status == "WARNING":
        status_color = (0,0,255)
    cv2.putText(frame, f"Status : {status}", (20,120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

    # =====================================================
    # FACE COUNT
    # =====================================================

    if results.multi_face_landmarks:
        cv2.putText(frame, f"Faces : {face_count}", (20,155), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
    else:
        cv2.putText(frame, "Faces : 0", (20,155), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    # =====================================================
    # VIOLATION COUNTERS
    # =====================================================

    cv2.putText(frame, f"No Face : {no_face_count}", (20,190), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 2)
    cv2.putText(frame, f"Looking Away : {look_count}", (20,225), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 2)
    cv2.putText(frame, f"Multiple Faces : {multiple_count}", (20,260), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 2)

    # =====================================================
    # SHOW WINDOW
    # =====================================================

    cv2.imshow("AI Proctoring System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# =====================================================
# SUMMARY
# =====================================================

report.write("\n")
report.write("=" * 50 + "\n")
report.write("SUMMARY\n")
report.write("=" * 50 + "\n")
report.write(f"Total No Face Violations      : {no_face_count}\n")
report.write(f"Total Looking Away Violations : {look_count}\n")
report.write(f"Total Multiple Face Events    : {multiple_count}\n")

# =====================================================
# CLEANUP
# =====================================================

cap.release()
report.close()
cv2.destroyAllWindows()
