***

# LIS3DH Sensor Interface – 4G Data Logger Board

This repository provides firmware and setup guidance for interfacing an LIS3DH sensor with the 4G Data Logger board. The solution enables real-time acquisition and visualization of three-axis acceleration data for motion and vibration monitoring using the IoT Serial Monitoring App.

***

## Features

- Measures acceleration on X, Y, Z axes using the LIS3DH sensor
- I2C communication with the 4G Data Logger Board (Quectel EC200U-based)
- Real-time visualization of sensor output in the IoT Serial Monitoring App
- Configurable data logging intervals and live UART logs

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U module recommended)
- LIS3DH Sensor (I2C interface)
- Programmer (for firmware and UART upload)
- USB cable (for PC-board interface)

***

## Software Requirements

- QPYCom (Python upload, file interaction, REPL access)
- IoT Serial Monitoring App (for displaying and charting acceleration data)
- Python runtime compatible with Quecpython v1.12 or newer

***

## Prerequisites

- Basic Python and I2C communication protocol understanding
- Project setup and hardware wiring ability

***

## Pin Configuration

| **Board Pins** | **Sensor Pins** |
|:---:|:---:|
| 3V3 | VCC |
| SDA | SDA |
| SCL | SCL |
| GND | GND |

| **Board Pins** | **Programmer Pins** |
|:---:|:---:|
| RSTx | RXD |
| RSRx | TXD |
| GND | GND |

***

## Setup & Configuration

1. Wire the LIS3DH sensor to the 4G Data Logger board as detailed above.
2. Connect your board to the PC via USB and launch QPYCom.
3. Select the correct COM port (Quectel USB REPL), set the baud rate (e.g., 115200), and open the port.
4. Upload Python files (`main.py`, `systemconfig.json`) to the board.
5. If upload fails, interrupt current execution in QPYCom's REPL with Ctrl+C.
6. Open IoT Serial Monitoring App, enter correct COM port, baud rate, sensor type, and interval settings.
7. View and log live acceleration data in the app.

***

## Sample Output

```
Connected to COM4 at 115200 baud
LIS3DH X0.000, Y0.000, Z9.807
LIS3DH X0.000, Y0.000, Z9.807
LIS3DH X0.000, Y0.000, Z9.807
...
Acceleration X 0.00 ms Y 0.00 ms Z 9.81 ms
```
Acceleration vector data are displayed and graphed in the IoT Serial Monitoring App.

***

## Usage

1. Flash LIS3DH firmware onto the 4G Data Logger Board.
2. Monitor live acceleration data for all axes via UART console or serial monitoring app.
3. Customize settings such as interval, sensor, and port in the app to match your requirements.

***

## Troubleshooting

- **Sensor Not Detected:**  
  - Check wiring connections and correct sensor mapping.
  - Verify app COM port and baud rate settings.
- **Upload/REPL Issues:**  
  - Press Ctrl+C to halt prior runs before re-uploading firmware.
- **Unexpected Output:**  
  - Examine sensor mounting and initialization method in code.

***

## License

Released under an open-source license. Refer to LICENSE file for complete terms.

***
