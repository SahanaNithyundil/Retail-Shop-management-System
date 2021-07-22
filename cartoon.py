from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.ttk import *
import cv2
from time import strftime

def open_imgC():
    x = openfilename()
    img = cv2.imread(x);
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel=Label(root, image = img)
    panel.image = img
    panel.grid(row = 2)
def Blur_image():
    x = openfilename()
    image=cv2.imread(x)
    Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
    image = cv2.copyMakeBorder(Gaussian, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
    cv2.imshow('Gaussian Blurring', image)
    cv2.waitKey(0)
def open_imgD():
    x = openfilename()
    img = Image.open(x)
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel=Label(root, image = img)
    panel.image = img
    panel.grid(row = 2)
def Grayscale():
    x = openfilename()
    img =cv2.imread(x)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = cv2.copyMakeBorder(gray_image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
    cv2.imshow('Grayscale', image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
def openfilename():
    filename = filedialog.askopenfilename(title ='"pen')
    return filename



root = Tk()
root.title("Filters")
root.geometry('1500x1500')
root.configure(background='blue')
root.resizable(width = True, height = True)

style = Style()
style.configure('TButton', font =('calibri', 25, 'bold'),background='black',foreground = 'red',width=25,height=10)

btn1= Button(root,text ='Cartoonify Your image',style='TButton' ,command = open_imgC).grid(padx=750,pady=100)
btn2= Button(root,text ='Blur Your image', style='TButton' ,command = Blur_image).grid (padx=750,pady=100)
btn3= Button(root,text ='GrayScale Your image',style='TButton' , command = Grayscale).grid (padx=750,pady=100)
btn4= Button(root,text ='Dust free image',style='TButton' , command = open_imgD).grid (padx=750,pady=100)


root.mainloop()
