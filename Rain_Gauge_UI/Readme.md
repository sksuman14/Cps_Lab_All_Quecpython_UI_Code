***

# Rain Gauge Sensor Interface – 4G Data Logger Board

This repository contains firmware and setup instructions for connecting a Rain Gauge sensor to the 4G Data Logger board. The project acquires rainfall measurements by converting analog pulses to digital counts and visualizes the data in real-time in the IoT Serial Monitoring App.

***

## Features

- Reads rainfall data from a Rain Gauge sensor (pulse counting / analog-to-digital conversion)
- Converts tip counts to digital rainfall measurements
- Displays real-time rainfall data and event logging using the IoT Serial Monitoring App
- Supports customizable logging intervals and live UART logging

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U recommended)
- Rain Gauge sensor (pulse-output or analog output)
- Programmer (for firmware upload and UART connection)
- USB cable (PC-board link)

***

## Software Requirements

- QPYCom (file upload, Python firmware loading, and REPL access)
- IoT Serial Monitoring App (live rainfall readings and visualization)
- Python runtime compatible with Quecpython v1.12 or newer

***

## Prerequisites

- Basic Python and embedded systems knowledge
- Understanding of analog/digital sensor interfacing and UART
- Correct wiring of sensor to board (see pin mapping below)

***

## Pin Configuration

| **Board Pins** | **Sensor Pins** |
|:---:|:---:|
| VBat (3V3) | Wire1 (Power) |
| ADCO | Wire2 (Signal) |
| GND | GND |

| **Board Pins** | **Programmer Pins** |
|:---:|:---:|
| RSTx | RXD |
| RSRx | TXD |
| GND | GND |

***

## Setup & Configuration

1. Wire the Rain Gauge sensor to the 4G Data Logger board as mapped above.
2. Connect the board to the PC via USB and open QPYCom.
3. Select the correct COM port (Quectel USB REPL), baud rate (e.g., 115200) and open the port.
4. Upload project files (`main.py`, and system configs) to the board.
5. If upload fails, press Ctrl+C in QPYCom REPL to halt existing code and retry.
6. Open the IoT Serial Monitoring App, enter COM port, baud rate, sensor, and interval settings.
7. Monitor rainfall counts and measurements live in the app and UART logs.

***

## Sample Output

```
Connected to COM4 at 115200 baud
Rain Tip Detected! Rainfall 10
Rain Tip Detected! Rainfall 11
Rain Tip Detected! Rainfall 12
...
OUTPUT: 10.5 mm
```
Rain tip events and cumulative rainfall (in mm) are displayed and logged in the IoT Serial Monitoring App.

***

## Usage

1. Flash the Rain Gauge firmware onto your 4G Data Logger Board.
2. Read and log rainfall events and totals in real time on the serial terminal or app.
3. Adjust interval, port, and sensor settings to match your monitoring requirements.

***

## Troubleshooting

- **No Data/Detection:**  
  - Confirm wiring, sensor alignment, and configuration.
  - Check COM port and baud rate settings.
- **Upload/REPL Issues:**  
  - Press Ctrl+C to stop any running firmware before uploading new code.
- **Incorrect Values:**  
  - Ensure sensor calibration and placement for precise measurements.

***

## License

Released under open-source license. See LICENSE file for terms.

***
