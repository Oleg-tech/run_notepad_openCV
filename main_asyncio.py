import time
import cv2 as cv
import numpy as np
import multiprocessing


gradient = "@#S%?*+;;,.     "
max_brightness = (0.375 * 255 + 0.5 * 255 + 0.16 * 255)
pre_calculated_value = max_brightness/15

num_processes = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=num_processes)


def write_to_txt_file(data):
    with open('file.txt', 'w') as file:
        file.write(data)


def run_rows(img):
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    pos = (0.375 * r + 0.5 * g + 0.16 * b) * pre_calculated_value
    ascii_indices = pos.astype(int)
    ascii_chars = np.array(list(gradient))[ascii_indices]
    ascii_picture = np.char.multiply(ascii_chars, 2)
    ascii_picture = ascii_picture[::3, ::2]
    ascii_text = '\n'.join([''.join(row) for row in ascii_picture])

    write_to_txt_file(ascii_text)


def main():
    cap = cv.VideoCapture('Erwins Last War Scream.mp4')

    count = 1
    while cap.isOpened():
        ret, frame = cap.read()
        print(count)
        count += 1

        start = time.time()
        run_rows(frame)
        print(f'{time.time() - start}')

        if not ret or cv.waitKey(1) == ord('q'):
            print("Video ended")
            break

        time.sleep(0.5)

    pool.close()
    pool.join()

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
