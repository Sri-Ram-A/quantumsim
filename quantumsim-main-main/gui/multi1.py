from tkinter import Tk, Canvas, Entry, StringVar, Frame
from customtkinter import CTkButton
from PIL import Image, ImageTk
import re 
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
        # Create an input field
        self.inputText = StringVar()
        self.inputFrame = Frame(self.root, width=240, height=50, bd=0, highlightbackground="white", highlightcolor="gray", highlightthickness=2)
        self.inputFrame.place(x=420, y=123)
        self.inputField = Entry(self.inputFrame, font=('arial', 25), textvariable=self.inputText, width=50, fg="white", bg="black", bd=0, justify='left')
        self.inputField.pack(ipady=13)
        #For angle input
        self.angleText = StringVar()
        self.angleFrame = Frame(self.root, width=100, height=30, bd=0, highlightbackground="white", highlightcolor="gray", highlightthickness=2)
        self.angleFrame.place(x=1200, y=123)
        self.angleField = Entry(self.angleFrame, font=('arial', 25), textvariable=self.angleText, width=15, fg="white", bg="black", bd=0)
        self.angleField.pack(ipady=13)
        # Create buttons using the create_button method
        self.input_frames = []  # List to store inputFrame widgets
        self.input_y = 1 # Initial y position for the first inputFrame
        self.angle_frames=[]
        # Create the '+' button
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
        # Setup the Bloch sphere
        self.fig, self.ax = plot_bloch_sphere()

        # Bind the close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    def add_input_field(self):
        # Create a new inputFrame for regular input
        new_input_frame = Frame(self.root, width=240, height=50, bd=0, highlightbackground="white", highlightcolor="gray", highlightthickness=2)
        new_input_frame.place(x=420, y=self.input_y+200)
        #new_input_frame.pack(padx=420, pady=self.input_y)
        self.input_frames.append(new_input_frame)  # Add to list of inputFrames

        # Create a new inputField for regular input
        new_input_text = StringVar()
        new_input_field = Entry(new_input_frame, font=('Arial', 25), textvariable=new_input_text, width=50, fg="white", bg="black", bd=0, justify='left')
        new_input_field.pack(ipady=13)

        # Create a new angleFrame for angle input
        new_angle_frame = Frame(self.root, width=100, height=30, bd=0, highlightbackground="white", highlightcolor="gray", highlightthickness=2)
        new_angle_frame.place(x=1200, y=self.input_y+200)  # Adjust padx as needed for alignment
        self.angle_frames.append(new_angle_frame)  # Add to list of inputFrames

        # Create a new angleField for angle input
        new_angle_text = StringVar()
        new_angle_field = Entry(new_angle_frame, font=('Arial', 25), textvariable=new_angle_text, width=15, fg="white", bg="black", bd=0)
        new_angle_field.pack(ipady=13)
        
    
        self.input_y += 80

        
    def initialize_log_file(self):
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        filename = f"quantumsim-main-main\\history\\{current_date}.txt"
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                file.write(f"quantumsim-main-main\\history\\{current_date}\n")
        return filename

    def log(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        with open(self.log_file, "a") as file:
            file.write(f"[{current_time}] {message}\n")

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

    def clearAll(self):
        self.inputText.set("")
        self.angleText.set("")

    def clickButton(self, button_id):
        print(f"Button {button_id} clicked")
        self.log(f"Button {button_id} clicked")
        if self.inputText.get() != 'Error':
            self.inputText.set(self.inputText.get() + str(button_id))
        else:
            self.inputText.set("" + str(button_id))
        if button_id in ['Rx', 'Ry', 'Rz', 'P']:
            self.angleText.set('Degree?')

    def clearButton(self):
        self.inputText.set(self.inputText.get()[0:-1])

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
    
    @staticmethod
    def split_at_uppercase(s):
        split_strings = re.split(r'(?=[A-Z])', s)
        if split_strings and split_strings[0] == '':
            split_strings.pop(0)
        return split_strings

    def equalTo(self):
        gates = {"X": X, "Y": Y, "Z": Z, "H": H,
                 "Rx": Rx, "Ry": Ry, "Rz": Rz, "P": P,
                 "Sr": Sr, "Tt": Tt, "Srt": Srt, "I": I,
                 "Ketzero": Ketzero, "Ketone": Ketone,'S':S,'T':T,'St':St}
        result = gates['I']()
        print('before iter', result)
        
        try:
            j = 0
            split_non_matrix = self.split_at_uppercase(self.inputText.get())
            angle_list = self.angleText.get().split(",")
            for i in split_non_matrix:
                if i in ['Rx', 'Ry', 'Rz', 'P']:
                    angle = angle_list[j]
                    j += 1
                    if not angle:
                        raise ValueError("Angle input is required for rotation gates.")
                    result = result @ gates[i](int(angle))
                else:
                    result = result @ gates[i]()
                print('i is', i)
            self.result_state = result  # Store the result state
            self.log(f"Calculation: {self.inputText.get()}")
            self.log(f"Angles: {self.angleText.get()}")
            self.log(f"Result: {result}")
            self.log(f"Probability of |0> {(abs(result[0]))**2}")
            self.log(f"Probability of |1> {(abs(result[1]))**2}")
        except Exception as e:
            result = f'Error: {e}'
            self.result_state = None
            self.log(f"Error during calculation: {e}")
        finally:
            print(result)
            self.inputText.set(str(result))
            
    def equivalent(self):
        pass

    def on_closing(self):
        self.log(f"\n{'='*20} End of Calculations {'='*20}\n")
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
