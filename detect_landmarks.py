####################################################
#### REAL TIME FACIAL LAND MARKS DETECTION #########
####################################################

#import necessary libraries
import cv2
import dlib
import numpy as np

def shape_to_np(shape, dtype):
    # create an empty numpy array
    coord = np.zeros(shape=(68, 2), dtype=dtype)

    # fill the numpy array with coordinates
    for i in range(0, 68):
        coord[i] = (shape.part(i). x, shape.part(i).y)

    # return the numpy array
    return coord

try:
    #initialize camera
    cam = cv2.VideoCapture(0)
    print('initializing camera...')

    #load the frontal face detector and landmark model
    p = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)
    print('training model loaded...')
    #start capturing the frames
    while True:

        ret,frame = cam.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #detect faces in gray scale frame
        rects = detector(gray,0)

        #determine facial landmarks over the face
        for (i,rect) in enumerate(rects):
            shape = predictor(gray,rect)

            #convert facial landmarks to numpy array
            shape= shape_to_np(shape,"int")
            #print('after to np shape:',shape)

            #loops over (x,y) coordinates for facial landmarks
            for (x,y) in shape:
                cv2.circle(img=frame,center=(x,y),radius=2,color=(0,255,0),thickness=-1)
        cv2.putText(frame, """ "q" to exit""", (30,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow(winname="landmarks",mat=frame)
        if cv2.waitKey(delay=1) & 0xFF == ord('q'):
            break
except ImportError:
    print("Install Opencv and dlib libraries")
finally:
    print('exiting')
    cam.release()
    cv2.destroyAllWindows()




