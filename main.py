import cv2
import tkinter as tk
from tkinter import filedialog, Text, Button, Label, Frame, Entry, StringVar
from PIL import Image, ImageTk
import threading


class MotionDetectorApp:
    def __init__(self, root):
        # ...
        self.video_frame = Frame(root, width=640, height=480, bg="grey")
        # ...
        self.root = root
        self.root.title("MotionGuard360: Enhanced Object detection")
        self.root.geometry("1200x1200")

        # Add a title and a description
        title_label = Label(
            root, text="MotionGuard360: Enhanced Object detection", font=("Raavi", 24)
        )
        title_label.pack(pady=20)
        description_label = Label(
            root,
            text="This application detects motion in a video feed and highlights the areas with motion.",
            font=("Helvetica", 14),
        )
        description_label.pack(pady=10)

        # Use a grid layout
        self.grid_frame = Frame(root)
        self.grid_frame.pack(pady=20)

        self.label_video = Label(self.grid_frame, text="No video feed")
        self.label_video.grid(row=0, column=0, columnspan=3, padx=(20, 0))

        self.btn_start = Button(
            self.grid_frame, text="Start", command=self.start_detection
        )
        self.btn_start.grid(row=1, column=0, padx=(20, 0))

        self.btn_stop = Button(
            self.grid_frame, text="Stop", command=self.stop_detection
        )
        self.btn_stop.grid(row=1, column=1)

        self.btn_open = Button(
            self.grid_frame, text="Open Video", command=self.open_video
        )
        self.btn_open.grid(row=1, column=2)

        # Add a status label
        self.status_label = Label(root, text="Status: Idle", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Initialize Video Capture
        self.cap = None
        self.running = False

    def open_video(self):
        self.video_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")),
        )
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def start_detection(self):
        if not self.cap:
            self.cap = cv2.VideoCapture(0)  # Default to webcam if no file chosen
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.motion_detection)
            self.thread.start()
            self.status_label.config(text="Status: Detection started")

    def stop_detection(self):
        self.running = False
        self.thread.join()
        if self.cap:
            self.cap.release()
            self.cap = None
        self.label_video.configure(image="")
        self.status_label.config(text="Status: Idle")

    def motion_detection(self):
        ret, frame1 = self.cap.read()
        ret, frame2 = self.cap.read()

        while self.running and ret:
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(
                dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
            )

            for contour in contours:
                if cv2.contourArea(contour) < 500:
                    continue
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

            img = Image.fromarray(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
            img = img.resize((640, 480))
            imgtk = ImageTk.PhotoImage(image=img)
            self.label_video.imgtk = imgtk
            self.label_video.configure(image=imgtk)

            frame1 = frame2
            ret, frame2 = self.cap.read()

        if self.cap:
            self.cap.release()
            self.cap = None

        self.stop_detection()


if __name__ == "__main__":
    root = tk.Tk()
    app = MotionDetectorApp(root)
    root.mainloop()
