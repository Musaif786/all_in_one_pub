import cv2
import getpass
import os

def capture_photo():
    # Open the default camera (you may need to adjust the index if you have multiple cameras)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read a frame from the camera
    data, frame = cap.read()

    # Save the captured frame as an image
    if data:
        username = getpass.getuser()
        image_path = f"{username}_login_capture.jpg"
        cv2.imwrite(image_path, frame)
        print(f"Photo captured and saved as: {image_path}")
    else:
        print("Error: Could not capture a photo.")

    # Release the camera
    cap.release()

if __name__ == "__main__":
    capture_photo()



'''
This python script will take picture whenever user login into a laptop
'''