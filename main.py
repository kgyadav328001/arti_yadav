from tkinter import*
from tkinter.messagebox import*
import math as m
from audio_helper import PlayAudio
import threading
# some useful variables
font=('verdana',12,'bold')
ob=PlayAudio()


# important functions
def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)

def all_clear():
    textField.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)
    t=threading.Thread(target=ob.speak,args=(text,))
    t.start()

    if text=='x':
        textField.insert(END,"*")
        return


    if text == '=':
      try:
          ex=textField.get()
          anser=eval(ex)
          textField.delete(0,END)
          textField.insert(0,anser)
      except Exception as e:
          print("Error..",e)
          showerror("Error",e)
      return;
    textField.insert (END,text)

# creating a window
window = Tk()
window.title('My calculator')
window.geometry('600x640')
# picture label
pic = PhotoImage(file='img/arti.png')
headingLabel = Label(window,image=pic)
headingLabel.pack(side=TOP,pady=2)
# heading label
heading = Label(window,text='My calculator', font=font,underline=0)
heading.pack(side=TOP)
#textfield
textField=Entry(window,font=font,justify=CENTER)
textField.pack(side=TOP,pady=10,fill=X,padx=10)
#buttons
buttonFrame =Frame(window)
buttonFrame.pack(side=TOP,padx=10)

# adding button
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn= Button(buttonFrame,text=str(temp),font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='white')
        btn.grid(row=i,column=j,padx=3,pady=3)
        temp = temp + 1
        btn.bind('<Button-1>',click_btn_function)
zeroBtn = Button(buttonFrame,text= '0',font=font,width=5,relief='ridge',activebackground= 'yellow',activeforeground='white')
zeroBtn.grid(row=3,column=0,padx=3,pady=3)
dotBtn = Button(buttonFrame,text= '.',font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='white')
dotBtn.grid(row=3,column=1,padx=3,pady=3)
equalBtn = Button(buttonFrame,text= '=',font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='white')
equalBtn.grid(row=3,column=2,padx=3,pady=3)

plusBtn = Button(buttonFrame,text= '+',font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='white')
plusBtn.grid(row=0,column=3,padx=3,pady=3)
minusBtn = Button(buttonFrame,text= '-',font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='white')
minusBtn.grid(row=1,column=3,padx=3,pady=3)
multBtn = Button(buttonFrame,text= 'x',font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='white')
multBtn.grid(row=2,column=3,padx=3,pady=3)
divideBtn = Button(buttonFrame,text= '/',font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='white')
divideBtn.grid(row=3,column=3,padx=3,pady=3)
clearBtn = Button(buttonFrame,text='<---',font=font,width=10,relief='ridge',activebackground='yellow',activeforeground='white',command=clear)
clearBtn.grid(row=4,column=0,columnspan=2,padx=3,pady=3)
allclearBtn = Button(buttonFrame,text='AC',font=font,width=10,relief='ridge',activebackground='yellow',activeforeground='white',command=all_clear)
allclearBtn.grid(row=4,column=2,columnspan=2,padx=3,pady=3)

#binding button
plusBtn.bind('<Button-1>',click_btn_function)
minusBtn.bind('<Button-1>',click_btn_function)
multBtn.bind('<Button-1>',click_btn_function)
divideBtn.bind('<Button-1>',click_btn_function)
zeroBtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)
def enterclick(event):
    print('hi')
    e=Event()
    e.widget=equalBtn
    click_btn_function(e)
textField.bind('<Return>',enterclick)
#####################################################
# second vedio fuun
scFrame = Frame(window)

sqrtButn=Button(scFrame,text='√',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
sqrtButn.grid(row=0,column=0)
powButn=Button(scFrame,text='‸',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
powButn.grid(row=0,column=1)
factButn=Button(scFrame,text='x!',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
factButn.grid(row=0,column=2)
radButn=Button(scFrame,text='toRad',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
radButn.grid(row=0,column=3)
degButn=Button(scFrame,text='todeg',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
degButn.grid(row=1,column=0)
sinButn=Button(scFrame,text='sinѲ',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
sinButn.grid(row=1,column=1)
cosButn=Button(scFrame,text='cosѲ',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
cosButn.grid(row=1,column=2)
tanButn=Button(scFrame,text='tanѲ',font=font,width=5,relief= 'ridge',activebackground='yellow',activeforeground='white')
tanButn.grid(row=1,column=3)



normalcalc =True
def calculate_sc(event):
    print('btn...')
    btn=event.widget
    text=btn['text']
    print(text)
    ex=textField.get()
    answer=''
    if text=='todeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))

    elif text=='toRad':
        print('radian')
        answer=str(m.radian(float(ex)))
    elif text=='x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text=='sinѲ':
       print("cal sin")
       answer = str(m.sin(m.radians(int(ex))))
    elif text=='cosѲ':
       print("cal cos")
       answer = str(m.cos(m.radians(int(ex))))
    elif text=='tanѲ':
       print("cal tanѲ")
       answer = str(m.tan(m.radians(int(ex))))
    elif text=='√':
       print("sqrt")
       answer = m.sqrt(int(ex))
    elif text == '‸':
       print('pow')
       base,pow=ex.split(',')
       print(base)
       print(pow)
       answer=m.pow(int(base),int(pow))

    textField.delete(0, END)
    textField.insert(0,answer)

def sc_click():
    global normalcalc
    if normalcalc:
           #sc...
           buttonFrame.pack_forget()
           # add sc frame
           scFrame.pack(side=TOP,pady=5)
           buttonFrame.pack(side=TOP)
           window.geometry('600x720')

           print("show sc")
           normalcalc = False
    else:
        print('show normal')
        scFrame.pack_forget()
        window.geometry('600x640')
        normalcalc=True
#end function
#binding sc button
sqrtButn.bind("<Button-1>", calculate_sc)
powButn.bind("<Button-1>",calculate_sc)
factButn.bind("<Button-1>",calculate_sc)
radButn.bind("<Button-1>",calculate_sc)
degButn.bind("<Button-1>",calculate_sc)
sinButn.bind("<Button-1>",calculate_sc)
cosButn.bind("<Button-1>",calculate_sc)
tanButn.bind("<Button-1>",calculate_sc)




fontMenu= ('',15)
menubar=Menu(window,font=fontMenu)

mode=Menu(menubar,font= fontMenu,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",command=sc_click)

menubar.add_cascade(label="mode",menu=mode)

window.config(menu = menubar)





window.mainloop()


