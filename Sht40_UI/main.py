from machine import I2C, UART  # Import hardware interfaces for I2C and UART communication
from usr.sht4x import SHT4X  # Import SHT40 temperature/humidity sensor driver
import utime as time  # Import time functions with alias
import osTimer
from misc import Power
import utime

class DeviceState:
    def __init__(self):
        self.CurrentTemp = 0.0
        self.CurrentHum = 0.0
        self.SensorInterval = 5000

device_state = DeviceState()
# ────────────────────────────────────────────────
# Add UART1 for output (usually the debug/USB serial port)


def uart_print(msg):
    """Send message to UART1 with newline"""
    try:
        uart1.write((msg + "\r\n").encode())
    except:
        pass  # silent fail - don't crash if UART1 has issue

def get_temp_sht40():
    try:
        tem, hum = sht.get_measurements()  # Returns (temperature, humidity)     
        if tem < -40:
            return -1
        device_state.CurrentTemp = tem
        device_state.CurrentHum = hum
        uart_print("SHT40:Temperature:{}°C, Humidity:{}%".format(device_state.CurrentTemp, device_state.CurrentHum)) 
        return (tem, hum)
    except Exception as e:
        return 
    
def data_check(args):
    get_temp_sht40()
    
uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)   # adjust pins/params if needed for your board
i2c_dev = I2C(0, fastmode=True)
sht = SHT4X(i2c_dev)
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