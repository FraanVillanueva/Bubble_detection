import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def main(argv):
    default_file = '1.jpeg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src1 = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    src=cv.resize(src1,(int(src1.shape[1]/4),int(src1.shape[0]/4)), interpolation=cv.INTER_AREA)
    # Check if image is loaded fine
    
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            if gray[i][j]>=150:
                gray[i][j]=255
            else:
                gray[i][j] = 0
    gray = cv.medianBlur(gray, 5)
    im=Image.fromarray(gray)
    im.show()
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 100,
                              param1=100, param2=30,
                              minRadius=0, maxRadius=70)
    data_radius=[]
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
            data_radius.append(radius.astype(float))
    #Data Analysis
    if data_radius!=[]:
        plt.xlim([min(data_radius),max(data_radius)])
        plt.hist(data_radius,bins=np.arange(0,100,5),alpha=0.5)
        plt.xlabel('Bubble Size (pixel)')
        plt.ylabel('Count')
    cv.imshow("detected circles", src)
    plt.show()
    cv.waitKey(0)
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
