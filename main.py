from tkinter import *
from tkinter import ttk
import serial
import io
import time

ser = serial.Serial('COM3', 9600, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

def measure(base):
    print("Starting measurement")
    sio.write("m\n")
    sio.flush()
    data = sio.readline()
    try:
        print("Collected data, attempting to convert to float")
        data = (((float(data[0:len(data)-1])) / 1024) * 5) - base
        print("Conversion successful")
        return data
    except:
        print("Conversion failed, retrying")
        return measure(base)

class MeasureTest:
    def __init__(self, master):
        self.label = ttk.Label(master, text="")
        self.label.grid(row=0, column=1, columnspan=1)
        self.testlbl = ttk.Label(master, text="Measured detector voltage:")
        self.testlbl.grid(row=0, column=0,columnspan=1)
        self.unit = ttk.Label(master, text="V")
        self.unit.grid(row=0, column=2,columnspan=1)
        self.progress = ttk.Progressbar(master, length=100)
        self.base = 0
        ttk.Button(master, text="Measure", command=self.doMeasurement).grid(row=1,column=1)
        ttk.Button(master, text="Calibrate", command=self.calibrate).grid(row=1,column=0)
    
    def doMeasurement(self):
        self.label.config(text=measure(self.base))

    def calibrate(self):
        basecount = 10
        base = 0
        for i in range(basecount):
            base = base + measure(0)
            #self.progress.step(10)
        self.base = base / basecount


root = Tk()
root.title("Spectrometer")
root.minsize(400, 100)
app = MeasureTest(root)
root.mainloop()