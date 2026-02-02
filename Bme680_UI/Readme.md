***

# BME680 Sensor Interface – 4G Data Logger Board

This repository provides firmware and setup instructions to integrate the BME680 environmental sensor with the 4G Data Logger board. The solution supports real-time acquisition and visualization of temperature, humidity, and pressure readings via the IoT Serial Monitoring App.

***

## Features

- Acquires data from BME680:  
  - Temperature  
  - Humidity  
  - Pressure  

- Communicates over I2C interface for reliable sensor data gathering
- Designed for use with Quectel EC200U-based 4G Data Logger hardware
- Visualizes data in real time using IoT Serial Monitoring App
- Configurable logging intervals via the serial interface
- Supports soft reboots and error handling for robust operation

***

## Hardware Requirements

- 4G Data Logger Board (Quectel EC200U module recommended)
- BME680 Sensor (I2C interface)
- Programmer (for flashing and UART connection)
- USB cable (for board-PC connection)

***

## Software Requirements

- QPYCom (recommended for Python flashing and REPL access)
- IoT Serial Monitoring App
- Basic Python environment (Quecpython v1.12 supported)

***

## Prerequisites

- Basic Python knowledge
- Familiarity with sensor communication protocols (I2C, UART)
- Correct hardware wiring as described below

***

## Pin Configuration

| **Board Pins**  | **Sensor Pins** |
|:---------------:|:---------------:|
| 3V3             | VCC             |
| GND             | GND             |
| SDA             | SDA             |
| SCL             | SCL             |

| **Board Pins**  | **Programmer Pins** |
|:---------------:|:-------------------:|
| RSTx            | RXD                 |
| RSRx            | TXD                 |
| GND             | GND                 |

***

## Setup & Configuration

1. Connect the 4G Data Logger Board to your PC using the USB cable.
2. Wire the BME680 sensor to the board via I2C as shown above.
3. Open QPYCom on your PC. Select the COM port corresponding to the Quectel USB REPL.
4. Upload the firmware files (`main.py`, `bmedriver.py`, etc.) to the board.
5. To stop any running code in REPL, press Ctrl+C and retry uploading.
6. Launch the IoT Serial Monitoring App and select the appropriate COM port and baud rate.
7. Set the desired interval for data updates.

***

## Sample Output

```
Connected to COM61 at 115200 baud
BME680 Temperature 24.96°C, Pressure 983.53 hPa, Humidity 65.65%
BME680 Temperature 25.02°C, Pressure 983.69 hPa, Humidity 65.71%
BME680 Temperature 26.37°C, Pressure 983.77 hPa, Humidity 67.62%
```

Data is refreshed at user-defined intervals, and live charts visualize sensor values.

***

## Usage

1. Flash the firmware onto your 4G Data Logger Board.
2. The application starts reading BME680 sensor data and logs it to the serial console.
3. Use the IoT Serial Monitoring App to view and analyze results.
4. Adjust configuration settings (port, baud rate, interval) as needed in the app.

***

## Troubleshooting

- **Sensor Not Detected:**  
  - Verify physical connections and I2C address (default 0x76/0x77).  
  - Confirm interface and address settings in configuration.
- **REPL/Upload Issues:**  
  - Stop running code (Ctrl+C in REPL) before retrying.
- **Incorrect Readings:**  
  - Ensure sensor wiring and environmental conditions are appropriate.
  - Confirm sensor initialization in firmware.

***

## License

Released under an open-source license. See LICENSE file for details.

***
