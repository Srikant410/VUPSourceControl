import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import RADDevice_VUP_ui
import time
import datetime
import serial
import threading

class Valued(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = RADDevice_VUP_ui.Ui_Dialog()        
        self.ui.setupUi(self)

        current_time = str(datetime.datetime.now().time())        
        #QObject.connect(self.ui.pushButton_1,SIGNAL("operation()"),ser_operation('rtcr'))
        self.ui.label.setText(ser_operation('myid'))
        self.ui.label_2.setText(ser_operation('getv'))
        self.ui.label_3.setText(ser_operation('stat'))
        self.ui.dateTimeEdit.setDisplayFormat(ser_operation('rtcr'))
        self.ui.lcdNumber.display(ser_operation('temp'))
        #self.ui.label.setText('AC123121SHAICC')
        #self.ui.label_2.setText('Version 1.0')
        #self.ui.label_3.setText('ok')
        #self.ui.dateTimeEdit.setDisplayFormat(str(datetime.datetime.now()))
        #self.ui.lcdNumber.display('47.00')
        connected = False
        port=3
        baud = 115200
        serial_port = serial.Serial(port, baud, timeout=0)
        thread = threading.Thread(target=read_from_port, args=(serial_port,))
        thread.start()    

def ser_operation(command):
    ser = serial.Serial(
          port='/dev/controlboard',
          baudrate = 115200,
          parity=serial.PARITY_NONE,
          stopbits=serial.STOPBITS_ONE,
          bytesize=serial.EIGHTBITS,
          timeout=1
        )
    cmd = command
    print("Serial is open: " + str(ser.isOpen()))
    v = '\r\n'
    ser.write(cmd.encode('ascii')+ v.encode('ascii'))
    print("Now Writing")
    time.sleep(1)
    x = ser.read(ser.inWaiting())
    print("got '" + x.decode('utf-8') + "'")
    a = x.decode('utf-8')
    ser.close()
    return a

def read_from_port(ser):
   
    while not connected:
        #serin = ser.read()
        connected = True

        while True:           
            if (ser.inWaiting()>0): #if incoming bytes are waiting to be read from the serial input buffer
                data_str = ser.read(ser.inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
                print(data_str, end='') #print the incoming string without putting a new-line ('\n') automatically after every print()


app = QApplication(sys.argv)
window = Valued()
window.show()
sys.exit(app.exec_())



