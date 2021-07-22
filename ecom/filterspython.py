from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.ttk import *
import cv2
from time import strftime
import tkinter.font


def open_imgC():
    
    x = openfilename()
    img = cv2.imread(x);
    img=cv2.resize(img,(500,500))
    numDownsamples=2
    numBilateralFilter=50
    img_color=img
    for i in range(numDownsamples):
            img_color=cv2.pyrDown(img_color)
    for i in range(numBilateralFilter):
            img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
    for i in range(numDownsamples):
            img_color = cv2.pyrUp(img_color)


	
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 3)	
    img_edge = cv2.adaptiveThreshold(img_blur, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 5, 2)
    (x,y,z) = img_color.shape
    img_edge = cv2.resize(img_edge,(y,x))
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    cv2.imwrite("edge.png",img_edge)
    cimage=cv2.bitwise_and(img_color, img_edge)
    cimage = cv2.copyMakeBorder(cimage, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
    cv2.imshow('Cartonized image',cimage)
    cv2.waitKey(0)



    
def Blur_image():
    x = openfilename()
    image=cv2.imread(x)
    Gaussian = cv2.blur(image, (9, 9))
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
def quit():
    global root
    root.destroy()


root = Tk()
root.title("Filters")
root.geometry('1500x1500')
root.configure(background='yellow')
root.resizable(width = True, height = True)

style = Style()
style.configure('TButton',font =('italic',15,'bold'),background='black',foreground = 'black',width=35,height=10)

btn1= Button(root,text ='Cartoonify ',style='TButton' ,command = open_imgC).grid(padx=500,pady=50)
btn2= Button(root,text ='Blur  ', style='TButton' ,command = Blur_image).grid (padx=500,pady=50)
btn3= Button(root,text ='GrayScale ',style='TButton' , command = Grayscale).grid (padx=500,pady=50)
btn4= Button(root,text ='Quit',style='TButton' , command = quit).grid (padx=500,pady=50)


root.mainloop()
