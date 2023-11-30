import cv2
from deepface import DeepFace
from speak import speak

def recognize_faces(img):
    # Use deepface to perform face analysis
    result = DeepFace.analyze(img, enforce_detection=False)

    if result[0]["face_detected"]:
        name = "Sir"  # Replace with your actual logic to get the name
        print(f"Welcome back, {name}!")
        speak(f"Welcome back, {name}")
    else:
        print("None")
def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        ret, img = cap.read()

        recognize_faces(img)

        cv2.imshow('Camera', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
