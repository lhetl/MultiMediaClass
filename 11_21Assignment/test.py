import os

import cv2
from PIL import Image
import numpy as np
def read_image(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    return image

def show_image(image, window_name="Image"):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_to_grayscale(image):
    height, width, _ = image.shape
    grayscale_image = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            b, g, r = image[i, j]
            grayscale_image[i, j] = 0.299 * r + 0.587 * g + 0.114 * b

    return grayscale_image

def show_rgb_channels(image):
    height, width, _ = image.shape
    b, g, r = cv2.split(image)

    zeros = np.zeros((height, width), dtype=np.uint8)

    blue_channel = cv2.merge([b, zeros, zeros])
    green_channel = cv2.merge([zeros, g, zeros])
    red_channel = cv2.merge([zeros, zeros, r])

    cv2.imshow("Blue Channel", blue_channel)
    cv2.imshow("Green Channel", green_channel)
    cv2.imshow("Red Channel", red_channel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_yuv_channels(image):
    height, width, _ = image.shape
    yuv_image = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            b, g, r = image[i, j]
            yuv_image[i, j, 0] = 0.299 * r + 0.587 * g + 0.114 * b
            yuv_image[i, j, 1] = 0.564 * (b - yuv_image[i, j, 0])
            yuv_image[i, j, 2] = 0.713 * (r - yuv_image[i, j, 0])

    cv2.imshow("Y Channel", yuv_image[:, :, 0])
    cv2.imshow("U Channel", yuv_image[:, :, 1])
    cv2.imshow("V Channel", yuv_image[:, :, 2])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def flip_horizontal(image):
    height, width, _ = image.shape
    flipped_image = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            flipped_image[i, j] = image[i, width - j - 1]

    return flipped_image

def flip_vertical(image):
    height, width, _ = image.shape
    flipped_image = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        flipped_image[i] = image[height - i - 1]

    return flipped_image

def crop_50_percent(image):
    height, width, _ = image.shape
    start_row, start_col = int(height * 0.25), int(width * 0.25)
    end_row, end_col = int(height * 0.75), int(width * 0.75)
    cropped_image = image[start_row:end_row, start_col:end_col]
    return cropped_image

if __name__ == "__main__":
    file_path = input("Enter the directory + filename of the image: ")
    tmp=os.path.join(os.path.dirname(__file__))+"\\image\\"+file_path
    image = read_image(tmp)

    while True:
        print("\n1. Show Color Image")
        print("2. Show Grayscale Image")
        print("3. Show RGB Channels")
        print("4. Show YUV Channels")
        print("5. Flip Horizontal")
        print("6. Flip Vertical")
        print("7. Crop 50%")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            show_image(image, "Color Image")
        elif choice == "2":
            grayscale_image = convert_to_grayscale(image)
            show_image(grayscale_image, "Grayscale Image")
        elif choice == "3":
            show_rgb_channels(image)
        elif choice == "4":
            show_yuv_channels(image)
        elif choice == "5":
            flipped_image = flip_horizontal(image)
            show_image(flipped_image, "Flipped Horizontal")
        elif choice == "6":
            flipped_image = flip_vertical(image)
            show_image(flipped_image, "Flipped Vertical")
        elif choice == "7":
            cropped_image = crop_50_percent(image)
            show_image(cropped_image, "Cropped 50%")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
