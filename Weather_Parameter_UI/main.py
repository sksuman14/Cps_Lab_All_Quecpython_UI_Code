import _thread
import utime
from machine import UART
from machine import I2C
from queue import Queue
import osTimer
from misc import ADC , Power
from usr.bmedriver import BME680
from usr.veml_7700_driver import VEML7700
import osTimer

class DeviceState:
    def __init__(self):
        self.Lux = 0.0
        self.CurrentTemp = 0.0
        self.CurrentHum = 0.0
        self.Pressure = 0.0
        self.Tips = 0  # Rainfall tip count
        self.BoolUltrasonic = False  # Flag for ultrasonic data availability
        self.ws_data = 0.0  # wind speed
        self.wd_data = 0.0  # wind direction
        self.SensorInterval = 5000

device_state = DeviceState()
# ───────────────────────────────────────────────

def uart_print(msg):
    """Send message to UART1 with newline"""
    try:
        uart1.write((msg + "\r\n").encode())
    except:
        pass  # silent fail - don't crash if UART1 has issue
# ────────────────────────────────────────────────

class Example_uart(object):
    def __init__(self, no=UART.UART2, bate=9600, data_bits=8, parity=0, stop_bits=1, flow_control=0):
        self.uart = UART(no, bate, data_bits, parity, stop_bits, flow_control)
        self._queue = Queue(5)
        _thread.start_new_thread(self.handler_thread, ())
        self.uart.set_callback(self.callback)
        self.ws_data = 0
        self.wd_data = 0
        self.msg = ""

    def callback(self, para):
        if(0 == para[0]):
            self._queue.put(para[2])

    def uartWrite(self, msg):
        print("write msg:{}".format(msg))
        self.uart.write(msg)

    def uartRead(self, len):
        msg = self.uart.read(len)
        if msg is not None:
            utf8_msg = msg.decode()
            self.msg = msg.decode()
            device_state.BoolUltrasonic = True
            print("UartRead msg: {}".format(utf8_msg))
        else: 
            device_state.BoolUltrasonic = False
            print("No data received")
               
        return utf8_msg

    def handler_thread(self):
        while True:
            recv_len = self._queue.get()
            self.uartRead(recv_len)

#____________________________For the sensors reading functions___________________________

def get_lux():
    try:
        device_state.Lux = veml.lux()
        print("VEML7700 - Light Intensity: {} lux".format(device_state.Lux))
        # uart_print("VEML7700 - Light Intensity : {:.2f} lux".format( veml.lux()))
        return device_state.Lux
    except Exception as e:
        print("Error reading Lux:{}".format(e))
        return None
    
def get_PTH():
    """Read BME680 bme data and apply coefficients to temperature, humidity, and pressure"""
    try:
        data_ready = bme.get_sensor_data()
        if data_ready:
            device_state.CurrentTemp = bme.data.temperature
            device_state.CurrentHum = bme.data.humidity 
            device_state.Pressure = bme.data.pressure 
            
            uart_print("T:{:.2f},H:{:.2f},P:{:.2f},L:{:.2f}".format(device_state.CurrentTemp, device_state.CurrentHum,device_state.Pressure,device_state.Lux))
        else:
            print("BME680 - Data not ready")
    except Exception as e:
        print("[ERROR] Failed to read bme values:{}".format(e))


def extract_wind_data():
    if device_state.BoolUltrasonic:
        utime.sleep(2)
        device_state.BoolUltrasonic = False
        data = uart_test.msg.split(',')
        device_state.wd_data = float(data[1])
        device_state.ws_data = float(data[2])
        uart_print("Wind speed: {:.2f},Wind direction: {:.1f} ".format(device_state.ws_data,device_state.wd_data))

def adc_loop():
    print("start adc loop\n")
    while True:
        try:
            adcVal = adc.read(ADC.ADC0)
            if adcVal is not None and adcVal > 1000:  # rain tip detected
                device_state.Tips += 1
                uart_print("Rain Tip Detected! Rainfall: {}".format(device_state.Tips))
                utime.sleep(1)
            utime.sleep(0.1)
        except Exception as e:
            print("ADC Loop Error: {}".format(e))
            utime.sleep(1)   # prevent spamming errors

def data_check(args):
    get_lux()
    get_PTH()
    extract_wind_data()


 
# Add UART1 for output (usually the debug/USB serial port)
uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
uart_test = Example_uart()
adc = ADC()
adc.open()
i2c_dev = I2C(0,fastmode = True)
veml=VEML7700(i2c_dev)
bme = BME680(i2c_dev)
bme.initialize_bme()

Sensor_timer = osTimer()
Sensor_timer.start(device_state.SensorInterval, 1, data_check)


_thread.start_new_thread(adc_loop, ())

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

