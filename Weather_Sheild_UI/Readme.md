
***

# Weather Shield Sensor Interface – 4G Data Logger Board

This repository provides firmware and instructions for interfacing a Weather Shield sensor module with the 4G Data Logger board. It collects, logs, and visualizes environmental parameters (temperature, humidity, pressure, and light intensity) in real time using the IoT Serial Monitoring App.

***

## Features

- Measures temperature, humidity, atmospheric pressure, and ambient light (lux)
- I2C communication for multi-sensor support on 4G Data Logger (Quectel EC200U)
- Live data charting and output in the IoT Serial Monitoring App
- Supports interval-based data logging and UART console logging

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U recommended)
- Weather Shield sensor module (I2C)
- Programmer (for firmware flashing/UART connection)
- USB cable (for board to PC interface)

***

## Software Requirements

- QPYCom (Python firmware upload and REPL access)
- IoT Serial Monitoring App (live dashboard/charting)
- Python environment compatible with Quecpython v1.12 or newer

***

## Prerequisites

- Basic Python programming skills
- Understanding of I2C/UART and environmental sensor protocols
- Correct wiring for all modules (see below)

***

## Pin Configuration

| **Board Pins** | **Sensor Pins** |
|:---:|:---:|
| 3V3 | VCC |
| SCL | SCL |
| SDA | SDA |
| GND | GND |

| **Board Pins** | **Programmer Pins** |
|:---:|:---:|
| RSTx | RXD |
| RSRx | TXD |
| GND | GND |

***

## Setup & Configuration

1. Connect the Weather Shield sensor module to the 4G Data Logger board using the mapping above.
2. Attach the board to your PC via USB and open QPYCom.
3. Select the correct COM port (Quectel USB REPL), set baud rate (e.g., 115200), and open the port.
4. Upload required Python files (`main.py`, drivers, system configs) to the board.
5. If files fail to upload, interrupt with Ctrl+C in QPYCom REPL and retry.
6. Launch the IoT Serial Monitoring App, configure COM port, baud rate, sensor selection, and logging interval.
7. View all live readings and sensor logs in the dashboard and UART console.

***

## Sample Output

```
Connected to COM4 at 115200 baud
Temperature 22.90°C, Humidity 57.58%, Pressure 986.81 hPa, Light 662.40 Lux
Temperature 22.90°C, Humidity 57.55%, Pressure 986.81 hPa, Light 656.00 Lux
Temperature 22.90°C, Humidity 57.56%, Pressure 986.81 hPa, Light 684.80 Lux
...
Sensor Data Visualization
Temperature: 22.90°C
Humidity: 57.49%
Pressure: 986.80 hPa
Light Intensity: 665.6 Lux
```
All sensor values are continuously graphed and logged in the app.

***

## Usage

1. Flash the Weather Shield firmware to your 4G Data Logger Board.
2. Monitor temperature, humidity, pressure, and light data in real time via UART console and app dashboard.
3. Adjust intervals, sensor settings, and COM port as needed for your application.

***

## Troubleshooting

- **Sensor not detected:**  
  - Check wiring, I2C addresses, and configuration settings.
  - Ensure all pins and modules are securely connected.
- **Upload/REPL errors:**  
  - Press Ctrl+C in REPL before uploading new files.
- **Incorrect readings:**  
  - Confirm sensor calibration and environmental exposure.

***

## License

Released under open-source license. See LICENSE for terms.

***
