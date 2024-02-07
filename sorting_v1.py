import numpy as np
import cv2
import random
from  moviepy.video.io.ImageSequenceClip import ImageSequenceClip

import warnings
warnings.filterwarnings('ignore')

def break_image(ip_img, x_step, y_step):
    img_list = []
    k = 0
    for i in range(0, ip_img.shape[0], y_step):       
        for j in range(0, ip_img.shape[1], x_step):   
            crop_img = ip_img[i : i + y_step - 1, j : j + x_step - 1]
            img_list.append([k, crop_img])
            k += 1 
    return img_list

def reform_image(ip_img_list, ip_img, x_step, y_step):
    k = 0
    v_list = []
    for i in range(int(ip_img.shape[0]/y_step)):        
        h_list = []
        for j in range(int(ip_img.shape[1]/x_step)):    
            h_list.append(ip_img_list[k][1])
            k += 1
        img_h = cv2.hconcat(h_list) 
        v_list.append(img_h)

    reformed_img = cv2.vconcat(v_list)
    reformed_img = cv2.cvtColor(reformed_img, cv2.COLOR_BGR2RGB)
    return reformed_img

def bubble_sort(img_list, ip_img, x_step, y_step, fps, file_name):
    k = 0
    images = []
    for i in range(len(img_list) - 1):
        for j in range(len(img_list) - 1):
            if img_list[j][0] > img_list[j + 1][0]:
                img_list[j][0], img_list[j + 1][0] = img_list[j + 1][0], img_list[j][0]
                img_list[j][1], img_list[j + 1][1] = img_list[j + 1][1], img_list[j][1]

                temp_img = reform_image(img_list, ip_img, x_step = x_step, y_step = y_step)
                # cv2.imwrite('./bubble_sort/temp_' + str(k) + '.jpg', temp_img)
                images.append(temp_img)
                k += 1
                print(k)
    print('bubble sort completed!')

    clip = ImageSequenceClip(images, fps = fps)
    clip.write_videofile('./bubble_sort/' + file_name + '.mp4')

def selection_sort(img_list, ip_img, x_step, y_step, fps, file_name):
    k = 0
    images = []
    for i in range(len(img_list)):
        min_index = i
        for j in range(i + 1, len(img_list)):
            if img_list[j][0] < img_list[min_index][0]:
                min_index = j  
                temp_img = reform_image(img_list, ip_img, x_step = x_step, y_step = y_step)
                images.append(temp_img)
                k += 1
                print(k)
        img_list[i][0], img_list[min_index][0] = img_list[min_index][0], img_list[i][0]
        img_list[i][1], img_list[min_index][1] = img_list[min_index][1], img_list[i][1]

        # l = [img_list[x][0] for x in range(len(img_list))]
        # print(l)

        temp_img = reform_image(img_list, ip_img, x_step = x_step, y_step = y_step)
        images.append(temp_img)
        k += 1
        print(k)

    print('selection sort completed!')

    clip = ImageSequenceClip(images, fps = fps)
    clip.write_videofile('./selection_sort/' + file_name + '.mp4')

def main():
    img_rgb = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)

    x_step = 64
    y_step = 64

    fps = 30

    img_list = break_image(img_rgb, x_step = x_step, y_step = y_step)
    random.shuffle(img_list)
    temp_img = reform_image(img_list, img_rgb, x_step = x_step, y_step = y_step)
    
    cv2.imwrite('./bubble_sort/original_image.jpg', img_rgb)
    cv2.imwrite('./bubble_sort/shuffled_image.jpg', temp_img)
    bubble_sort(img_list, img_rgb, x_step = x_step, y_step = y_step, fps = fps, file_name = 'bubble_sort.mp4')

    random.shuffle(img_list)
    temp_img = reform_image(img_list, img_rgb, x_step = x_step, y_step = y_step)

    cv2.imwrite('./selection_sort/original_image.jpg', img_rgb)
    cv2.imwrite('./selection_sort/shuffled_image.jpg', temp_img)
    selection_sort(img_list, img_rgb, x_step = x_step, y_step = y_step, fps = fps, file_name = 'selection_sort.mp4')

if __name__ == '__main__':
    main()