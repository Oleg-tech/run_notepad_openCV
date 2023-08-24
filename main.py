import time
import asyncio
import cv2 as cv
import numpy as np


gradient = "@#S%?*+;;,.     "
max_brightness = (0.375 * 255 + 0.5 * 255 + 0.16 * 255)


def write_to_txt_file(data):
    with open('file.txt', 'w') as file:
        file.write(data)


def run_rows(img):
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    pos = ((0.375 * r + 0.5 * g + 0.16 * b) / max_brightness) * 15
    ascii_indices = pos.astype(int)
    ascii_chars = np.array(list(gradient))[ascii_indices]
    ascii_picture = np.char.multiply(ascii_chars, 2)
    # ascii_picture = ascii_picture[::3, ::2]
    ascii_text = '\n'.join([''.join(row) for row in ascii_picture])

    write_to_txt_file(ascii_text)


def resize_video(input_path, output_path, target_width, target_height):
    cap = cv.VideoCapture(input_path)
    fps = int(cap.get(cv.CAP_PROP_FPS))
    codec = cv.VideoWriter_fourcc(*'XVID')  # Виберіть бажаний кодек

    out = cv.VideoWriter(output_path, codec, fps, (target_width, target_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv.resize(frame, (target_width, target_height))
        out.write(resized_frame)

    cap.release()
    out.release()
    cv.destroyAllWindows()


def main():
    start = time.time()    
    cap = resize_video('Erwins Last War Scream.mp4', 'output.mp4', 640, 480)
    print(f'{time.time() - start}')

    cap = cv.VideoCapture('Erwins Last War Scream.mp4')

    count = 1
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret or cv.waitKey(1) == ord('q'):
            print("Video ended")
            break

        print(count)
        count += 1

        start = time.time()
        run_rows(frame)
        print(f'{time.time() - start}')

        time.sleep(0.5)

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
