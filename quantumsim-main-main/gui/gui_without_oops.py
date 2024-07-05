from pathlib import Path
from PIL import Image,ImageTk

#from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame
from customtkinter import *

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"quantumsim-main\Quantum Circuit Simulation.png")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1500x800")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 900,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
image = Image.open(r"quantumsim-main\Quantum Circuit Simulation.png")
resized_image = image.resize((1550, 840), resample=Image.Resampling.LANCZOS)
canvas.place(x = 0, y = 0)
image_image_1 = ImageTk.PhotoImage(resized_image)
image_1 = canvas.create_image(
    775.0,
    420.0,
    image=image_image_1
)


inputText=StringVar()
inputFrame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="gray",
                    highlightthickness=2)
inputFrame.pack(padx=484,pady=123)
inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50,fg="white", bg="black", bd=0,
                    justify=RIGHT)
inputField.pack(ipady=13)
def buttons():
    button_1 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_1 clicked"),
        width=80,
        height=80
    ).place(
        x=49,
        y=163
    )

    # entry= CTkEntry(
    #     master=window,
    #     width=632,
    #     height=80,
    #     corner_radius=2,
    #     text_color='white'
    #     #fg_color='
    
    # )
    # entry.place(
    #     x=484.0,
    #     y=123.0  
    # )  

    button_3 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_3 clicked"),
        width=80,
        height=80
    )
    button_3.place(
        x=49.0,
        y=273.0
    )

    button_4 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_4 clicked"),
        width=80,
        height=80
    )
    button_4.place(
        x=49.0,
        y=383.0
    )

    button_5 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_5 clicked"),
        width=80,
        height=80
    )
    button_5.place(
        x=49.0,
        y=493.0
    )

    button_6 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_6 clicked"),
        width=80,
        height=80
    )
    button_6.place(
        x=49.0,
        y=603.0
    )

    button_7 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_7 clicked"),
        width=80,
        height=80
    )

    button_7.place(
        x=49.0,
        y=722.0
    )

    button_8 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_8 clicked"),
        width=80,
        height=80
    )
    button_8.place(
        x=156.0,
        y=163.0
    )

    button_9 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_9 clicked"),
        width=80,
        height=80
    )
    button_9.place(
        x=156.0,
        y=273.0
    )

    button_10 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_10 clicked"),
        width=80,
        height=80
    )
    button_10.place(
        x=156.0,
        y=383.0
    )

    button_11 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_11 clicked"),
        width=80,
        height=80
    )
    button_11.place(
        x=156.0,
        y=493.0
    )

    button_12 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_12 clicked"),
        width=80,
        height=80
    )
    button_12.place(
        x=156.0,
        y=603.0
    )

    button_13 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_13 clicked"),
        width=80,
        height=80
    )
    button_13.place(
        x=156.0,
        y=722.0
    )

    button_14 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_14 clicked"),
        width=80,
        height=80
    )
    button_14.place(
        x=263.0,
        y=163.0
    )

    button_15 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_15 clicked"),
        width=80,
        height=80
    )
    button_15.place(
        x=263.0,
        y=273.0
    )

    button_16 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_16 clicked"),
        width=80,
        height=80
    )
    button_16.place(
        x=263.0,
        y=383.0
    )

    button_17 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_17 clicked"),
        width=80,
        height=80
    )
    button_17.place(
        x=263.0,
        y=493.0
    )

    button_18 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_18 clicked"),
        width=135,
        height=61
    )
    button_18.place(
        x=484.0,
        y=334.0
    )

    button_19 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_19 clicked"),
        width=80,
        height=80
    )
    button_19.place(
        x=263.0,
        y=603.0
    )

    button_20 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_20 clicked"),
        width=80,
        height=80
    )
    button_20.place(
        x=263.0,
        y=722.0
    )

    button_21 = CTkButton(
        master=window,
        text='H',
        font=('Bold',20),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        #corner_radius=100,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_21 clicked"),
        width=40,
        height=40
    )
    button_21.place(
        x=1036.0,
        y=233.0
    )

    button_22 = CTkButton(
        master=window,
        text='H',
        font=('Bold',40),
        text_color='#FFFFFF',
        fg_color='transparent',
        hover_color='#651fff',
        corner_radius=2,
        bg_color='black',
        border_color='#FFFFFF',
        border_width=2,
        anchor='center',
        command=lambda: print("button_22 clicked"),
        width=135,
        height=61
    )
    button_22.place(
        x=484.0,
        y=243.0
    )
buttons()



def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)


window.resizable(True, True)
window.mainloop()
