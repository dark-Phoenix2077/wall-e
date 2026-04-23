# Wiring diagram

Battery → Motor Hat

| Battery | Motor Hat (J5) |
|---|---|
| + (positive) | J5 Pin 1 (+VMOT) |
| − (negative) | J5 Pin 2 (GND) |

* XT30 connector + short pigtail

Motor Hat → Raspberry Pi (J1 jumper wires — 4 wires only)

| Motor Hat (J1) | Pi Physical Pin | Net |
|---|---|---|
| J1 Pin 2 | Pin 2 | +5V (board powers Pi) |
| J1 Pin 6 | Pin 6 | GND |
| J1 Pin 3 | Pin 3 (BCM 2) | SDA |
| J1 Pin 5 | Pin 5 (BCM 3) | SCL |

Motor Hat → Motors

| Motor Hat | Motor |
|---|---|
| J2 Pin 1 | Rear Left + |
| J2 Pin 2 | Rear Left − |
| J3 Pin 1 | Rear Right + |
| J3 Pin 2 | Rear Right − |
| J4 Pin 1 | Front Steering + |
| J4 Pin 2 | Front Steering − |

Camera Hat → Raspberry Pi

USB-C

| Camera Hat | Pi |
|---|---|
| USB-C port | any USB-A port on Pi |

J3 GPIO ribbon (9-pin, 2.54mm)

| Camera Hat (J3) | Pi Physical Pin | Pi GPIO | Direction |
|---|---|---|---|
| Pin 1 (GND) | Pin 6 | — | — |
| Pin 2 (+3V3) | Pin 1 | — | reference only, not powering board |
| Pin 3 (PI_PWDN) | Pin 11 | GPIO 17 | Pi → Hat |
| Pin 4 (PI_RESET) | Pin 13 | GPIO 27 | Pi → Hat |
| Pin 5 (LED1_PWM) | Pin 15 | GPIO 22 | Pi → Hat |
| Pin 6 (LED2_PWM) | Pin 29 | GPIO 5 | Pi → Hat |
| Pin 7 (BTN_OUT) | Pin 31 | GPIO 6 | Hat → Pi |
| Pin 8 (UART_RX) | Pin 10 | GPIO 15 | Hat → Pi |
| Pin 9 (UART_TX) | Pin 8 | GPIO 14 | Pi → Hat |

Camera Module → Camera Hat

| Camera Module | Camera Hat (J4) |
|---|---|
| ribbon cable | J4 (2×15 OddEven connector) |
