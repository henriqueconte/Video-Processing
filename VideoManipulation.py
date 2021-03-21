import cv2
import numpy as np

def printInstructions():
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

printInstructions()

beforeVideo = cv2.VideoCapture(0)
afterVideo = cv2.VideoCapture(0)

while True:
    retBefore, frameBefore = beforeVideo.read()
    retAfter, frameAfter = afterVideo.read()
    
    retBefore = beforeVideo.set(3, 320)
    retBefore = beforeVideo.set(4, 240)
    # frameBefore = cv2.cvtColor(frameBefore,cv2.COLOR_BGR2RGB)
    # frameAfter = cv2.cvtColor(frameAfter,cv2.COLOR_BGR2RGB)

    cv2.imshow("Before",frameBefore)
    cv2.imshow("After",frameAfter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

beforeVideo.release()
afterVideo.release()
cv2.destroyAllWindows()
