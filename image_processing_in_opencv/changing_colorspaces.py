# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os

size = (400, 225)


def test_video():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame, size)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # blue
        lower = np.array([110, 50, 50])
        upper = np.array([130, 255, 255])
        blue_mask = cv2.inRange(hsv, lower, upper)
        # fresh
        lower = np.array([0, 50, 50])
        upper = np.array([15, 255, 255])
        fresh_mask = cv2.inRange(hsv, lower, upper)

        mask = cv2.bitwise_or(blue_mask, fresh_mask)

        res = cv2.bitwise_and(frame, frame, mask=mask)
        # above could be like bellow
        #mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        #res = cv2.bitwise_and(frame, mask)

        cv2.imshow('blue_mask', blue_mask)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test_video()
