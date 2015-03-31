# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os


def test_capture():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def test_video():
    cap = cv2.VideoCapture(os.path.realpath('./../movie/test.mp4'))
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def test_save():
    # TODO the scripts bellow doesn't work on osx
    cap = cv2.VideoCapture(0)
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #fourcc = cv2.cv.CV_FOURCC(*'XVID')
    #fourcc = cv2.cv.CV_FOURCC(*'X264')
    fourcc = cv2.cv.CV_FOURCC('M', 'J', 'P', 'G')
    #fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
    #fourcc = cv2.cv.CV_FOURCC('I', 'Y', 'U', 'V')
    size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
    print size
    out = cv2.VideoWriter()
    success = out.open(os.path.realpath('./../movie/output.avi'), fourcc, 15, size, True)
    #out = cv2.VideoWriter(os.path.realpath('./../movie/output.avi'), fourcc, 20.0, (640, 480), True)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            #frame = cv2.flip(frame, 0)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break
    cap.release()
    out.release()
    out = None
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #test_video()
    test_save()
