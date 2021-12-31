import face_recognition
from face_recognition.api import face_locations
image = face_recognition.load_image_file("facesTest1.jpg")
face_locations = face_recognition.face_locations(image)
face_locations()