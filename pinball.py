import random
import pygame  # versio 2.5.1
import cv2  # mediapipe 0.9.0.1
import cvzone  # version 1.5.6
import numpy as np
from cvzone.HandTrackingModule import HandDetector

pygame.init()

cam = cv2.VideoCapture(0)
cam.set(3, 1280)
cam.set(4, 720)

w, h = 1280, 720
wind = pygame.display.set_mode((w, h))
pygame.display.set_caption("LapTop.studios (Для конкурса) Пинбол")

fps = 30
clock = pygame.time.Clock()

blpoz = [615, 335]
score = [0, 0]
gameover = False
_x = random.randint(-2, 2) * 15
_y = random.randint(-2, 2) * 15

if _y == 0:
    _y += 2*15
if _x == 0:
    _x += -2*15

detector = HandDetector(detectionCon = 0.8, maxHands = 2)

stop = True
while stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = False
            pygame.quit()

    imgbg = cv2.imread("RESURSES/Background.png")
    imgball = cv2.imread("RESURSES/Ball.png", cv2.IMREAD_UNCHANGED)
    imgbat1 = cv2.imread("RESURSES/bat1.png", cv2.IMREAD_UNCHANGED)
    imgbat2 = cv2.imread("RESURSES/bat2.png", cv2.IMREAD_UNCHANGED)
    imggameover = cv2.imread("RESURSES/gameOver.png")

    _, img = cam.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    img = cv2.addWeighted(img, 0.2, imgbg, 0.8, 0)

    if hands:
        for hand in hands:
            x, y, w, h = hand["bbox"]
            h1, w1, _ = imgbat1.shape
            y1 = y - h1//2
            y1 = np.clip(y1, 20, 415)

            if hand["type"] == "Right":
                img = cvzone.overlayPNG(img, imgbat1, (60, y1))
                if blpoz[0] < 60 + w1 and y1 < blpoz[1] < y1 + h1:
                    _x = -_x

            if hand["type"] == "Left":
                img = cvzone.overlayPNG(img, imgbat2, (1190, y1))
                if blpoz[0] > 1190 - 56 and y1 < blpoz[1] < y1 + h1:
                    _x = -_x

    if blpoz[0] >= 1190:
        score[0] += 1
        blpoz = [615, 335]
        _x = -_x

    if blpoz[0] <= 60:
        score[1] += 1
        blpoz = [615, 335]
        _x = -_x

    if blpoz[1] >= 490 or blpoz[1] <= 20:

        _y = -_y

    blpoz[0] += _x
    blpoz[1] += _y

    if gameover == False:
        img = cvzone.overlayPNG(img, imgball, blpoz)
    else:
        _x = 0
        _y = 0

    if score[0] == 5:
        img = imggameover
        cv2.putText(img, "15", (590, 355), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 4)
        gameover = True

    if score[1] == 5:
        img = imggameover
        cv2.putText(img, "15", (590, 355), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 4)
        gameover = True

    cv2.putText(img, str(int(score[0])) + ":" + str(int(score[1])), (565, 670), cv2.FONT_HERSHEY_PLAIN, 6, (255, 255, 255), 4)

    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgrgb = np.rot90(imgrgb)
    frame = pygame.surfarray.make_surface(imgrgb).convert()
    frame = pygame.transform.flip(frame, True, False)

    wind.fill((255, 255, 255))
    wind.blit(frame, (0, 0))

    #cv2.imshow("Pingpong", img)

    cv2.waitKey(1)

    pygame.display.update()
    clock.tick(fps)