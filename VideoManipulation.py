import cv2
import numpy as np
import keyboard

def printInstructions():
    print('1: Flip the video horizontally')
    print('2: Flip the video vertically')
    print('3: Flip the video both horizontal and vertically')
    print('4: Decrease brightness')
    print('5: Increase brightness')
    print('6: Decrease contrast')
    print('7: Increase contrast')
    print('Q or q: quit')
    print('B or b: Blurring (Gaussian)')
    print('C or c: Color (no processing)')
    print('E or e: Edges (Canny)')
    print('G or g: Grayscale')
    print('N or n: Negative')
    print('S or s: Gradient (Sobel)')
    print('T or t: rotate the video frames')
    print('V or v: toggle Video recording')
    print('Z or z: toggle resize frame to 1/4 of the original size')


def gaussianBlur(frame):
    return cv2.GaussianBlur(frame, (5,5), 10)

def canny(frame):
    return cv2.Canny(frame, 100, 200)

def sobel(frame):
    frame = grayScale(frame)
    return cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)

def grayScale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def changeBrightness(frame):
    frame = cv2.convertScaleAbs(frame, alpha=1, beta=10 * brightnessCount)
    # frame = cv2.add(frame, 10 * brightnessCount)
    # frame = [0 if value < 0 else value for value in frame]
    # frame[frame < 0]
    # frame = np.add(frame, 10 * brightnessCount)
    return frame

# def increaseBrightness(frame):
#     frame = cv2.convertScaleAbs(frame, alpha=1, beta=10 * brightnessCount)
#     return frame

# def decreaseContrast(frame):
#     frame = cv2.convertScaleAbs(frame, alpha=1 + (contrastCount * 0.1), beta=0)
#     return frame

def changeContrast(frame):
    frame = cv2.convertScaleAbs(frame, alpha=1 + (contrastCount * 0.1), beta=0)
    # frame = np.clip(frame, 0, 255)
    return frame

def resize(frame):
    return cv2.resize(frame, (int(afterVideo.get(3) / 2), int(afterVideo.get(4) / 2)), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)

def rotate(frame):
    return cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)

def flip(frame, flipMode):
    return cv2.flip(frame, int(flipMode))

def applyFilter(pressedKey, firstFrame, secondFrame):
    if pressedKey == '1':
        return flip(secondFrame, '1')
    elif pressedKey == '2':
        return flip(secondFrame, '0')
    elif pressedKey == '3':
        return flip(secondFrame, '-1')
    elif pressedKey == '4':
        return changeBrightness(firstFrame)
    elif pressedKey == '5':
        return changeBrightness(firstFrame)
    elif pressedKey == '6':
        return changeContrast(firstFrame)
    elif pressedKey == '7':
        return changeContrast(firstFrame)
    elif pressedKey == 'c':
        return firstFrame
    elif pressedKey == 'b':
        return gaussianBlur(secondFrame)
    elif pressedKey == 'e':
        return canny(firstFrame)
    elif pressedKey == 'g':
        return grayScale(secondFrame)
    elif pressedKey == 'n':
        return secondFrame
    elif pressedKey == 's':
        return sobel(firstFrame)
    elif pressedKey == 't':
        return rotate(secondFrame)
    elif pressedKey == 'v':
        return secondFrame
    elif pressedKey == 'z':
        return resize(secondFrame)
    else: 
        return secondFrame

printInstructions()

beforeVideo = cv2.VideoCapture(0)
afterVideo = cv2.VideoCapture(0)
width = int(afterVideo.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(afterVideo.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
videoWriter = cv2.VideoWriter('video_demo.mov',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 10.0, size)
pressedKey = 'c'
isRecording = False
appliedFilters = []
brightnessCount = 0
contrastCount = 0


while True:
    retBefore, frameBefore = beforeVideo.read()
    retAfter, frameAfter = afterVideo.read()
    
    # Sets frame size from windows
    retBefore = beforeVideo.set(3, size[0])
    retBefore = beforeVideo.set(4, size[1])
    retAfter = afterVideo.set(3, size[0])
    retAfter = afterVideo.set(4, size[1])

    for currentFilter in appliedFilters:
        frameAfter = applyFilter(currentFilter, frameBefore, frameAfter)

    if isRecording:
        videoWriter.write(frameAfter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if keyboard.is_pressed('q'):
        break
    elif keyboard.is_pressed('b'):
        appliedFilters.append('b')
        pressedKey = 'b'
    elif keyboard.is_pressed('c'):
        appliedFilters = []
        brightnessCount = 0
        contrastCount = 0
        pressedKey = 'c'
    elif keyboard.is_pressed('e'):
        appliedFilters = []
        appliedFilters.append('e')
        pressedKey = 'e'
    elif keyboard.is_pressed('f'):
        appliedFilters.append('f')
        pressedKey = 'f'
    elif keyboard.is_pressed('1'):
        appliedFilters.append('1')
        pressedKey = '1'
    elif keyboard.is_pressed('2'):
        appliedFilters.append('2')
        pressedKey = '2'
    elif keyboard.is_pressed('3'):
        appliedFilters.append('3')
        pressedKey = '3'
    elif keyboard.is_pressed('4'):
        appliedFilters.append('4')
        pressedKey = '4'
        brightnessCount -= 1
    elif keyboard.is_pressed('5'):
        appliedFilters.append('5')
        pressedKey = '5'
        brightnessCount += 1
    elif keyboard.is_pressed('6'):
        appliedFilters.append('6')
        pressedKey = '6'
        contrastCount -= 1
    elif keyboard.is_pressed('7'):
        appliedFilters.append('7')
        pressedKey = '7'
        contrastCount += 1
    elif keyboard.is_pressed('g'):
        appliedFilters = []
        appliedFilters.append('g')
        pressedKey = 'g'
    elif keyboard.is_pressed('n'):
        appliedFilters = []
        appliedFilters.append('n')
        pressedKey = 'n'
    elif keyboard.is_pressed('s'):
        appliedFilters = []
        appliedFilters.append('s')
        pressedKey = 's'
    elif keyboard.is_pressed('t'):
        appliedFilters.append('t')
        pressedKey = 't'
    elif keyboard.is_pressed('v'):
        isRecording = not isRecording
    elif keyboard.is_pressed('z'):
        appliedFilters.append('z')
        pressedKey = 'z'

    # Show before and after videos
    cv2.imshow("Before",frameBefore)
    cv2.imshow('After',frameAfter)

videoWriter.release()
beforeVideo.release()
afterVideo.release()
cv2.destroyAllWindows()

