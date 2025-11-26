
***

# VEML7700 Light Sensor Interface – 4G Data Logger Board

This repository provides firmware and instructions for interfacing the VEML7700 ambient light sensor with the 4G Data Logger board. It reads lux (light intensity) data and enables real-time visualization on the IoT Serial Monitoring App.

***

## Features

- Measures ambient light intensity (lux) using the VEML7700 sensor
- Communicates via I2C with the 4G Data Logger Board (Quectel EC200U-powered)
- Live data output and charting in the IoT Serial Monitoring App
- Configurable logging intervals and real-time UART logs

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U recommended)
- VEML7700 sensor (I2C output)
- Programmer (for firmware upload/UART usage)
- USB cable (for board-PC connection)

***

## Software Requirements

- QPYCom (for uploading Python files and accessing REPL)
- IoT Serial Monitoring App (light intensity charting and display)
- Python runtime compatible with Quecpython v1.12 or newer

***

## Prerequisites

- Basic Python programming and sensor interfacing skills
- Familiarity with I2C and UART communication protocols
- Correct wiring between sensor and board as described below

***

## Pin Configuration

| **Board Pins** | **Sensor Pins**      |
|:---:|:---:|
| 3V3 | VCC |
| SCL  | SCL  |
| SDA  | SDA  |
| GND | GND |

| **Board Pins** | **Programmer Pins** |
|:---:|:---:|
| RSTx | RXD |
| RSRx | TXD |
| GND | GND |

***

## Setup & Configuration

1. Wire the VEML7700 sensor to the 4G Data Logger Board per the above mapping.
2. Connect the board to your PC with a USB cable and open QPYCom.
3. Select the correct COM port (Quectel USB REPL), set baud rate (e.g. 115200), and open the port.
4. Upload source files (`main.py`, `veml7700driver.py`, `veml7700registers.py`) to the board.
5. Stop any running code by pressing Ctrl+C in the REPL if upload issue occurs.
6. Open the IoT Serial Monitoring App, set COM port, baud rate, sensor type, and interval.
7. View live lux readings and logs in the app and serial console.

***

## Sample Output

```
Connected to COM89 at 115200 baud
VEML7700 Lux96.00
VEML7700 Lux 89.60
VEML7700 Lux96.00
VEML7700 Lux92.80
VEML7700 Lux86.40
...
Sensor Data Visualization
Light Intensity 86.4 Lux
```
Light intensity is graphically displayed and logged in the IoT Serial Monitoring App.

***

## Usage

1. Flash firmware to the board.
2. Monitor lux data from the VEML7700 sensor in the monitoring app or UART console.
3. Adjust reporting interval, COM port, and sensor settings as needed for your application.

***

## Troubleshooting

- **Sensor not detected:**  
  - Check all wiring, power, and configuration settings.
  - Ensure I2C and baud rate settings match your hardware.
- **Upload/REPL errors:**  
  - Press Ctrl+C to stop running code before uploading new files.
- **Lux readings incorrect:**  
  - Confirm sensor exposure and proper initialization.

***

## License

Released under open-source license. Check LICENSE file for details.

***
