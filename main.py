import time
import numpy as np
import cv2 as cv


gradient = "@#S%?*+;;,.     "
max_brightness = (0.375 * 255 + 0.5 * 255 + 0.16 * 255)


def write_to_txt_file(data):
    with open('file.txt', 'w') as file:
        file.write(data)


def run_rows(img):
    ascii_picture = ''

    for i in range(2, img.shape[0]):
        for j in range(img.shape[1]):
            r, g, b = img[i][j]
            pos = ((0.375 * r + 0.5 * g + 0.16 * b) / max_brightness) * 15
            ascii_picture += gradient[int(pos)]
        ascii_picture += '\n'

    write_to_txt_file(ascii_picture)


def main():
    cap = cv.VideoCapture('video_5.mp4')

    count = 1
    while cap.isOpened():
        ret, frame = cap.read()
        print(count)
        count += 1
        start = time.time()
        run_rows(frame)
        print(time.time() - start)
        # if frame is read correctly ret is True
        if not ret or cv.waitKey(1) == ord('q'):
            print("Video ended")
            break
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        time.sleep(0.5)

        # cv.imshow('frame', gray)

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
