# tlv493d_drv.py
import utime
from machine import I2C

TLV493D_I2C_ADDR = 0x5E
DATA_REG_START = 0x00


class TLV493D:
    def __init__(self, i2c):
        self.i2c = i2c

    # ─────────────────────────────────────────────
    # Low-level helpers (QuecPython safe)

    def _burst_read(self, start_reg, length):
        buf = bytearray(length)

        try:
            self.i2c.write(
                TLV493D_I2C_ADDR,
                b'', 0,
                bytearray([start_reg]), 1
            )
        except:
            self.i2c.write(
                TLV493D_I2C_ADDR,
                bytearray([start_reg])
            )

        utime.sleep_ms(1)

        try:
            self.i2c.read(TLV493D_I2C_ADDR, buf)
        except:
            self.i2c.read(
                TLV493D_I2C_ADDR,
                b'', 0,
                buf, length, 0
            )

        return buf

    @staticmethod
    def _twos_complement(val, bits):
        if val & (1 << (bits - 1)):
            val -= (1 << bits)
        return val

    # ─────────────────────────────────────────────
    # Public API

    def read_magnetic_mT(self):
        try:
            data = self._burst_read(DATA_REG_START, 6)

            bx = ((data[0] << 4) | (data[4] & 0x0F))
            by = ((data[1] << 4) | (data[4] >> 4))
            bz = ((data[2] << 4) | (data[5] & 0x0F))

            bx = self._twos_complement(bx, 12)
            by = self._twos_complement(by, 12)
            bz = self._twos_complement(bz, 12)

            scale = 0.098  # mT / LSB

            return (
                round(bx * scale, 3),
                round(by * scale, 3),
                round(bz * scale, 3),
            )

        except Exception:
            return None, None, None
