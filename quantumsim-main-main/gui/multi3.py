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
        self.input_field_list=[]
        self.angle_field_list=[]
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
        input_field = ct.CTkEntry(self.root, width=780, height=75,fg_color=("black"),text_color=("white"),font=("Arial",25),border_color="white")
        input_field.place(x=420, y=self.input_y+225)
        angle_field = ct.CTkEntry(self.root, width=277,height=75,fg_color=("black"),text_color=("white"),font=("Arial",25),border_color="white")
        angle_field.place(x=1200, y=self.input_y+225)
        self.input_y+=100
        self.input_field_list.append(input_field)
        self.angle_field_list.append(angle_field)

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
    @staticmethod
    def convert_list(lst):
        result = []
        for item in lst:
            split_strings = re.split(r'(?=[A-Z])', item)
            if split_strings and split_strings[0] == '':
                split_strings.pop(0)
            result.append(split_strings)
        return result
     
    def equalTo(self):
        input_list = [i.get() for i in self.input_field_list]
        angle_list = [i.get().split(',') for i in self.angle_field_list]

        # Flatten angle_list manually
        angle_list_flat = [angle for sublist in angle_list for angle in sublist]

        input_matrix = self.convert_list(input_list)  # This is a matrix

        print(input_matrix)
        print(angle_list_flat)

        gates = {"X": X, "Y": Y, "Z": Z, "H": H,
                 "Rx": Rx, "Ry": Ry, "Rz": Rz, "P": P,
                 "Sr": Sr, "Tt": Tt, "Srt": Srt, "I": I,
                 "Ketzero": Ketzero, "Ketone": Ketone, 'S': S, 'T': T, 'St': St}

        angle_index = 0
        for i in range(len(input_matrix)):
            for j in range(len(input_matrix[i])):
                gate = input_matrix[i][j]
                if gate in ['Rx', 'Ry', 'Rz', 'P']:
                    if angle_index < len(angle_list_flat):
                        angle = angle_list_flat[angle_index]
                        angle_index += 1
                        if angle:
                            input_matrix[i][j] = gates[gate](int(angle))
                        else:
                            raise ValueError(f"Angle is required for gate {gate}")
                    else:
                        raise ValueError("Not enough angles provided")
                else:
                    input_matrix[i][j] = gates[gate]()

        # Calculate tensor products column-wise
        tensor_input = []
        num_columns = len(input_matrix[0])
        for col in range(num_columns):
            col_tensor_product = input_matrix[0][col]
            for row in range(1, len(input_matrix)):
                col_tensor_product = np.kron(col_tensor_product, input_matrix[row][col])
            tensor_input.append(col_tensor_product)

        # Calculate the matrix product of reversed tensor_input
        pre_matrix = tensor_input[-1]
        for mat in reversed(tensor_input[:-1]):
            pre_matrix = pre_matrix @ mat

        # printing the final result
        print(pre_matrix)
        ketzero=np.zeros((2**(len(input_matrix)),1))
        ketzero[0]=1
        self.result_state=pre_matrix@ketzero
        print(self.result_state)
        print(self.result_state.size)
        return self.result_state

        
           
if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
