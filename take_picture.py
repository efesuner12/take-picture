from pathlib import Path
import time
import cv2
import os

def take_picture():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)  # If you don't wait, the image will be dark

    return_value, image = camera.read()

    take_picture.counter = int(readCounterVal())

    filename = Path("pic.png")

    if filename.is_file():
        filename = f"pic{take_picture.counter}.png"
        take_picture.counter += 1
        writeCounterVal(str(take_picture.counter))

    cv2.imwrite(str(filename), image)

    print("Picture took!")

    print(os.path.abspath(str(filename)))

    del(camera)

def writeCounterVal(value):
    f = open("counterValPIC.txt", "w")

    if not Path("counterValPIC.txt").is_file():
        f.write("0")
    else:
        f.write(value)

    f.close()

def readCounterVal():
    if not Path("counterValPIC.txt").is_file():
        content = "0"
    else:
        f = open("counterValPIC.txt", "r")
        content = f.read()
        f.close()

    return content


if __name__ == "__main__":
    take_picture()
    