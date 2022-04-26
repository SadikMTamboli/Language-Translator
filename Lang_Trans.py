import googletrans
from tkinter import *
from tkinter import ttk

from googletrans import Translator
from PIL import Image, ImageTk

source  = ""
destination = ""
t = ""
# print(googletrans.LANGUAGES)
def comboAction(event):  
    global source
    global destination
    source = combo1.get()  
    destination = combo2.get()
    
    
def Traduct(event):
    
    trans  = Translator()
    global t
    t = ""
    t = T1.get("1.0" , END)
    
    translated = trans.translate(t, src= source, dest= destination)
    T2.delete('1.0', END)
    T2.insert(END , translated.text)
    


root = Tk()
root.geometry("800x300")
root.config(bg='#99FCD6')

l = Label(root, text = "LANGUAGE TRANSLATOR\n",font=('calibre',35, 'bold'),bg='#7CFDEA',justify='center')
l.pack()
l.place(x=460,y=30)
labelChooseLang = Label(root, text = "Source language",font=('calibre',10, 'bold'),bg='#99FCD6') 
labelChooseLang.config(justify='center')
labelChooseLang.pack()
labelChooseLang.place(x = 180+80 , y = 200)
labelLangTraduct = Label(root, text = "Destination language",font=('calibre',10, 'bold'),bg='#99FCD6') 
labelLangTraduct.config(justify='center')
labelLangTraduct.pack()
labelLangTraduct.place(x = 530+400 , y = 200)

img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/Processing/bidirect.png')
resize_image = img.resize((60, 60))
img = ImageTk.PhotoImage(resize_image)
m=Label(root,image=img)
m.config(image=img)
m.pack()

m.place(x=700,y=330)
# m.place(x=900,y=380+130)


languages =['fr' , 'en' , 'es' , 'ar','hi','mr']

combo1 = ttk.Combobox(root, values = languages )
combo1.place(x = 330+80 , y = 200)
combo1.current(0)
combo1.bind("<<ComboboxSelected>>", comboAction)

combo2 = ttk.Combobox(root, values = languages)
combo2.place(x = 690+400 , y = 200)
combo2.current(0)
combo2.bind("<<ComboboxSelected>>", comboAction)


T1 = Text(root )
T1.place(x = 200 , y = 300 , width = 400 , height = 150)
T1.bind("<Return>" , Traduct)

T2 = Text(root)
T2.place(x = 690+200 , y = 300 , width = 400 , height = 150)

root.mainloop()

    
