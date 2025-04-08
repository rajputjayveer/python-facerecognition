# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# import cv2
# import face_recognition
# import numpy as np
# import base64

# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Load known faces
# known_face_encodings = []
# known_face_names = []

# face_data = {
#     "jay": "faces/jay.jpg",
#     "khushi": "faces/khushi.jpg",
#     "virat": "faces/virat.jpeg",
#     "jef": "faces/jef.jpeg",
#     "prince": "faces/prince.jpg"
# }

# for name, file in face_data.items():
#     image = face_recognition.load_image_file(file)
#     encoding = face_recognition.face_encodings(image)[0]
#     known_face_encodings.append(encoding)
#     known_face_names.append(name)

# # Process video frames from frontend
# @socketio.on('video_frame')
# def handle_video_frame(data):
#     image_data = base64.b64decode(data.split(',')[1])
#     npimg = np.frombuffer(image_data, np.uint8)
#     frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     detected_names = []
#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         best_match_index = np.argmin(face_distances)

#         if matches[best_match_index]:
#             name = known_face_names[best_match_index]
#             detected_names.append(name)

#     emit('recognized_faces', {'faces_detected': detected_names})

# if __name__ == '__main__':
#     socketio.run(app, debug=True, host='0.0.0.0', port=5000)
