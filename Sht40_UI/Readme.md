***

# SHT40 Sensor Interface – 4G Data Logger Board

This repository provides firmware and setup instructions to integrate the SHT40 temperature and humidity sensor with the 4G Data Logger board. The project enables real-time acquisition and visualization of environmental data using the IoT Serial Monitoring App.

***

## Features

- Measures temperature and humidity using the SHT40 sensor
- Communicates via I2C for reliable and precise sensor data acquisition
- Designed for compatibility with Quectel EC200U-powered 4G Data Logger hardware
- Live data display and charting in the IoT Serial Monitoring App
- Supports user-configurable logging intervals and UART logs

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U module recommended)
- SHT40 Sensor (I2C interface)
- Programmer (for flashing and UART connection)
- USB cable (PC to board connection)

## Software Requirements

- QPYCom (recommended for Python flashing and REPL access)
- IoT Serial Monitoring App
- Basic Python environment (Quecpython v1.12 supported)


***

## Prerequisites

- Basic knowledge of Python
- Understanding of I2C and UART communication protocols
- Basic project setup and wiring skills

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

1. Connect the SHT40 sensor to the 4G Data Logger Board via I2C as per the pin mapping above.
2. Connect your board to the PC using a USB cable.
3. Open QPYCom, select the COM port for the Quectel USB REPL, set baud rate (e.g., 115200), and open the port.
4. Upload the required Python files (`main.py`, `sht4x.py` and configuration files) to the board.
5. If uploading fails, stop any running REPL code with Ctrl+C.
6. Launch the IoT Serial Monitoring App, enter COM port, baud rate, sensor type, and interval settings.
7. View live temperature and humidity data in the app.

***

## Sample Output

```
Connected to COM4 at 115200 baud
SHT40 Temperature 30.18°C, Humidity 52.09%
SHT40 Temperature 30.08°C, Humidity 51.25%
SHT40 Temperature 29.96°C, Humidity 50.78%
SHT40 Temperature 29.87°C, Humidity 50.37%
SHT40 Temperature 29.76°C, Humidity 50.15%
```
Live visualization and logs are available in the IoT Serial Monitoring App.

***

## Usage

1. Flash the firmware onto your 4G Data Logger Board.
2. The firmware starts reading temperature and humidity data from the SHT40 sensor.
3. Data is streamed to your PC and visualized via the IoT Serial Monitoring App.
4. Log intervals, COM port, and settings can be configured in the app.

***

## Troubleshooting

- **Sensor Not Detected:**  
  - Check all wiring and physical connections.
  - Ensure the I2C address and baud rate are set correctly in the app.
- **Upload/REPL Issues:**  
  - Interrupt previous code execution using Ctrl+C in the QPYCom terminal.
  - Retry uploading after stopping the REPL.
- **Inconsistent Readings:**  
  - Confirm correct sensor placement.
  - Verify I2C interface selections and initialization in firmware.

***

## License

Released under an open-source license. See LICENSE file for details.

***
