# lis3dh_drv.py
from machine import I2C

class LIS3DH:
    WHO_AM_I_REG = 0x0F
    WHO_AM_I_VAL = 0x33
    ADDR_LIST = [0x18, 0x19]

    def __init__(self, i2c):
        self.i2c = i2c
        self.addr = None
        self._detect()
        self._init_sensor()

    # ─────────────────────────────────────────────
    # Low-level I2C helpers (QuecPython safe)

    def _write_reg(self, reg, val):
        buf = bytearray([reg, val])
        self.i2c.write(self.addr, b'', 0, buf, 2)

    def _read_reg(self, reg):
        reg_buf = bytearray([reg])
        self.i2c.write(self.addr, b'', 0, reg_buf, 1)
        val_buf = bytearray(1)
        self.i2c.read(self.addr, b'', 0, val_buf, 1, 0)
        return val_buf[0]

    # ─────────────────────────────────────────────
    # Device detection

    def _detect(self):
        for addr in self.ADDR_LIST:
            self.addr = addr
            try:
                if self._read_reg(self.WHO_AM_I_REG) == self.WHO_AM_I_VAL:
                    return
            except Exception:
                pass
        raise Exception("LIS3DH not found")

    # ─────────────────────────────────────────────
    # Sensor configuration

    def _init_sensor(self):
        self._write_reg(0x20, 0x57)  # CTRL_REG1: 50 Hz, enable axes
        self._write_reg(0x23, 0x08)  # CTRL_REG4: high resolution

    # ─────────────────────────────────────────────
    # Public API

    @staticmethod
    def _twos_complement(val, bits):
        if val & (1 << (bits - 1)):
            val -= 1 << bits
        return val

    def read_axes_ms2(self):
        scale = 0.001  # g/LSB
        try:
            axes = []
            for reg in (0x28, 0x2A, 0x2C):
                l = self._read_reg(reg)
                h = self._read_reg(reg + 1)
                raw = (h << 8) | l
                raw = self._twos_complement(raw, 16)
                raw >>= 4
                axes.append(raw * scale * 9.80665)
            return tuple(axes)
        except Exception:
            return (0.0, 0.0, 9.80665)
