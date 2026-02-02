# vl53l0x_drv.py
import utime
from machine import I2C

# I2C address
VL53L0X_I2C_ADDR = 0x29

# Registers
SYSRANGE_START          = 0x00
SYSTEM_INTERRUPT_CLEAR  = 0x0B
FINAL_RANGE_MSB         = 0x1E


class VL53L0X:
    def __init__(self, i2c):
        self.i2c = i2c

    # ─────────────────────────────────────────────
    # Low-level helpers (QUECPYTHON SAFE)

    def _write_reg(self, reg, val):
        data = bytearray([reg, val])
        try:
            self.i2c.write(VL53L0X_I2C_ADDR, data)
        except:
            self.i2c.write(
                VL53L0X_I2C_ADDR,
                b'', 0,
                data, 2
            )

    def _burst_read(self, start_reg, length):
        buf = bytearray(length)

        try:
            self.i2c.write(
                VL53L0X_I2C_ADDR,
                b'', 0,
                bytearray([start_reg]), 1
            )
        except:
            self.i2c.write(
                VL53L0X_I2C_ADDR,
                bytearray([start_reg])
            )

        utime.sleep_ms(1)

        try:
            self.i2c.read(VL53L0X_I2C_ADDR, buf)
        except:
            self.i2c.read(
                VL53L0X_I2C_ADDR,
                b'', 0,
                buf, length, 0
            )

        return buf

    # ─────────────────────────────────────────────
    # Public API

    def read_distance_cm(self):
        try:
            # Start ranging
            self._write_reg(SYSRANGE_START, 0x01)
            utime.sleep_ms(50)

            data = self._burst_read(FINAL_RANGE_MSB, 2)
            distance_mm = (data[0] << 8) | data[1]

            # Clear interrupt
            self._write_reg(SYSTEM_INTERRUPT_CLEAR, 0x01)

            return round(distance_mm / 10.0, 2)

        except Exception:
            return None
