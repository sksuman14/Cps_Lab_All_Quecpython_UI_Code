from machine import I2C, UART
from usr.sts30 import STS30  
import utime 
import osTimer
from misc import Power


class DeviceState:
    def __init__(self):
        self.CurrentTemp = 0.0
        
        self.SensorInterval = 5000

device_state = DeviceState() 

def uart_print(msg):
    """Send message to UART1 with newline"""
    try:
        uart1.write((msg + "\r\n").encode())
    except:
        pass 

def get_STS30_Temperature():
    """Read STS30 temperature data"""
    try:
        temp = sts.get_temperature()
        if temp is not None:
            device_state.CurrentTemp = temp

            uart_print("Temperature:{:.2f}".format(device_state.CurrentTemp))
        else:
            print("STS30 - Data not ready")

    except Exception as e:
        print("[ERROR] Failed to read STS30 temperature: {}".format(e))


def data_check(args):
    get_STS30_Temperature()

uart1 = UART(UART.UART2, 115200, 8, 0, 1, 0) 
i2c_dev = I2C(0, fastmode=True)
sts = STS30(i2c_dev)    
print("SHT40 initialized")
Sensor_timer = osTimer()
Sensor_timer.start(device_state.SensorInterval, 1, data_check)

while True:
    if uart1.any() > 0:
        num_bytes = uart1.any()
        incoming = uart1.read(num_bytes)
        if incoming is not None:
            uart_print("RX Received {} bytes: {}".format(num_bytes, incoming))
            try:
                text = incoming.decode('utf-8').strip()
                uart_print("Text: '{}'".format(text))
            
                if text.startswith("SET_INTERVAL:"):
                    Interval = int(text.split(":", 1)[1])
                    device_state.SensorInterval = Interval * 1000
                    uart_print("Interval set to {}s".format(Interval))
                    if Sensor_timer is not None:
                        Sensor_timer.stop()              # stop old one safely
                    
                    Sensor_timer = osTimer()             # create brand new timer object
                    Sensor_timer.start(device_state.SensorInterval, 1, data_check)

                elif text == "restartDevice":
                    uart_print("Restarting device...")
                    Power.powerRestart()
                else:
                    uart_print("Unknown command: {}".format(text))
            except Exception as e:
                uart_print("Error processing command: {}".format(e))
    utime.sleep(0.1) 