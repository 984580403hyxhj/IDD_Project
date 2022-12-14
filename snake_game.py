import time

import mediapipe as mp
import math
import random
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

from pygame import mixer  # Load the popular external library

from screeninfo import get_monitors
width = get_monitors()[0].width
height = get_monitors()[0].height
print(width,height)
mixer.init()


cap = cv2.VideoCapture(0)
cap.set(3, 2400)
cap.set(4, 1020)

detector = HandDetector(detectionCon=0.8, maxHands=1)
imgHand = cv2.imread("show_hand.png", cv2.IMREAD_UNCHANGED)
imgForawrd = cv2.imread("move_forward.png", cv2.IMREAD_UNCHANGED)
red = cv2.imread("red.png", cv2.IMREAD_UNCHANGED)

class SnakeGameClass:
    def __init__(self, pathFood, pathHuman):
        self.points = None  # all points of the snake
        self.points2 = None
        self.fireballSpeed = 20

        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.imgHuman = cv2.imread(pathHuman, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.hHuman, self.wHuman, _ = self.imgHuman.shape
        self.rescuePoint = 0, 0
        self.rescuePoint2 = 0, 0
        self.rescuePoint3 = 0, 0
        self.humanPoint = 0, 0
        self.randomFoodLocation()
        self.randomFoodLocation2()
        self.randomFoodLocation3()
        self.randomHumanLocation()

        self.score = 0
        self.gameOver = False
        self.isHurt = False
        self.isDonutTime = False
        self.DonutTime()


    def DonutTime(self):
        if not self.isDonutTime:
            self.imgFood = cv2.imread("fireball.png", cv2.IMREAD_UNCHANGED)
        else:
            self.imgFood = cv2.imread("donut.png", cv2.IMREAD_UNCHANGED)



    def randomHumanLocation(self):
        self.humanPoint = random.randint(100, 1000), 850

    def randomFoodLocation(self):
        self.rescuePoint = random.randint(100, 1000), 101

    def randomFoodLocation2(self):
        self.rescuePoint2 = random.randint(100, 1000), 101

    def randomFoodLocation3(self):
        self.rescuePoint3 = random.randint(100, 1000), 101

    def update(self, imgMain, currentHead, currentHead2 = None):
        cx, cy = currentHead
        self.points = [cx, cy]
        if currentHead2:
            c2x, c2y = currentHead2
            self.points2 = [c2x, c2y]

        # Check if player hit the fire ball ***
        rx, ry = self.rescuePoint
        self.rescuePoint = rx, ry + self.fireballSpeed
        rx, ry = self.rescuePoint
        if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and ry - self.hFood // 2 < cy < ry + self.hFood // 2:
            mixer.music.load('ouch-sound-effect-30-11844.mp3')
            self.randomFoodLocation()
            if not self.isDonutTime:
                mixer.music.play()
                self.score -= 2
                print(self.score)
                self.isHurt = True
            else:
                self.score += 2

        rx, ry = self.rescuePoint2
        self.rescuePoint2 = rx, ry + self.fireballSpeed
        rx, ry = self.rescuePoint2
        if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and ry - self.hFood // 2 < cy < ry + self.hFood // 2:
            mixer.music.load('ouch-sound-effect-30-11844.mp3')
            self.randomFoodLocation2()
            if not self.isDonutTime:
                mixer.music.play()
                self.score -= 2
                print(self.score)
                self.isHurt = True
            else:
                self.score += 2

        rx, ry = self.rescuePoint3
        self.rescuePoint3 = rx, ry + self.fireballSpeed
        rx, ry = self.rescuePoint3
        if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and ry - self.hFood // 2 < cy < ry + self.hFood // 2:
            mixer.music.load('ouch-sound-effect-30-11844.mp3')
            self.randomFoodLocation3()
            if not self.isDonutTime:
                mixer.music.play()
                self.score -= 2
                print(self.score)
                self.isHurt = True
            else:
                self.score += 2

        if currentHead2:
            rx, ry = self.rescuePoint
            if rx - self.wFood // 2 < c2x < rx + self.wFood // 2 and \
                    ry - self.hFood // 2 < c2y < ry + self.hFood // 2:
                mixer.music.load('ouch-sound-effect-30-11844.mp3')
                self.randomFoodLocation()
                mixer.music.play()
                self.score -= 2
                print(self.score)

        ## if save the human
        rhx, rhy = self.humanPoint
        if rhx - self.wHuman // 2 < cx < rhx + self.wHuman // 2 and rhy - self.hHuman // 2 < cy < rhy + self.hHuman // 2:
            self.randomHumanLocation()
            mixer.music.load('thankyou.mp3')
            mixer.music.play()
            self.score += 5
            print(self.score)

        if currentHead2:
            rhx, rhy = self.humanPoint
            if rhx - self.wHuman // 2 < c2x < rhx + self.wHuman // 2 and rhy - self.hHuman // 2 < c2y < rhy + self.hHuman // 2:
                self.randomHumanLocation()
                mixer.music.load('thankyou.mp3')
                mixer.music.play()
                self.score += 5
                print(self.score)

        ## if fire hit human
        rhx, rhy = self.humanPoint
        if rhx - self.wHuman // 2 < self.rescuePoint[0] < rhx + self.wHuman // 2 and rhy - self.hHuman // 2 < self.rescuePoint[1] < rhy + self.hHuman // 2:
            mixer.music.load('ouch-sound-effect-30-11844.mp3')
            self.randomHumanLocation()
            mixer.music.play()
            self.score -= 5
            print(self.score)


        # Draw Snake ***
        if self.points:
            cv2.circle(imgMain, self.points, 20, (0, 255, 0), cv2.FILLED)

            # Draw Food
            try:
                rx, ry = self.rescuePoint
                imgMain = cvzone.overlayPNG(imgMain, self.imgFood, (rx - self.wFood // 2, ry - self.hFood // 2))
            except Exception as e:
                self.randomFoodLocation()

            try:
                rx, ry = self.rescuePoint2
                imgMain = cvzone.overlayPNG(imgMain, self.imgFood, (rx - self.wFood // 2, ry - self.hFood // 2))
            except Exception as e:
                self.randomFoodLocation2()

            try:
                rx, ry = self.rescuePoint3
                imgMain = cvzone.overlayPNG(imgMain, self.imgFood, (rx - self.wFood // 2, ry - self.hFood // 2))
            except Exception as e:
                self.randomFoodLocation3()

            try:
                imgMain = cvzone.overlayPNG(imgMain, self.imgHuman, (rhx - self.wHuman // 2, rhy - self.hHuman // 2))
            except Exception as e:
                print(e)
                self.randomHumanLocation()

            cvzone.putTextRect(imgMain, f'Score: {self.score}', [50, 80], scale=3, thickness=3, offset=10)

        if self.points2:
            cv2.circle(imgMain, self.points2, 20, (0, 255, 0), cv2.FILLED)

        return imgMain


game = SnakeGameClass("fireball.png", "human.png")
game.DonutTime()
hurt_time = 20
donut_time = 100
i = 0
j = 0
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        if len(hands) == 2:
            lmList = hands[0]['lmList']
            pointIndex = lmList[8][0:2]
            lmList2 = hands[1]['lmList']
            pointIndex2 = lmList2[8][0:2]
            img = game.update(img, pointIndex, pointIndex2)
        else:
            lmList = hands[0]['lmList']
            pointIndex = lmList[8][0:2]
            img = game.update(img, pointIndex)

        if game.isHurt and not game.isDonutTime:
            i += 1
            if i == hurt_time:
                game.isHurt = False
                i = 0
            img =cvzone.overlayPNG(img, red)

        if game.score > 50:
            game.score -= 50
            game.isDonutTime = True
            game.DonutTime();

        if game.isDonutTime:
            j += 1
            if j == donut_time:
                j = 0
                game.isDonutTime = False
                game.DonutTime()

    else:
        img = imgHand
        # img = imgForawrd



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        game.gameOver = False