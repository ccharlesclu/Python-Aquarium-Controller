from tkinter import *
import tkinter
import math
#from PIL import ImageTk
import tempTest
import lights
import Dimmer
import lightningSync2
import colorMess
import RPi.GPIO as GPIO
from Device import Device
from RelayDevice import RelayDevice

wavemaker = RelayDevice(5, False)
topoff = RelayDevice(19, False)
led = Dimmer.Dimmer(4)
led2 = Dimmer.Dimmer(17)
led3 = Dimmer.Dimmer(22)

topoffOn = False
wavemakerOn = False
heaterOn = 'ON'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class appTest:

    def __init__(self, master):

        master.protocol('WM_DELETE_WINDOW', self.onExit)

        brightVal = tkinter.IntVar()
        
        frame = Frame(master)
        master.columnconfigure(0, weight=1)
        master.title("Reef Controller")
        master.resizable(0,0)

        self.bkgLabel = Label(master)
        bkgImg = PhotoImage(file="/home/pi/ledtest/reefbg.png")
        self.bkgLabel.config(image=bkgImg, width = 600, height = 450)
        self.bkgLabel.image = bkgImg
        self.bkgLabel.place(x=0, y=0, relwidth=1, relheight=1)


        ## TITLE
        self.titleLabel = Label(master, text="Reef Controller", fg="cyan", font="Verdana 15 bold", bg = 'teal', borderwidth=3, relief=SOLID,
                                pady=5, width=30)
        self.titleLabel.grid(row=1,column=1, columnspan=4, pady=20)

        ## TEMPERATURE
        self.tempLabel = Label(master, text='Temperature', relief=RIDGE, width = 22, font="Verdana 10 bold", bg='#5b5b5b', fg='white',
                                 borderwidth=3, padx=10)
        self.tempLabel.grid(row=2, column=3, columnspan=2)
        
        self.tempDisplay = Label(master, text='', fg="red", width=9, font="-size 22 -weight bold", borderwidth=2, relief=SOLID, padx=10)
        self.tempDisplay.grid(row=3, column=3, columnspan=2, padx=20)

        self.heaterLabel = Label(master, text="Heater is:   " + heaterOn, font="-size 10 -weight bold")
        self.heaterLabel.grid(row=4, column=3, padx=(40,0))

        ## LIGHTS
        self.lightsLabel = Label(master, text="Lights", relief=RIDGE, width = 22, font="Verdana 10 bold", bg='#5b5b5b', fg='white',
                                 borderwidth=3, padx=10)
        self.lightsLabel.grid(row=2, column=1, padx=(20,0))
        self.lightsButton = Button(master, text="OFF",command=self.lightToggle, width=5)
        self.lightsButton.grid(row=4, column=1, padx=(20, 0))
        
        self.brightness = tkinter.Scale(master, from_=0, to=100, font = "-weight bold", length=175, orient="horizontal", variable=brightVal,
                                        command=self.changeDim)
        self.brightness.grid(row=3, column=1, padx=(20,0))

        ## TOP-OFF
        self.topoffButton = Button(master)
        dropButton = PhotoImage(file="/home/pi/ledtest/dropButton.png")
        self.topoffButton.config(image=dropButton, width = dropButton.width(), command= self.topoff_switch)
        self.topoffButton.image = dropButton
        self.topoffButton.grid(row=6, column=1, columnspan=2, pady=(20,0))

        self.topoffLabel = Label(master, text="Top-off pump is:   Off", width=20, font="-size 10 -weight bold")
        self.topoffLabel.grid(row=7, column=1, columnspan=2, pady=(5,20))

        ## STORM
        self.stormButton = Button(master)
        stormImg = PhotoImage(file="/home/pi/ledtest/storm.png")
        self.stormButton.config(image=stormImg, width = stormImg.width(), bg='#415263', relief=SOLID, borderwidth=2,
                                command= lambda: self.storm())
        self.stormButton.image = stormImg
        self.stormButton.grid(row=5, column=2)

        ## WAVEMAKER
        self.waveButton = Button(master)
        waveButton = PhotoImage(file="/home/pi/ledtest/waveButton.png")
        self.waveButton.config(image=waveButton, width = waveButton.width(), command= self.wavemaker_switch)
        self.waveButton.image = waveButton
        self.waveButton.grid(row=6, column=3, columnspan=2, padx=(0,60), pady=(20, 0))

        self.waveLabel = Label(master, text="Wavemaker is:   Off", width=20, font="-size 10 -weight bold")
        self.waveLabel.grid(row=7, column=3, columnspan=2, padx=(0,60), pady=(5,20))

        ## REFRESH
        self.tempRefresher()
        self.scaleChange()

    def lightToggle(self):
        if self.lightsButton["text"] == "OFF":
            self.lightsOn(100)
        else:
            self.lightsOff()

    def changeDim(self, value):
        colorMess.set_bright(int(value))

    def lightsOn(self, brightness):
        self.brightness.set(brightness)
        self.lightsButton.config(text="ON", relief=SUNKEN, font="-size 10 -weight bold", bg='#00ff00', fg='white')
        lights.turn_on()
    def lightsOff(self):
        self.brightness.set(0)
        self.lightsButton.config(text="OFF", relief=RAISED, font="-size 10 -weight bold", bg="#bbbbbb", fg='black')
        lights.turn_off()
    
    def scaleChange(self):
        if self.brightness.get()==0:
            self.lightsOff()
        else:
            self.lightsOn(self.brightness.get())
        root.after(250,self.scaleChange)

    def wavemaker_set(self, value):
        global wavemakerOn
        wavemakerOn = value
        if value == True:
            self.waveButton.configure(relief=SUNKEN, bg='#00ff00')
            self.waveLabel.configure(text="Wavemaker is:   ON")
            
        else:
            self.waveButton.configure(relief=RAISED, bg='#f0f0f0')
            self.waveLabel.configure(text="Wavemaker is:   OFF")

    def wavemaker_switch(self):
        global wavemakerOn
        if wavemakerOn == False:
            self.wavemaker_set(True)
        else:
            self.wavemaker_set(False)
        wavemaker.flip()

    def topoff_set(self, value):
        global topoffOn
        topoffOn = value
        if value == True:
            self.topoffButton.configure(relief=SUNKEN, bg='#00ff00')
            self.topoffLabel.configure(text="Top-off pump is:   ON")
            
        else:
            self.topoffButton.configure(relief=RAISED, bg='#f0f0f0')
            self.topoffLabel.configure(text="Top-off pump is:   OFF")

    def topoff_switch(self):
        global topoffOn
        if topoffOn == False:
            self.topoff_set(True)
        else:
            self.topoff_set(False)
        topoff.flip()

    def storm(self):
        ##
        global wavemakerOn
        global topoffOn
        tempWavemaker = False
        tempTopoff = False
        if wavemakerOn == True:
            tempWavemaker = True
        if topoffOn == True:
            tempTopoff = True
        ##    
        self.wavemaker_set(True)
        self.topoff_set(True)

        ##
        wavemaker.on()
        topoff.on()
        lightningSync2.storm()

        ##
        if tempWavemaker == False:
            wavemakerOn = False
            self.wavemaker_set(False)
            wavemaker.off()
        if tempTopoff == False:
            topoffOn = False
            self.topoff_set(False)
            topoff.off()

    def tempRefresher(self):
        showTemp=tempTest.read_temp()
        self.tempDisplay.configure(text=str(round(showTemp,1)) + u'\N{DEGREE SIGN} F')
        if round(showTemp,1) > 80:
            heaterOn = 'OFF'
            self.heaterLabel.configure(text="Heater is:   " + heaterOn)
        else:
            heaterOn = 'ON'
            self.heaterLabel.configure(text="Heater is:   " + heaterOn)
        root.after(1000,self.tempRefresher)

    def onExit(self):
        GPIO.cleanup()
        colorMess.off()
        root.destroy()

root = Tk()
b = appTest(root)

root.mainloop()
