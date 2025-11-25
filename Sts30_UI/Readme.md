***

# STS30 Sensor Interface – 4G Data Logger Board

This repository provides firmware and setup instructions to integrate the STS30 temperature sensor with the 4G Data Logger board. The project supports real-time acquisition and visualization of temperature data using the IoT Serial Monitoring App.

***

## Features

- Measures ambient temperature using the STS30 sensor
- Connects via I2C interface for stable sensor communication
- Optimized for Quectel EC200U-powered 4G Data Logger hardware
- Live display and charting of data in the IoT Serial Monitoring App
- Supports logging intervals and UART logs for flexible monitoring

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U module recommended)
- STS30 Sensor (I2C)
- Programmer (for flashing and UART connection)
- USB cable (for board-PC interface)

***

## Software Requirements

- QPYCom (for Python flashing and REPL access)
- IoT Serial Monitoring App (for live data output)
- Quecpython v1.12 or compatible Python environment

***

## Prerequisites

- Familiarity with basic Python programming
- Understanding of I2C and UART communication protocols
- Basic project wiring skills

***

## Pin Configuration

| **Board Pins** | **Sensor Pins** |
|:---:|:---:|
| 3V3 | VCC |
| GND | GND |
| SDA | SDA |
| SCL | SCL |

| **Board Pins** | **Programmer Pins** |
|:---:|:---:|
| RSTx | RXD |
| RSRx | TXD |
| GND | GND |

***

## Setup & Configuration

1. Connect the STS30 sensor to the 4G Data Logger Board via I2C using the pin mapping above.
2. Use a USB cable to connect your board to the PC.
3. Open QPYCom, select the correct COM port for Quectel USB REPL, set baud rate (e.g., 115200), and open port.
4. Upload relevant Python source files (`main.py`, `sts30.py`, system configuration files) to the board.
5. Interrupt any running code by pressing Ctrl+C in QPYCom if you encounter upload errors.
6. Start the IoT Serial Monitoring App, enter COM port, baud rate, sensor selection, and interval settings.
7. Monitor and visualize live temperature data from the sensor.

***

## Sample Output

```
Connected to COM4 at 115200 baud
STS30 Temperature 23.03°C
STS30 Temperature 23.05°C
STS30 Temperature 23.06°C
...
```
Temperature readings are charted and logged in the IoT Serial Monitoring App.

***

## Usage

1. Flash the STS30 firmware to your 4G Data Logger Board.
2. Start the system and sensor readings will appear in the serial terminal or IoT Serial Monitoring App.
3. Adjust COM port, baud rate, sensor selection, and interval in the app as needed.

***

## Troubleshooting

- **Sensor Not Detected:**  
  - Inspect wiring and connections; confirm correct I2C address and baud rate.
- **Upload/REPL Issues:**  
  - Stop previous code in the QPYCom terminal (Ctrl+C) and retry uploading.
- **Erratic Readings:**  
  - Check physical environment and initialization steps in firmware.

***

## License

This project is released under an open-source license. See LICENSE file for details.

***
