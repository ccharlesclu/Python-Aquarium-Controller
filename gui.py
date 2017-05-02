from tkinter import *
import tkinter
from PIL import ImageTk
import liveTime

topoffOn = False
wavemakerOn = True

class appTest:

    def __init__(self, master):

        brightVal = tkinter.IntVar()
        
        frame = Frame(master)
        master.columnconfigure(0, weight=1)
        master.title("Reef Controller")

        self.bkgLabel = Label(master)
        bkgImg = PhotoImage(file="C:\\cygwin64\\home\\ccharles\\piMe\\reefbg.png")
        self.bkgLabel.config(image=bkgImg, width = 600, height = 450)
        self.bkgLabel.image = bkgImg
        self.bkgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.titleLabel = Label(master, text="Reef Controller", fg="cyan", font="Verdana 15 bold", bg = 'teal', borderwidth=3, relief=SOLID,
                                pady=5, width=30)
        self.titleLabel.grid(row=1,column=1, columnspan=4, pady=20)

##        self.quitButton = Button(master, text="Quit", command=frame.quit, font="-size 10 -weight bold")
##        self.quitButton.grid(row=1, column=4, pady=20)

        self.timeLabel = Label(master, text='Temperature', font="Verdana 10 bold")
        self.timeLabel.grid(row=2, column=3, columnspan=2)
        
        self.timeDisplay = Label(master, text='', fg="red", font="-weight bold")
        self.timeDisplay.grid(row=3, column=3, columnspan=2, padx=(20,20))

        self.lightsLabel = Label(master, text="Lights", relief=RIDGE, width = 19, font="Verdana 10 bold", bg='#5b5b5b', fg='white',
                                 borderwidth=3, padx=5)
        self.lightsLabel.grid(row=2, column=2)
        self.lightsButton = Button(master, text="OFF",command=self.lightToggle, width=5)
        self.lightsButton.grid(row=3, column=1, padx=(20, 20))
        
        self.brightness = tkinter.Scale(master, from_=0, to=100, font = "-weight bold", length=175, orient="horizontal", variable=brightVal)
        self.brightness.grid(row=3, column=2)

        self.waterButton = Button(master)
        dropButton = PhotoImage(file="C:\\cygwin64\\home\\ccharles\\piMe\\dropButton.png")
        self.waterButton.config(image=dropButton, width = dropButton.width(), command = lambda: self.topoff())
        self.waterButton.image = dropButton
        self.waterButton.grid(row=5, column=1, columnspan=2, pady=(20,0))

        self.waterLabel = Label(master, text="Top-off pump is:\tOFF", width=20, font="-size 10 -weight bold")
        self.waterLabel.grid(row=6, column=1, columnspan=2, padx=20, pady=(5,20))

        self.waveButton = Button(master)
        waveButton = PhotoImage(file="C:\\cygwin64\\home\\ccharles\\piMe\\waveButton.png")
        self.waveButton.config(image=waveButton, width = waveButton.width(), bg='#00ff00', relief=SUNKEN, command= lambda: self.wavemaker())
        self.waveButton.image = waveButton
        self.waveButton.grid(row=5, column=3, pady=(20, 0))

        self.waveLabel = Label(master, text="Wavemaker is:\tON", width=20, font="-size 10 -weight bold")
        self.waveLabel.grid(row=6, column=3, padx=20, pady=(5,20))

        self.Refresher()
        self.scaleChange()

    def showTime(self):
        showTime = liveTime.showTime()

    def lightToggle(self):
        if self.lightsButton["text"] == "Off":
            self.lightsOn(100)
        else:
            self.lightsOff()

    def lightsOn(self, brightness):
        self.brightness.set(brightness)
        self.lightsButton.config(text="ON", relief=SUNKEN, font="-size 10 -weight bold", bg='#00ff00', fg='white')
    def lightsOff(self):
        self.brightness.set(0)
        self.lightsButton.config(text="Off", relief=RAISED, font="-size 10 -weight bold", bg="#bbbbbb", fg='black')
    
    def scaleChange(self):
        if self.brightness.get()==0:
            self.lightsOff()
        else:
            self.lightsOn(self.brightness.get())
        root.after(250,self.scaleChange)

    def topoff(self):
        global topoffOn
        if topoffOn == False:
            onoff = "ON"
            topoffOn = True
            self.waterButton.configure(relief=SUNKEN, bg='#00ff00')
        else:
            topoffOn = False
            onoff = "OFF"
            self.waterButton.configure(relief=RAISED, bg='#f0f0f0')
        self.waterLabel.configure(text="Top-off pump is:\t" + onoff)

    def wavemaker(self):
        global wavemakerOn
        if wavemakerOn == True:
            onoff = "OFF"
            wavemakerOn = False
            self.waveButton.configure(relief=RAISED, bg='#f0f0f0')
        else:
            onoff = "ON"
            wavemakerOn = True
            self.waveButton.configure(relief=SUNKEN, bg='#00ff00')
        self.waveLabel.configure(text="Wavemaker is:\t" + onoff)

    def Refresher(self):
        showTime=liveTime.showTime()
        self.timeDisplay.configure(text=showTime)
        root.after(1000,self.Refresher)

root = Tk()
b = appTest(root)

root.mainloop()
