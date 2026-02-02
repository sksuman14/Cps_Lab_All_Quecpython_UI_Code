from misc import ADC , Power # type: ignore
from machine import UART  # type: ignore
import utime
import _thread

class DeviceState:
    def __init__(self):
        self.Tips = 0  # Rainfall tip count
        self.SensorInterval = 5000

device_state = DeviceState()

def uart_print(msg):
    """Send message to UART1 with newline"""
    try:
        uart1.write((msg + "\r\n").encode())
    except:
        pass  # silent fail - don't crash if UART1 has issue

def adc_loop():
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

uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
adc = ADC()
adc.open()
_thread.start_new_thread(adc_loop, ())
print("ADC Rain Tip Detection Started")

while True:
    if uart1.any() > 0:
        num_bytes = uart1.any()
        incoming = uart1.read(num_bytes)
        if incoming is not None:
            uart_print("RX Received {} bytes: {}".format(num_bytes, incoming))
            try:
                text = incoming.decode('utf-8').strip()
                uart_print("Text: '{}'".format(text))
                if text == "restartDevice":
                    uart_print("Restarting device...")
                    Power.powerRestart()
                else:
                    uart_print("Unknown command: {}".format(text))
            except Exception as e:
                uart_print("Error processing command: {}".format(e))
    utime.sleep(0.1)