from tkinter import Tk, Canvas, Entry, StringVar, Frame
from customtkinter import CTkButton
import customtkinter as ct
from PIL import Image, ImageTk
import re
import numpy as np
import matplotlib.pyplot as plt
from quantum_gates import *
from datetime import datetime
import os
from bloch import plot_bloch_sphere, update_bloch_sphere
from probability_bargraph import *

plt.style.use("dark_background")


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Tkinter App")
        self.num_frames = 30

       

        self.log_file = self.initialize_log_file()

        self.canvas = Canvas(
            self.root,
            # bg="black",
            height=900,
            width=1600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        # Load and place the background image
        image = Image.open(r"quantumsim-main-main\\gui\\Quantum Circuit Simulation.png")
        resized_image = image.resize((1635, 850), resample=Image.Resampling.LANCZOS)
        self.image_image_1 = ImageTk.PhotoImage(resized_image)
        self.image_1 = self.canvas.create_image(
            775.0,
            420.0,
            image=self.image_image_1
        )
       
        self.input_y = 1 # Initial y position for the first inputFrame
       
        self.create_button('+', x=359, y=775, command=self.add_input_field)
        self.create_button_1(text='X', x=49, y=163, command=lambda: self.clickButton('X'))
        self.create_button_1(text='Y', x=150, y=163, command=lambda: self.clickButton('Y'))
        self.create_button_1(text='Z', x=257, y=163, command=lambda: self.clickButton('Z'))
        self.create_button_2(text='H', x=49, y=265, command=lambda: self.clickButton('H'))
        self.create_button_3(text='P', x=150, y=265, command=lambda: self.clickButton('P'))
        self.create_button_3(text='Sr', x=257, y=265, command=lambda: self.clickButton('Sr'))
        self.create_button_3(text='S', x=49, y=367, command=lambda: self.clickButton('S'))
        self.create_button_3(text='T', x=150, y=367, command=lambda: self.clickButton('T'))
        self.create_button_2(text='I', x=257, y=367, command=lambda: self.clickButton('I'))
        self.create_button_4(text='Rx', x=49, y=469, command=lambda: self.clickButton('Rx'))
        self.create_button_4(text='Ry', x=150, y=469, command=lambda: self.clickButton('Ry'))
        self.create_button_4(text='Rz', x=257, y=469, command=lambda: self.clickButton('Rz'))
        self.create_button_5(text='St', x=49, y=571, command=lambda: self.clickButton('St'))
        self.create_button_5(text='Tt', x=150, y=571, command=lambda: self.clickButton('Tt'))
        self.create_button_5(text='Srt', x=257, y=571, command=lambda: self.clickButton('Srt'))
        self.create_button_6(text='|0>', x=49, y=673, command=lambda: self.clickButton('Ketzero'))
        self.create_button_6(text='|1>', x=150, y=673, command=lambda: self.clickButton('Ketone'))
        self.create_button_6(text='(--', x=257, y=673, command=lambda: self.clearButton())
        self.create_button_7(text='AC', x=49, y=775, command=lambda: self.clearAll())
        self.create_button_7(text='=', x=150, y=775, command=lambda: self.equalTo())
        self.create_button(text='Bloch', x=257, y=775, command=lambda: self.plotBlochSphere())
        self.create_button(text='BarP', x=359, y=673, command=lambda: self.plotBarGraph()) #button for bar graph
        self.result_state = None  # To store the result state vector
        self.quiver_ref = None
        self.scatter_ref = None
        self.bar_fig = None
        self.bar_ax = None
        
        self.fig, self.ax = plot_bloch_sphere()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
       
        self.current_angle_field = None

    
    def add_input_field(self):
        new_input_field = ct.CTkEntry(self.root, width=780, height=75,fg_color=("black"),text_color=("white"),font=("Arial",25),border_color="white")
        new_input_field.place(x=420, y=self.input_y+225)
        new_angle_field = ct.CTkEntry(self.root, width=277,height=75,fg_color=("black"),text_color=("white"),font=("Arial",25),border_color="white")
        new_angle_field.place(x=1200, y=self.input_y+225)
        self.input_y+=100

    def clearButton(self):
        
        if self.input_texts:
            self.input_texts[-1].set("")
        if self.angle_texts:
            self.angle_texts[-1].set("")
    def clearAll(self):
       
        for input_text in self.input_texts:
            input_text.set("")
        for angle_text in self.angle_texts:
            angle_text.set("")
    def on_input_field_focus_in(self, event):
        self.current_input_field = event.widget
    def on_angle_field_focus_in(self, event):
        self.current_angle_field = event.widget

    

    def clickButton(self, button_id):
        button_text = button_id
        self.current_input_field = self.root.focus_get()
        if self.current_input_field:
            self.current_input_field.insert("end", button_text)
        elif self.current_angle_field:
            self.current_angle_field.insert("end", button_text)
        print(f"Button {button_id} clicked: {button_text}")
        self.log(f"Button {button_id} clicked: {button_text}")
            
    def create_button_1(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='#4589ff',
            hover_color='#355ea1',
            corner_radius=13,
            bg_color='black',
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def create_button_2(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='#ff3334',
            hover_color='#b4313a',
            corner_radius=15,
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def create_button_3(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='#955ae9',
            hover_color='#651fff',
            corner_radius=15,
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def create_button_4(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='#ff99cc',
            hover_color='#f319d2',
            corner_radius=15,
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)
    
    def create_button_5(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='#ffff66',
            hover_color='yellow',
            corner_radius=15,
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def create_button_6(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='#35d533',
            hover_color='green',
            corner_radius=15,
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def create_button_7(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='red',
            hover_color='#ff99cc',
            corner_radius=15,
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def create_button(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='black',
            fg_color='#fe7400',
            hover_color='#fee566',
            corner_radius=15,
            border_color='black',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def plotBlochSphere(self):
        if self.result_state is not None:
            state_vector = self.result_state
            self.quiver_ref, self.scatter_ref = update_bloch_sphere(self.ax, state_vector, self.quiver_ref, self.scatter_ref, self.num_frames)
        else:
            print("Error: No valid quantum state to plot")

    def plotBarGraph(self):
        if self.result_state is not None:
            state_vector = self.result_state[:, 0]
            if self.bar_fig is None or self.bar_ax is None:
                self.bar_fig, self.bar_ax = plt.subplots(figsize=(2, 4))
            plot_bar_graph(state_vector, self.bar_fig, self.bar_ax)  # Use the updated function to plot the bar graph in the same figure
            self.bar_fig.show()
        else:
            print("Error: No valid quantum state to plot")

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        with open(self.log_file, "a") as log_file:
            log_file.write(log_message + "\n")
    
    def initialize_log_file(self):
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, "app_log.txt")
        return log_file
    
    def on_closing(self):
        if self.bar_fig:
            plt.close(self.bar_fig)
        self.root.destroy()
        
if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
