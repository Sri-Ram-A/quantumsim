from customtkinter import CTkButton
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import subprocess

class VideoPlayer(tk.Tk):
    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path
        self.title("Video Player with Button")
        self.geometry("1600x900")

        # Define the desired video size
        self.video_width = 1600
        self.video_height = 900

        self.video_label = tk.Label(self)
        self.video_label.pack()

        self.cap = cv2.VideoCapture(self.video_path)
        self.play_video()

        # Create a button and place it in the center of the video
        self.button = CTkButton(
            master=self,
            anchor='center',
            command=self.open_file,
            text="Get Started >",
            font=('Bold', 40),
            text_color='#FFFFFF',
            fg_color='black',
            hover_color='#651fff',
            corner_radius=10,
            bg_color='black',
            border_color='#FFFFFF',
            border_width=2,
            width=300,
            height=60
        ).place(
            x=680,
            y=565
        )

    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (self.video_width, self.video_height))  # Resize the frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
            self.after(30, self.play_video)  # Schedule the next frame update
        else:
            self.cap.release()

    def open_file(self):
        file_path = r"quantumsim-main-main\gui\actual.py"
        try:
            subprocess.Popen(["python", file_path])
            self.destroy()  # Close the Tkinter window
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open the file: {e}")

if __name__ == "__main__":
    #video_path = r"quantumsim-main-main\gui\Begin quantum simulating (1).mp4"  # Replace with the path to your video file
    
    video_path=r"quantumsim-main-main\gui\megatron.gif"
    app = VideoPlayer(video_path)
    app.mainloop()

