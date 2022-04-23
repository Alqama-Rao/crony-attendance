# import cv2
# import face_recognition
from fastapi import FastAPI
# import base64
# import numpy as np
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def string_return():
    return "Running"



@app.post("/check2/")
def check2(videoname: str):
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(videoname)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video  file")

    # Read until video is completed
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret is not True:
            if cap is not None:
                cap.release()
                cv2.destroyWindow(videoname)
            return "end"

        
@app.get("/compare_image")
def recognition(image,image2):
    image = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    image2 = cv2.GaussianBlur(image2, (5, 5), cv2.BORDER_DEFAULT)

    if image == image2:
        return "Same Image"
    else:
        return "Not The Same Image"
    # picture = base64.b64decode(image)
    # print("Decoded")
    # pic_as_np = np.frombuffer(picture, dtype=np.uint8)
    # frame = cv2.imdecode(pic_as_np, flags=1)
    #
    # encodeListKnown = list
    # frame = cv2.flip(frame, 1)
    #
    # faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    # faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
    #
    # facesCurrentFrame = face_recognition.face_locations(faces)
    # encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)
    #
    # for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
    #     matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
    #     faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
    #     # print(faceDis)
    #     matchIndex = np.argmin(faceDis)
    #
    #     if matches[matchIndex]:
    #         name = personNames[matchIndex].upper()
    #         print(name)
    #         # y1, x2, y2, x1 = faceLoc
    #         # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
    #         # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #         # cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
    #         # cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    #         # attendance(name)
    #         print(name)
    #         return name
    #     else:
    #         return "No Face Detected"

# def recognition(image, list, personNames):
#     picture = base64.b64decode(image)
#     print("Decoded")
#     pic_as_np = np.frombuffer(picture, dtype=np.uint8)
#     frame = cv2.imdecode(pic_as_np, flags=1)
#
#     encodeListKnown = list
#     frame = cv2.flip(frame, 1)
#
#     faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
#     faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
#
#     facesCurrentFrame = face_recognition.face_locations(faces)
#     encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)
#
#     for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#         # print(faceDis)
#         matchIndex = np.argmin(faceDis)
#
#         if matches[matchIndex]:
#             name = personNames[matchIndex].upper()
#             print(name)
#             # y1, x2, y2, x1 = faceLoc
#             # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             # cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             # cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#             # attendance(name)
#             print(name)
#             return name
#         else:
#             return "No Face Detected"



