from tkinter import Tk, Canvas, Entry, StringVar, Frame
from customtkinter import CTkButton
from PIL import Image, ImageTk
from quantum_gates import *

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Tkinter App")
        
        # Create a canvas for the background image
        self.canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=900,
            width=1600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        # Load and place the background image
        image = Image.open(r"quantumsim-main\gui\Quantum Circuit Simulation.png")
        resized_image = image.resize((1635, 850), resample=Image.Resampling.LANCZOS)
        self.image_image_1 = ImageTk.PhotoImage(resized_image)
        self.image_1 = self.canvas.create_image(
            775.0,
            420.0,
            image=self.image_image_1
        )
        
        # Create an input field
        self.inputText = StringVar()
        self.inputFrame = Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="gray", highlightthickness=2)
        self.inputFrame.pack(padx=484, pady=123)
        self.inputField = Entry(self.inputFrame, font=('arial', 25), textvariable=self.inputText, width=50, fg="white", bg="black", bd=0, justify='right')
        self.inputField.pack(ipady=13)
        
        # Create buttons using the create_button method
        self.create_button(text='01', x=49, y=163, command=lambda: self.clickButton(1))
        self.create_button(text='02', x=156, y=163, command=lambda: self.clickButton(2))
        self.create_button(text='03', x=263, y=163, command=lambda: self.clickButton(3))
        self.create_button(text='04', x=49, y=273, command=lambda: self.clickButton(4))
        self.create_button(text='05', x=156, y=273, command=lambda: self.clickButton(5))
        self.create_button(text='06', x=263, y=273, command=lambda: self.clickButton(6))
        self.create_button(text='07', x=49, y=383, command=lambda: self.clickButton(7))
        self.create_button(text='08', x=156, y=383, command=lambda: self.clickButton(8))
        self.create_button(text='09', x=263, y=383, command=lambda: self.clickButton(9))
        self.create_button(text='10', x=49, y=493, command=lambda: self.clickButton(10))
        self.create_button(text='11', x=156, y=493, command=lambda: self.clickButton(11))
        self.create_button(text='12', x=263, y=493, command=lambda: self.clickButton(12))
        self.create_button(text='13', x=49, y=603, command=lambda: self.clickButton(13))
        self.create_button(text='14', x=156, y=603, command=lambda: self.clickButton(14))
        self.create_button(text='15', x=263, y=603, command=lambda: self.clickButton(15))
        self.create_button(text='16', x=49, y=722, command=lambda: self.clickButton(16))
        self.create_button(text='17', x=156, y=722, command=lambda: self.clickButton(17))
        self.create_button(text='18', x=263, y=722, command=lambda: self.clickButton(18))
        self.create_button(text='19', x=484, y=243, command=lambda: self.clickButton(19))
        self.create_button(text='20', x=484, y=334, command=lambda: self.clickButton(20))
    
    def create_button(self, text, x, y, command):
        button = CTkButton(
            master=self.root,
            text=text,
            font=('Bold', 40),
            text_color='#FFFFFF',
            fg_color='black',
            hover_color='#651fff',
            corner_radius=5,
            bg_color='black',
            border_color='#FFFFFF',
            border_width=2,
            anchor='center',
            command=command,
            width=80,
            height=80
        )
        self.canvas.create_window(x, y, window=button)

    def clickButton(self, button_id):
        print(f"Button {button_id} clicked")
        global expression
        self.inputText.set(self.inputText.get()+(str(button_id)))

