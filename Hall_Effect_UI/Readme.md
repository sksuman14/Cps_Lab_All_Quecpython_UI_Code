***

# Hall Effect Sensor Interface – 4G Data Logger Board

This repository contains firmware and setup instructions to detect magnetic field changes using a Hall Effect sensor and the 4G Data Logger board. The module provides digital output for magnetic presence and supports real-time state visualization in the IoT Serial Monitoring App.

***

## Features

- Detects magnetic field changes via Hall Effect sensor (digital state monitoring)
- Reliable data logging on the 4G Data Logger Board (Quectel EC200U-based)
- Real-time sensor state and analog output displayed in IoT Serial Monitoring App
- Customizable logging intervals and UART state logging

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U module recommended)
- Hall Effect Sensor (analog or digital output)
- Programmer (for firmware and UART connection)
- USB cable (for board-PC interfacing)

***

## Software Requirements

- QPYCom (for Python file upload and REPL access)
- IoT Serial Monitoring App (for live state display and charting)
- Quecpython v1.12 or newer Python environment

***

## Prerequisites

- Basic Python knowledge
- Familiarity with analog/digital signals, UART communication
- Proper sensor and board wiring (see below)

***

## Pin Configuration

| **Board Pins** | **Sensor Pins** |
|:---:|:---:|
| 3V3 | VCC |
| ADCO | DO (digital output) |
| GND | GND |

| **Board Pins** | **Programmer Pins** |
|:---:|:---:|
| RSTx | RXD |
| RSRx | TXD |
| GND | GND |

***

## Setup & Configuration

1. Wire the Hall Effect sensor to the 4G Data Logger Board as shown above.
2. Use a USB cable to connect the board to your PC and launch QPYCom.
3. Select the proper COM port (Quectel USB REPL), baud rate (e.g., 115200), and open port.
4. Upload project files (`main.py`, `systemconfig.json`, etc.) to the board.
5. If upload fails, interrupt running code via Ctrl+C in QPYCom REPL.
6. Open IoT Serial Monitoring App, enter COM port, baud rate, sensor selection, and interval configuration.
7. Monitor magnetic field state and analog values in real time.

***

## Sample Output

```
Connected to COM4 at 115200 baud
Hall Sensor State0, AO2735
Hall Sensor State0, AO2734
Hall Sensor State0, AO2731
...
Hall Sensor Low Not Detected
```
Sensor digital state and analog readings are displayed and visualized in the IoT Serial Monitoring App.

***

## Usage

1. Flash firmware to the 4G Data Logger Board.
2. View state changes and analog output from the Hall Effect sensor in the serial console and app.
3. Change data interval, COM port, and settings in the app as needed.

***

## Troubleshooting

- **Sensor Not Detected:**  
  - Confirm wiring (especially VCC, DO, GND) and configuration.
  - Verify correct COM port and baud rate.
- **Upload/REPL Issues:**  
  - Stop old code runs with Ctrl+C before re-uploading firmware.
- **State/Reading Errors:**  
  - Ensure correct power and magnetic field presence for Hall Effect detection.

***

## License

Project is released under an open-source license. See LICENSE file for full terms.

***
