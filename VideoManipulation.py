import cv2
import numpy as np
import keyboard

def printInstructions():
    print('Q or q: quit')
    print('B or b: Blurring (Gaussian)')
    print('C or c: Color (no processing)')
    print('E or e: Edges (Canny)')
    print('F or f: Flip the video')
    print('+ or -: Increment/Decrement Flip mode: mode = 0 (default): Vertical; mode > 0: Horizontal; mode < 0: Vert & Horiz.')
    print('G or g: Grayscale')
    print('H or h: Help')
    print('N or n: Negative')
    print('O or o: Contrast enhancement')
    print('R or r: brightness enhancement')
    print('S or s: Gradient (Sobel)')
    print('T or t: rotate the video frames')
    print('V or v: toggle Video recording')
    print('Z or z: toggle resize frame to 1/4 of the original size')

def nothing(x):
    print(x)

def presentTrackbar():
    emptyWindow = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('After - controls')
    cv2.createTrackbar('Value', 'After - controls', 0, 30, nothing)    
    cv2.imshow('After - controls', emptyWindow)


def gaussianBlur(frame):
    return cv2.GaussianBlur(frame, (5,5), 10)

def canny(frame):
    return cv2.Canny(frame, 100, 200)

def sobel(frame):
    frame = grayScale(frame)
    return cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)

def grayScale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def increaseBrightness(frame):
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # h,s,v = cv2.split(hsv)
    # v += 50
    # final_hsv = cv2.merge((h,s,v))
    # frame = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    
    # Possibilidade: https://docs.opencv.org/3.4/d3/dc1/tutorial_basic_linear_transform.html

    return frame

def resize(frame):
    return cv2.resize(frame, (int(afterVideo.get(3) / 2), int(afterVideo.get(4) / 2)), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)

def applyFilter(pressedKey, firstFrame, secondFrame):
    if pressedKey == 'c':
        return firstFrame
    elif pressedKey == 'b':
        return gaussianBlur(secondFrame)
    elif pressedKey == 'e':
        return canny(firstFrame)
    elif pressedKey == 'f':
        return secondFrame
    elif pressedKey == '+':
        return secondFrame
    elif pressedKey == '-':
        return secondFrame
    elif pressedKey == 'g':
        return grayScale(secondFrame)
    elif pressedKey == 'h':
        return secondFrame
    elif pressedKey == 'n':
        return secondFrame
    elif pressedKey == 'o':
        return secondFrame
    elif pressedKey == 'r':
        return increaseBrightness(secondFrame)
    elif pressedKey == 's':
        return sobel(firstFrame)
    elif pressedKey == 't':
        return secondFrame
    elif pressedKey == 'v':
        return secondFrame
    elif pressedKey == 'z':
        return resize(secondFrame)
    else: 
        return secondFrame

printInstructions()
# presentTrackbar()

beforeVideo = cv2.VideoCapture(0)
afterVideo = cv2.VideoCapture(0)
pressedKey = 'c'

while True:
    retBefore, frameBefore = beforeVideo.read()
    retAfter, frameAfter = afterVideo.read()
    
    # Sets frame size from windows
    retBefore = beforeVideo.set(3, 320)
    retBefore = beforeVideo.set(4, 240)
    # frameBefore = cv2.cvtColor(frameBefore,cv2.COLOR_BGR2RGB)
    # frameAfter = cv2.cvtColor(frameAfter,cv2.COLOR_BGR2RGB)

    frameAfter = applyFilter(pressedKey, frameBefore, frameAfter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if keyboard.is_pressed('q'):
        break
    elif keyboard.is_pressed('b'):
        pressedKey = 'b'
    elif keyboard.is_pressed('c'):
        pressedKey = 'c'
    elif keyboard.is_pressed('e'):
        pressedKey = 'e'
    elif keyboard.is_pressed('f'):
        pressedKey = 'f'
    elif keyboard.is_pressed('+'):
        pressedKey = '+'
    elif keyboard.is_pressed('-'):
        pressedKey = '-'
    elif keyboard.is_pressed('g'):
        pressedKey = 'g'
    elif keyboard.is_pressed('h'):
        pressedKey = 'h'
    elif keyboard.is_pressed('n'):
        pressedKey = 'n'
    elif keyboard.is_pressed('o'):
        pressedKey = 'o'
    elif keyboard.is_pressed('r'):
        pressedKey = 'r'
    elif keyboard.is_pressed('s'):
        pressedKey = 's'
    elif keyboard.is_pressed('t'):
        pressedKey = 't'
    elif keyboard.is_pressed('v'):
        pressedKey = 'v'
    elif keyboard.is_pressed('z'):
        pressedKey = 'z'

    # Show before and after videos
    cv2.imshow("Before",frameBefore)
    cv2.imshow('After',frameAfter)

beforeVideo.release()
afterVideo.release()
cv2.destroyAllWindows()

