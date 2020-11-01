import os
import pickle

from PyQt5.QtCore import *


class Worker(QRunnable):
    @pyqtSlot()
    def run(self):
        os.system('python heartbeat.py')


class NWorker(QRunnable):
    @pyqtSlot()
    def run(self):
        import sys
        from timeit import default_timer as timer

        import cv2

        start = timer()

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        cap = cv2.VideoCapture(0)
        c = 0
        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                k = 1
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    k = 0
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                if k == 1:
                    sys.stdout.write('\a')
                    sys.stdout.flush()
                    out = "You've blinked ", c, " times"
                    c = c + 1
                    # print (out)

            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k == ord('q'):
                break
        file = open("pickles/eye_blink_count.pickle",'wb')
        count = (int)(c)
        end = timer()
        sec = (int)(end - start)
        val = (int)((count * 60) / sec)
        pickle.dump(val,file)
        file.close()
        cap.release()
        cv2.destroyAllWindows()


class MWorker(QRunnable):
    @pyqtSlot()
    def run(self):
        import argparse
        import os

        import cv2
        import matplotlib.pyplot as plt
        import numpy as np
        from tensorflow.keras.layers import Conv2D
        from tensorflow.keras.layers import Dense, Dropout, Flatten
        from tensorflow.keras.layers import MaxPooling2D
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.preprocessing.image import ImageDataGenerator

        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        # command line argument
        ap = argparse.ArgumentParser()
        ap.add_argument("--mode", help="train/display")
        mode = ap.parse_args().mode
        l = []

        # plots accuracy and loss curves
        def plot_model_history(model_history):
            """
            Plot Accuracy and Loss curves given the model_history
            """
            fig, axs = plt.subplots(1, 2, figsize=(15, 5))
            # summarize history for accuracy
            axs[0].plot(range(1, len(model_history.history['accuracy']) + 1), model_history.history['accuracy'])
            axs[0].plot(range(1, len(model_history.history['val_accuracy']) + 1), model_history.history['val_accuracy'])
            axs[0].set_title('Model Accuracy')
            axs[0].set_ylabel('Accuracy')
            axs[0].set_xlabel('Epoch')
            axs[0].set_xticks(np.arange(1, len(model_history.history['accuracy']) + 1),
                              len(model_history.history['accuracy']) / 10)
            axs[0].legend(['train', 'val'], loc='best')
            # summarize history for loss
            axs[1].plot(range(1, len(model_history.history['loss']) + 1), model_history.history['loss'])
            axs[1].plot(range(1, len(model_history.history['val_loss']) + 1), model_history.history['val_loss'])
            axs[1].set_title('Model Loss')
            axs[1].set_ylabel('Loss')
            axs[1].set_xlabel('Epoch')
            axs[1].set_xticks(np.arange(1, len(model_history.history['loss']) + 1),
                              len(model_history.history['loss']) / 10)
            axs[1].legend(['train', 'val'], loc='best')
            fig.savefig('plot.png')
            plt.show()

        # Define data generators
        train_dir = 'data/train'
        val_dir = 'data/test'

        num_train = 28709
        num_val = 7178
        batch_size = 64
        num_epoch = 50

        train_datagen = ImageDataGenerator(rescale=1. / 255)
        val_datagen = ImageDataGenerator(rescale=1. / 255)

        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(48, 48),
            batch_size=batch_size,
            color_mode="grayscale",
            class_mode='categorical')

        validation_generator = val_datagen.flow_from_directory(
            val_dir,
            target_size=(48, 48),
            batch_size=batch_size,
            color_mode="grayscale",
            class_mode='categorical')

        # Create the model
        model = Sequential()

        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
        model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(1024, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(7, activation='softmax'))

        # emotions will be displayed on your face from the webcam feed
        model.load_weights('model.h5')

        # prevents openCL usage and unnecessary logging messages
        cv2.ocl.setUseOpenCL(False)

        # dictionary which assigns each label an emotion (alphabetical order)
        emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

        # start the webcam feed
        cap = cv2.VideoCapture(0)
        while True:
            # Find haar cascade to draw bounding box around face
            ret, frame = cap.read()
            if not ret:
                break
            facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                prediction = model.predict(cropped_img)
                maxindex = int(np.argmax(prediction))
                l.append(maxindex)
                cv2.putText(frame, emotion_dict[maxindex], (x + 20, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 255),
                            2, cv2.LINE_AA)

            cv2.imshow('Video', cv2.resize(frame, (1600, 960), interpolation=cv2.INTER_CUBIC))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                a = np.array(l)
                counts = np.bincount(a)
                with open('pickles/emotion.pickle','wb') as file:
                    pickle.dump(emotion_dict[counts.argmax()],file)
                break

        cap.release()
        cv2.destroyAllWindows()


class OWorker(QRunnable):
    @pyqtSlot()
    def run(self):
        os.system("python audio-speech2.py")


class PWorker(QRunnable):
    @pyqtSlot()
    def run(self):
        os.system("python heartbeat.py")
