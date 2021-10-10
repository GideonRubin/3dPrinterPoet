import serial
import time


def testSerial(port):
    ret = False
    test = serial.Serial(baudrate=115200, timeout=0, writeTimeout=0)
    test.port = port
    while not ret:
        try:
            test.open()
            if test.isOpen():
                test.close()
                ret = True
        except serial.serialutil.SerialException:
            print('Can not connect to serial port.')
            time.sleep(2)

    return ret

def writeCode():
    port = '/dev/cu.usbserial-1440'
    testSerial(port)
    gcode=[i.strip() for i in open('drawing.gcode')]
    ser = serial.Serial(port, 115200)
    ser.write((gcode[0]+"\r\n").encode())

    for j in range(1,len(gcode)):
        ok = True
        while ok:
            msg = ser.readline().decode()
            print(msg)
            if 'ok' in msg:
                ok = False
                line = gcode[j] + "\r\n"
                ser.write(line.encode())
                print(line)
                print('received ok')
            print('waiting')
    ser.close()
    print("Job complete!")