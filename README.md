# 🎓 Face Recognition Attendance System

This project is a real-time face recognition-based attendance system built using Python, OpenCV, and the `face_recognition` library. It captures faces through a webcam, identifies known individuals, and logs their attendance (name and time) into a CSV file named with the current date.

---

## 📸 Features

* Real-time webcam-based face detection
* Automatic recognition of registered faces
* Attendance recording with timestamp
* CSV log generation for each day
* Easy scalability by adding new face images

---

## 🛠️ Tech Stack

* Python
* OpenCV
* face\_recognition (Dlib-based library)
* NumPy
* CSV Module
* Flask (Imported but not used in this version)

---

## 📁 Folder Structure

```
project-folder/
│
├── faces/
│   ├── jay.jpg
│   ├── khushi.jpg
│   ├── virat.jpeg
│   ├── jef.jpeg
│   ├── prince.jpg
│   └── ary.jpg
│
├── main.py  <-- (This script)
└── [DD-MM-YYYY].csv (generated daily)
```

---

## 🚀 How It Works

1. **Initialization**:

   * The webcam starts capturing frames.
   * Known face images are loaded and encoded into numerical data.

2. **Real-Time Face Detection**:

   * Each frame is resized and converted to RGB.
   * Face locations and encodings are extracted.

3. **Recognition & Attendance**:

   * For every detected face, the script compares it with the known faces.
   * If a match is found:

     * The name is displayed on the screen.
     * The name and timestamp are logged into a CSV file.
     * The student is removed from the list to avoid multiple entries.

4. **Exit**:

   * Press `q` to quit and save the attendance file.

---

## ✅ How to Use

1. Install Dependencies:

```bash
pip install face_recognition opencv-python numpy
```

2. Add Known Faces:

   * Place clear face images inside the `faces/` folder.
   * Update the Python script to load and encode these new faces.

3. **Run the Script**:

```bash
python main.py
```

4. **Quit**:

   * Press `q` to stop the camera and generate the CSV log file.

---

## 📄 Output

The attendance is saved as:

```csv
jay, 09:30:01
khushi, 09:32:15
...
```

Saved as: `18-06-2025.csv` (based on current date)

---

## ⚠️ Notes

* Make sure lighting is good for better accuracy.
* Add high-quality front-facing images for better face recognition.
* Currently, Flask is imported but not used – could be extended for a web-based interface in future.

---

## 📌 Future Improvements

* Add GUI using Tkinter or web dashboard using Flask/Django
* Add unknown face alerts
* Store attendance data in a database
* Email notification or daily report

---

## 👨‍💻 Author

**Jayveer Solanki**


