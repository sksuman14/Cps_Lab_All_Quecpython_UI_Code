from machine import I2C, UART
import utime
import osTimer
from misc import Power
from usr.vl53l0x import VL53L0X

# ─────────────────────────────────────────────
# Device State

class DeviceState:
    def __init__(self):
        self.Distance_cm = 0.0
        self.SensorInterval = 1000  # ms

device_state = DeviceState()

# ─────────────────────────────────────────────
# UART

uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)

def uart_print(msg):
    try:
        uart1.write((msg + "\r\n").encode())
    except:
        pass

# ─────────────────────────────────────────────
# I2C + Sensor init

i2c = I2C(I2C.I2C0, I2C.FAST_MODE)
vl53 = VL53L0X(i2c)

uart_print("VL53L0X ready")

# ─────────────────────────────────────────────
# Timer callback

def data_check(args):
    dist = vl53.read_distance_cm()
    if dist is not None:
        device_state.Distance_cm = dist
        uart_print("Distance is {} cm".format(dist))
    else:
        uart_print("VL53L0X: Read failed")

# ─────────────────────────────────────────────
# Start timer

Sensor_timer = osTimer()
Sensor_timer.start(device_state.SensorInterval, 1, data_check)

# ─────────────────────────────────────────────
# UART command loop

while True:
    if uart1.any():
        incoming = uart1.read(uart1.any())
        if incoming:
            try:
                cmd = incoming.decode().strip()
                uart_print("RX: {}".format(cmd))

                if cmd.startswith("SET_INTERVAL:"):
                    sec = int(cmd.split(":", 1)[1])
                    device_state.SensorInterval = sec * 1000

                    Sensor_timer.stop()
                    Sensor_timer = osTimer()
                    Sensor_timer.start(
                        device_state.SensorInterval,
                        1,
                        data_check
                    )

                    uart_print("Interval set to {} seconds".format(sec))

                elif cmd == "restartDevice":
                    uart_print("Restarting device...")
                    Power.powerRestart()

                else:
                    uart_print("Unknown command")

            except Exception as e:
                uart_print("CMD error: {}".format(e))

    utime.sleep(0.1)
