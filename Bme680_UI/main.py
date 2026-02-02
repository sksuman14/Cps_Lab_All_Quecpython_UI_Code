from machine import I2C, UART  # Import hardware interfaces for I2C and UART communication
from usr.bmedriver import BME680
import utime as time  # Import time functions with alias
import osTimer
from misc import Power
import utime


class DeviceState:
    def __init__(self):
        self.CurrentTemp = 0.0
        self.CurrentHum = 0.0
        self.Pressure = 0.0
        self.Lux = 0.0  
        self.SensorInterval = 5000

device_state = DeviceState()

def uart_print(msg):
    """Send message to UART1 with newline"""
    try:
        uart1.write((msg + "\r\n").encode())
    except:
        pass  # silent fail - don't crash if UART1 has issue

def get_PTH():
    """Read BME680 bme data and apply coefficients to temperature, humidity, and pressure"""
    try:
        data_ready = bme.get_sensor_data()
        if data_ready:
            device_state.CurrentTemp = bme.data.temperature
            device_state.CurrentHum = bme.data.humidity 
            device_state.Pressure = bme.data.pressure 
            
            uart_print("Temperature:{:.2f},Humidity:{:.2f},Pressure:{:.2f}".format(device_state.CurrentTemp, device_state.CurrentHum,device_state.Pressure))
        else:
            print("BME680 - Data not ready")
    except Exception as e:
        print("[ERROR] Failed to read bme values:{}".format(e))

def data_check(args):
    get_PTH()

uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
i2c_dev = I2C(0,fastmode = True)
bme = BME680(i2c_dev)
bme.initialize_bme()

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
