from tkinter import Tk, Canvas, Entry, StringVar, Frame
from customtkinter import CTkButton
from PIL import Image, ImageTk
from quantum_gates import *
import re

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
        self.create_button(text='X', x=49, y=163, command=lambda: self.clickButton('X'))
        self.create_button(text='Y', x=156, y=163, command=lambda: self.clickButton('Y'))
        self.create_button(text='Z', x=263, y=163, command=lambda: self.clickButton('Z'))
        self.create_button(text='H', x=49, y=273, command=lambda: self.clickButton('H'))
        self.create_button(text='P', x=156, y=273, command=lambda: self.clickButton('P'))
        self.create_button(text='Sr', x=263, y=273, command=lambda: self.clickButton('Sr'))
        self.create_button(text='Tt', x=49, y=383, command=lambda: self.clickButton('Tt'))
        self.create_button(text='Srt', x=156, y=383, command=lambda: self.clickButton('Srt'))
        self.create_button(text='I', x=263, y=383, command=lambda: self.clickButton('I'))
        self.create_button(text='Rx', x=49, y=493, command=lambda: self.clickButton('Rx'))
        self.create_button(text='Ry', x=156, y=493, command=lambda: self.clickButton('Ry'))
        self.create_button(text='Rz', x=263, y=493, command=lambda: self.clickButton('Rz'))
        self.create_button(text='13', x=49, y=603, command=lambda: self.clickButton(13))
        self.create_button(text='14', x=156, y=603, command=lambda: self.clickButton(14))
        self.create_button(text='15', x=263, y=603, command=lambda: self.clickButton(15))
        self.create_button(text='16', x=49, y=722, command=lambda: self.clickButton(16))
        self.create_button(text='17', x=156, y=722, command=lambda: self.clickButton(17))
        self.create_button(text='<--', x=263, y=722, command=lambda: self.clearButton())
        self.create_button(text='AC', x=484, y=243, command=lambda: self.clearAll())
        self.create_button(text='=', x=484, y=334, command=lambda: self.equalTo())
    
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

    def clearAll(self):
        self.inputText.set("")
    
    @staticmethod
    def split_at_uppercase(s):
        split_strings = re.split(r'(?=[A-Z])', s)
        if split_strings and split_strings[0] == '':
            split_strings.pop(0)
        return split_strings
    
    def equalTo(self):
        gates = {"X": X,"Y": Y,"Z": Z,"H": H,
                 "Rx": Rx,"Ry": Ry,"Rz": Rz,"P": P,
                 "Sr": Sr,"St": St,"Tt": Tt,"Srt": Srt,"I": I }
        result=gates['I']()
        print('before iter',result)
        try:
            split_strings=self.split_at_uppercase(self.inputText.get())
            for i in split_strings:
                print('i is',i)
                result=result@gates[f'{i}']()
           
        except:
            result='Error'
        finally:
            print(result)
            self.inputText.set(str(result))

    
        
    def clickButton(self,button_id):
        print(f"Button {button_id} clicked")
        if(self.inputText != 'Error'):
            self.inputText.set(self.inputText.get()+(str(button_id)))
        else:
            self.inputText.set(""+(str(button_id)))

    def clearButton(self):
        self.inputText.set(self.inputText.get()[0:-1])