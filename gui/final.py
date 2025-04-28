from tkinter import Tk, Canvas
from customtkinter import CTkButton
import customtkinter as ct
from PIL import Image, ImageTk
import re
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import matplotlib as mpl

#custom imports
from quantum_gates import *
from bloch import plot_bloch_sphere, update_bloch_sphere
from probability_bargraph import *


plt.ion()
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
        image_path ="Quantum Circuit Simulation.png"
        image = Image.open(image_path)
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
        self.create_button(text="?", x=257, y=755, command=self.show_help_window)
        self.create_button('+', x=364, y=163, command=self.add_input_field)
        self.create_button_1(text='X', x=49, y=163, command=lambda: self.clickButton('X'))
        self.create_button_1(text='Y', x=150, y=163, command=lambda: self.clickButton('Y'))
        self.create_button_1(text='Z', x=257, y=163, command=lambda: self.clickButton('Z'))
        self.create_button_2(text='H', x=49, y=250, command=lambda: self.clickButton('H'))
        self.create_button_3(text='P', x=150, y=250, command=lambda: self.clickButton('P'))
        self.create_button_3(text='Sr', x=257, y=250, command=lambda: self.clickButton('Sr'))
        self.create_button_3(text='S', x=49, y=350, command=lambda: self.clickButton('S'))
        self.create_button_3(text='T', x=150, y=350, command=lambda: self.clickButton('T'))
        self.create_button_2(text='I', x=257, y=350, command=lambda: self.clickButton('I'))
        self.create_button_4(text='Rx', x=49, y=450, command=lambda: self.clickButton('Rx'))
        self.create_button_4(text='Ry', x=150, y=450, command=lambda: self.clickButton('Ry'))
        self.create_button_4(text='Rz', x=257, y=450, command=lambda: self.clickButton('Rz'))
        self.create_button_5(text='St', x=49, y=555, command=lambda: self.clickButton('St'))
        self.create_button_5(text='Tt', x=150, y=555, command=lambda: self.clickButton('Tt'))
        self.create_button_5(text='Srt', x=257, y=555, command=lambda: self.clickButton('Srt'))
        self.create_button_6(text='|0>', x=49, y=655, command=lambda: self.clickButton('Ketzero'))
        self.create_button_6(text='|1>', x=150, y=655, command=lambda: self.clickButton('Ketone'))
        #self.create_button_6(text='(--', x=257, y=655, command=lambda: self.clearButton())
        #self.create_button_7(text='AC', x=49, y=755, command=lambda: self.clearAll())
        self.create_button_7(text='=', x=150, y=755, command=lambda: self.equalTo())
        self.create_button(text='(O)', x=257, y=655, command=lambda: self.plotBlochSphere())
        self.create_button(text='p(x)', x=49, y=755, command=lambda: self.plotBarGraph(self.result_state)) #button for bar graph
        self.result_state = None  # To store the result state vector
        self.quiver_ref = None
        self.scatter_ref = None
        self.bar_fig = None
        self.bar_ax = None    
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.current_input_field = None
        self.current_angle_field = None
    def on_closing(self):
        self.log(f"\n{'='*20} End of Calculations {'='*20}\n")
        self.root.destroy()
    
    def add_input_field(self):
        input_field = ct.CTkEntry(self.root, width=780, height=75,fg_color=("black"),text_color=("white"),font=("Arial",25),border_color="white",corner_radius=15)
        input_field.place(x=420, y=self.input_y+100)
        angle_field = ct.CTkEntry(self.root, width=277,height=75,fg_color=("black"),text_color=("white"),font=("Arial",25),border_color="white",corner_radius=15)
        angle_field.place(x=1200, y=self.input_y+100)
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
 
    def clickButton(self, button_id):
        button_text = button_id
        # Get the currently focused widget
        focused_widget = self.root.focus_get()

        if focused_widget in self.input_field_list:
            focused_widget.insert("end", button_text)
        elif focused_widget in self.angle_field_list:
            focused_widget.insert("end", button_text)
        else:
            # If no field is focused, maybe print a message or focus the first input field
            print("Please select an input field first")
            if self.input_field_list:  # if there are input fields
                self.input_field_list[0].focus_set()
                self.input_field_list[0].insert("end", button_text)
            
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
        if self.result_state is not None and len(self.result_state) == 2:
            self.fig, self.ax = plot_bloch_sphere()
            state_vector = self.result_state
            self.quiver_ref, self.scatter_ref = update_bloch_sphere(self.ax, state_vector, self.quiver_ref, self.scatter_ref, self.num_frames)
        else:
            def kill_window():
                new_window.destroy()

            new_window=ct.CTkToplevel(self.root)
            new_window.transient(self.root)
            new_window.title("ERROR!")
            new_window.geometry("475x150")
            new_window.resizable(0,0)
            new_window.configure(fg_color="BLACK")
            label = ct.CTkLabel(new_window, text="Error: No valid quantum state to plot", fg_color="transparent",font=("Times new roman",25,"bold"),text_color=("red"),corner_radius=15,anchor="nw")
            label.grid(row=1, column=1, pady=10,padx=2, sticky="w")
            try_again_button = ct.CTkButton(new_window, text="Try Again", command=kill_window, width=450, height=80 ,font=("Times new roman", 20, "bold"),corner_radius=18,border_width=3,border_color=("black"))
            try_again_button.grid(row=2, column=1, columnspan=2,padx=10, pady=10,sticky="w")
            print("Error: No valid quantum state to plot")

    def plotBarGraph(self, prob):
        modulus = (np.abs(prob))**2
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x, y = np.meshgrid(np.arange(modulus.shape[1]), np.arange(modulus.shape[0]))

        cmap = mpl.colormaps['plasma']  # options:'viridis', 'plasma', 'coolwarm'
        modulus_flat = modulus.ravel()
        x_flat = x.ravel()
        y_flat = y.ravel()

        for i in range(len(modulus_flat)):
            color = cmap(modulus_flat[i])
            ax.bar3d(x_flat[i], y_flat[i], 0, 1, 1, modulus_flat[i], color=color,edgecolor='k')

        ax.set_title('3D Bar Graph of probabilities')
        ax.set_xticks([])
        num_bars = modulus.shape[0]
        y_tick_labels = [format(i, 'b').zfill(int(np.log2(num_bars))) for i in range(num_bars)]
        ax.set_yticks(np.arange(num_bars)+0.5)
        if len(modulus_flat)>=16:
            ax.set_yticklabels(y_tick_labels,rotation=90, ha='center')
        else:
            ax.set_yticklabels(y_tick_labels,rotation=0, ha='center')
        #ax.set_ylabel('Qubits')
        ax.set_zlabel('Probabilities')
        ax.view_init(elev=30, azim=45)

        plt.show(block=True)

    def initialize_log_file(self):
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        directory = os.path.join("quantumsim-main-main","history")
        filename = f"{directory}\\{current_date}.txt"

        # 🛠️ Make sure the 'history' directory exists
        os.makedirs(directory, exist_ok=True)

        if not os.path.exists(filename):
            with open(filename, "w") as file:
                file.write(f"{filename}\n")
        return filename

    def log(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        with open(self.log_file, "a") as file:
            file.write(f"[{current_time}] {message}\n")
    
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
        angle_list_flat=[item for item in angle_list_flat if item] #To remove empty strings

        input_matrix = self.convert_list(input_list)  # This is a matrix
        self.log(f"Input Matrices are\n{input_matrix}")
        self.log(f"Input Angles are\n{angle_list_flat}")

        print("Input Matrix:", input_matrix)
        print("Angle List Flat:", angle_list_flat)

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

        #print("Transformed Input Matrix:", input_matrix)

        # Calculate tensor products column-wise
        tensor_input = []
        num_columns = len(input_matrix[0])
        for col in range(num_columns):
            col_tensor_product = input_matrix[0][col]
            for row in range(1, len(input_matrix)):
                try:
                    col_tensor_product = np.kron(col_tensor_product, input_matrix[row][col])
                except IndexError as e:
                    print(f"IndexError at row {row}, column {col}: {e}")
                    print("Input Matrix Shape:", len(input_matrix), len(input_matrix[0]))
                    return
            tensor_input.append(col_tensor_product)

        # Calculate the matrix product of reversed tensor_input
        pre_matrix = tensor_input[-1]
        for mat in reversed(tensor_input[:-1]):
            pre_matrix = pre_matrix @ mat

        # printing the final result
        #print(pre_matrix)
        ketzero = np.zeros((2 ** (len(input_matrix)), 1))
        ketzero[0] = 1
        self.result_state = pre_matrix @ ketzero
        print(self.result_state)
        print(self.result_state.size)
        self.log(f"Resultant Matrix\n{self.result_state}\nNumber of qubits:{self.result_state.size}")
        return self.result_state
    def show_help_window(self):
        new_window = ct.CTkToplevel(self.root)
        new_window.transient(self.root)
        new_window.title("Help Menu")
        new_window.geometry("800x600")
        new_window.resizable(0, 0)
        new_window.configure(bg_color="darkgray")
        new_window.configure(fg_color="BLACK")

        gate_descriptions = {
            "X": "Pauli X Gate: Flips the state of the qubit (|0> to |1> and vice versa).",
            "Y": "Pauli Y Gate: Rotates the qubit state around the Y axis of the Bloch sphere.",
            "Z": "Pauli Z Gate: Rotates the qubit state around the Z axis of the Bloch sphere.",
            "H": "Hadamard Gate: Puts the qubit in a superposition of |0> and |1>.",
            "Rx": "Rotation Gate around X axis. Requires an angle parameter.",
            "Ry": "Rotation Gate around Y axis. Requires an angle parameter.",
            "Rz": "Rotation Gate around Z axis. Requires an angle parameter.",
            "S": "Phase Gate: Applies a phase shift of pi/2 radians about Z axis.",
            "T": "Phase Gate: Applies a phase shift of pi/4 radians about Z axis.",
            "P": "Phase Gate: Applies an arbitrary phase shift (requires an angle).",
            "Sr":"Square Root of X Gate.",
            "St":"Hermitian Conjugate of S Gate.",
            "Tt":"Hermitian Conjugate of T Gate.",
            "Srt":"Square Root of X Gate followed by its Hermitian Conjugate.",
            "I": "Identity Gate: Does nothing (leaves the qubit state unchanged).",
            "|0>":"Represents the |0> state (initial state with all probability).",
            "|1>":"Represents the |1> state (opposite to |0> state).",
            "=":"Calcuates the final state that is obtained after performing the \noperations to the qubits.",
            "(O)":"It plots a Bloch sphere🌐, for visualization of change in states of a single qubit.",
            "p(x)":"It plots a 3D Bar graph, which represents probabilites of \neach qubit state."
        }

        canvas = ct.CTkCanvas(new_window, bg="black")
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ct.CTkScrollbar(new_window, orientation="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        frame = ct.CTkFrame(canvas, bg_color="black", fg_color="BLACK")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        y_pos = 20
        for gate, description in gate_descriptions.items():
            if gate in ["X", "Y", "Z"]:
                label = ct.CTkLabel(
                    frame,
                    text=f"{gate}: {description}",
                    fg_color="black",
                    text_color="#4589ff",
                    font=("Times new roman", 20,"bold"),
                    justify="left",
                    anchor="nw",
                    wraplength=700
                )
            elif gate in ["H", "I"]:
                label = ct.CTkLabel(
                    frame,
                   text=f"{gate}: {description}",
                    fg_color="black",
                    text_color="#ff3334",
                    font=("Times new roman", 20,"bold"),
                    justify="left",
                    anchor="nw",
                    wraplength=700
                )
            elif gate in ["Rx", "Ry","Rz"]:
                label = ct.CTkLabel(
                    frame,
                    text=f"{gate}: {description}",
                    fg_color="black",
                    text_color="#ff99cc",
                    font=("Times new roman", 20,"bold"),
                    justify="left",
                    anchor="nw",
                    wraplength=700
                )
            elif gate in ["St", "Tt", "Srt"]:
                label = ct.CTkLabel(
                    frame,
                    text=f"{gate}: {description}",
                    fg_color="black",
                    text_color="#ffff66",
                    font=("Times new roman", 20,"bold"),
                    justify="left",
                    anchor="nw",
                    wraplength=700
                )
            elif gate in ["|0>", "|1>", "(--"]:
                label = ct.CTkLabel(
                    frame,
                    text=f"{gate}: {description}",
                    fg_color="black",
                    text_color="#35d533",
                    font=("Times new roman", 20,"bold"),
                    justify="left",
                    anchor="nw",
                    wraplength=700
                )        
            elif gate in ["P", "S", "Sr", "T"]:
                label = ct.CTkLabel(
                    frame,
                    text=f"{gate}: {description}",
                    fg_color="black",
                    text_color="#955ae9",
                    font=("Times new roman", 20,"bold"),
                    justify="left",
                    anchor="nw",
                    wraplength=700
                )
            else:
                label = ct.CTkLabel(
                    frame,
                    text=f"{gate}: {description}",
                    fg_color="black",
                    text_color="#fe7400",
                    font=("Times new roman", 20,"bold"),
                    justify="left",
                    anchor="nw",
                    wraplength=700
                )
            label.pack(pady=10)

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        new_window.mainloop()
           
if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()