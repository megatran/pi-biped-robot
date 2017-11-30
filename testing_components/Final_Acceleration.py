#Arthur Mayer, Nhan Tran
#11/14/17
#Final Project Accelerometer Stuff

import smbus
import time
import RPi.GPIO

i=0
RPi.GPIO.setmode(RPi.GPIO.BCM)

class Accelerometer:
    def __init__(self, x_acc=0, y_acc=0, z_acc=0):
        self.x_acc=x_acc
        self.y_acc=y_acc
        self.z_acc=z_acc
        self.coordinateRepresentation = '('+str(self.x_acc)+', '+str(self.y_acc)+', '+str(self.z_acc)+')'
    def printData(self):
        print('Acceleration in x is', self.x_acc)
        print('Acceleration in y is', self.y_acc)
        print('Acceleration in z is', self.z_acc)
    def printCoord(self):
        print(self.coordinateRepresentation)

def printArray(array):
    arrayString="[\n"
    for i in array:
        if str(type(i)) == "<class '__main__.Accelerometer'>" or str(type(i)) == "<type 'instance'>":
            arrayString = arrayString + i.coordinateRepresentation+',\n'
        else:
            arrayString=arrayString+str(i)+',\n'
    arrayString=arrayString+']'
    print(arrayString)

# Get I2C bus - initial bus to channel 1
bus = smbus.SMBus(1)
accs=[]
'''
try:
    while True:
        #Parameters for write_byte_data
        #1. Address of the device
        #2. Communication data - active mode control register
        #3. Our data - 0 (standby mode) or 1 (active)
        bus.write_byte_data(0x1D, 0x2A, 1)
        time.sleep(0.5)
        
        #Read from the status register, real-time status register 0x00
        #Data returned will be an array
        #Contents of 7 bytes read and stored in data array represent:
        #status (ignore), MSBx, LSBx, MSBy, LSBy, MSBz, LSBz
        data = bus.read_i2c_block_data(0x1D, 0x00, 7)
        #accs.append(Accelerometer(((data[1]*256+data[2])/16) - 4096*((data[1]*256+data[2])/16>2047), ((data[3]*256+data[4])/16) - 4096*((data[3]*256+data[4])/16>2047), ((data[5]*256+data[6])/16) - 4096*((data[5]*256+data[6])/16>2047)))
        acceleration = Accelerometer(((data[1]*256+data[2])/16) - 4096*((data[1]*256+data[2])/16>2047), ((data[3]*256+data[4])/16) - 4096*((data[3]*256+data[4])/16>2047), ((data[5]*256+data[6])/16) - 4096*((data[5]*256+data[6])/16>2047))
        if acceleration.x_acc>500:
            print("right")
        if acceleration.x_acc<-500:
            print("left")

        if acceleration.y_acc>500:
            print("up")
        if acceleration.y_acc<-500:
            print("down")
        
        #put register in standbye mode
        bus.write_byte_data(0x1D, 0x2A, 0)
        time.sleep(0.5)

        #print(data)
        i=i+1

#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
    #printArray(accs)
    print("User requested exit... bye!")
try:
    while True:
        #Parameters for write_byte_data
        #1. Address of the device
        #2. Communication data - active mode control register
        #3. Our data - 0 (standby mode) or 1 (active)
        bus.write_byte_data(0x1D, 0x2A, 1)
        time.sleep(0.5)
        
        #Read from the status register, real-time status register 0x00
        #Data returned will be an array
        #Contents of 7 bytes read and stored in data array represent:
        #status (ignore), MSBx, LSBx, MSBy, LSBy, MSBz, LSBz
        data = bus.read_i2c_block_data(0x1D, 0x00, 7)
        #accs.append(Accelerometer(((data[1]*256+data[2])/16) - 4096*((data[1]*256+data[2])/16>2047), ((data[3]*256+data[4])/16) - 4096*((data[3]*256+data[4])/16>2047), ((data[5]*256+data[6])/16) - 4096*((data[5]*256+data[6])/16>2047)))
        acceleration = Accelerometer(((data[1]*256+data[2])/16) - 4096*((data[1]*256+data[2])/16>2047), ((data[3]*256+data[4])/16) - 4096*((data[3]*256+data[4])/16>2047), ((data[5]*256+data[6])/16) - 4096*((data[5]*256+data[6])/16>2047))
        if acceleration.x_acc>500:
            print("right")
        if acceleration.x_acc<-500:
            print("left")

        if acceleration.y_acc>500:
            print("up")
        if acceleration.y_acc<-500:
            print("down")
        
        #put register in standbye mode
        bus.write_byte_data(0x1D, 0x2A, 0)
        time.sleep(0.5)

        #print(data)
        i=i+1

#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
    #printArray(accs)
    print("User requested exit... bye!")

#Sample modified from https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2
'''
