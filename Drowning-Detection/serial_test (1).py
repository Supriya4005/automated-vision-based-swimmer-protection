import serial
import time
data = serial.Serial(
                    'COM3',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )

def Send(a):
  c
  print('sent............')

##def Read():


while True:
  Data = data.readline()
  Data1 = Data.decode('utf-8', 'ignore')
  print("Data{}".format(Data))

  if '00' in str(Data):
    print('Detected')
