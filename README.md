# wall-e
a custom smart rover with vision-assisted autonomous navigation and object tracking, built around a Raspberry Pi 3B+ and two fully custom PCB HATs.

<img width="753" height="580" alt="Screenshot 2026-04-23 at 11 15 12 pm" src="https://github.com/user-attachments/assets/0d08e636-d8c2-46cb-86b8-48581a6f3f63" />

# Why I built this
I built this to push myself towards more advanced PCBs and more complex automated systems/ I wanted to try making a fun toy that could also teach me a lot about PCB design and CAD - this being some of my more complex CAD work, especially for the suspension.

# What the project is
Wall-e is a 3D printed rover with custom wheels and suspension powered by a raspberry pi 3b+, as well as two custom PCBs - one for vision, and one for motor control/PD. 

it consists of:

The motor/PD PCB - a tiny little PCB that takes in a battery and 3 motors, and controls them via an ATmega chip, accepting high-level commands from the pi via gpio. it also pushes power to the pi from its own battery:

<img width="1024" height="580" alt="Screenshot 2026-04-23 at 11 21 24 pm" src="https://github.com/user-attachments/assets/b263a01d-1f03-441a-a410-14402280e4bc" />

The vision PCB - a board with an esp32 and a pi camera, as well as usb c and gpio. it communicates mainly via usb c providing a usb camera feed to the pi (translated via the esp32), and uses the gpio for util functions. it has an adressable button (likelly will use for debugging/emergency shutdown purposes) and two status LEDs:

<img width="1024" height="751" alt="Screenshot 2026-04-23 at 11 23 19 pm" src="https://github.com/user-attachments/assets/f881ec33-d26b-4df7-814c-c05fb7c7e981" />

The cad - houses all of it, has a 2 point suspension thingy (idk the proper term):

<img width="773" height="585" alt="Screenshot 2026-04-23 at 11 24 04 pm" src="https://github.com/user-attachments/assets/9e620d3a-6ad0-4b31-89ad-199691c2a34a" />

Code - currently two test scripts for colour tracking and line following, will start with those and might expand after I get them working - untested on hardware

# BOM

cam PCB

| Line | Designator | Footprint | Qty | Value / Designation | Suggested Part | Supplier / Ref | Link |
|---:|---|---|---:|---|---|---|---|
| 1 | C1, C4, C5, C7, C8, C10 | C_0805_2012Metric | 6 | 10uF | 10uF MLCC 0805 16V+ | Generic | [LCSC search](https://www.lcsc.com/search?q=10uF+0805) |
| 2 | C2 | C_0402_1005Metric | 1 | 100pF | 100pF MLCC 0402 NP0/C0G | Generic | [LCSC search](https://www.lcsc.com/search?q=100pF+0402+C0G) |
| 3 | C3, C6, C9, C11–C17 | C_0402_1005Metric | 10 | 100nF | 100nF MLCC 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=100nF+0402) |
| 4 | D1 | LED_0603_1608Metric | 1 | Green LED | Green LED 0603 | Generic | [LCSC search](https://www.lcsc.com/search?q=LED+0603+green) |
| 5 | D2 | LED_0603_1608Metric | 1 | Red LED | Red LED 0603 | Generic | [LCSC search](https://www.lcsc.com/search?q=LED+0603+red) |
| 6 | D3 | SOT-143 | 1 | PRTR5V0U2X | PRTR5V0U2X,215 | Nexperia — LCSC C12333 | [LCSC C12333](https://www.lcsc.com/product-detail/C12333.html) |
| 7 | J1 | USB_C_Receptacle_HRO_TYPE-C-31-M-12 | 1 | USB-C Receptacle USB2.0 16P | HRO TYPE-C-31-M-12 | HRO | [LCSC search](https://www.lcsc.com/search?q=TYPE-C-31-M-12) |
| 8 | J3 | PinHeader_1x09_P2.54mm_Vertical | 1 | J_GPIO 1×9 | 2.54mm 1×9 pin header | Generic | [LCSC search](https://www.lcsc.com/search?q=pin+header+1x9+2.54mm) |
| 9 | J4 | Hirose_DF40C-30DS-0.4V_2x15_P0.4mm | 1 | Conn 2×15 Board-to-Board | Hirose DF40C-30DS-0.4V | Hirose | [LCSC search](https://www.lcsc.com/search?q=DF40C-30DS-0.4V) |
| 10 | R1, R2 | R_0402_1005Metric | 2 | 5.1k | 5.1k resistor 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=5.1k+0402) |
| 11 | R3 | R_0402_1005Metric | 1 | 1M | 1M resistor 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=1M+0402+resistor) |
| 12 | R4, R5 | R_0402_1005Metric | 2 | 4.7k | 4.7k resistor 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=4.7k+0402) |
| 13 | R6, R7 | R_0402_1005Metric | 2 | 68R | 68 ohm resistor 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=68R+0402+resistor) |
| 14 | R8, R9, R10 | R_0402_1005Metric | 3 | 10k | 10k resistor 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=10k+0402) |
| 15 | SW1 | SW_SPST_TL3342 | 1 | SW_Push | Tactile switch TL3342 | Generic | [LCSC search](https://www.lcsc.com/search?q=TL3342+tactile+switch) |
| 16 | SW2, SW3 | SW_SPST_B3U-1000P | 2 | SW_Push | Tactile switch B3U-1000P | Omron | [LCSC search](https://www.lcsc.com/search?q=B3U-1000P) |
| 17 | U1 | SOT-223-3_TabPin2 | 1 | AMS1117-3.3 | AMS1117-3.3 | AMS — LCSC C6186 | [LCSC C6186](https://www.lcsc.com/product-detail/C6186.html) |
| 18 | U2 | SOT-223-3_TabPin2 | 1 | AMS1117-1.8 | AMS1117-1.8 | AMS — LCSC C6185 | [LCSC C6185](https://www.lcsc.com/product-detail/C6185.html) |
| 19 | U3 | QFN-56-1EP_7x7mm_P0.4mm_EP4x4mm | 1 | ESP32-S3 | ESP32-S3 | Espressif — JLCPCB C2913192 | [JLCPCB C2913192](https://jlcpcb.com/partdetail/EspressifSystems-ESP32S3/C2913192) |
| 20 | Camera Module | CSI FPC module | 1 | OV5647 RPi Camera | OV5647 5MP CSI Camera Module | SunFounder | [SunFounder product page](https://www.sunfounder.com/products/ov5647-camera-module) |

motor/PD PCB

| Line | Designator | Footprint | Qty | Value / Designation | Suggested Part | Supplier / Ref | Link |
|---:|---|---|---:|---|---|---|---|
| 21 | C1, C2 | C_0402_1005Metric | 2 | 22pF | 22pF MLCC 0402 NP0 | Generic | [LCSC search](https://www.lcsc.com/search?q=22pF+0402+NP0) |
| 22 | C3, C4, C10–C15 | C_0402_1005Metric | 8 | 100nF | 100nF MLCC 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=100nF+0402) |
| 23 | C5, C8, C9 | C_0805_2012Metric | 3 | 10uF | 10uF MLCC 0805 | Generic | [LCSC search](https://www.lcsc.com/search?q=10uF+0805) |
| 24 | C6, C16, C17 | C_1210_3225Metric | 3 | 100uF | 100uF cap 1210 low-ESR | Generic | [LCSC search](https://www.lcsc.com/search?q=100uF+1210) |
| 25 | C7 | C_1210_3225Metric | 1 | 220uF | 220uF cap 1210 | Generic | [LCSC search](https://www.lcsc.com/search?q=220uF+1210) |
| 26 | D1 | D_SMA | 1 | D_Schottky | Schottky diode SMA | Generic | [LCSC search](https://www.lcsc.com/search?q=schottky+diode+SMA) |
| 27 | J1 | PinHeader_1x04_P2.54mm_Vertical | 1 | J_PI_GPIO 1×4 | 2.54mm 1×4 pin header | Generic | [LCSC search](https://www.lcsc.com/search?q=pin+header+1x4+2.54mm) |
| 28 | J2 | JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical | 1 | Motor_A_Rear_Left | JST EH 2-pin vertical | JST | [LCSC search](https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| 29 | J3 | JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical | 1 | Motor_B_Rear_Right | JST EH 2-pin vertical | JST | [LCSC search](https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| 30 | J4 | JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical | 1 | Motor_C_Steering | JST EH 2-pin vertical | JST | [LCSC search](https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| 31 | J5 | JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical | 1 | VMOT_Battery_Input | JST EH 2-pin vertical | JST | [LCSC search](https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| 32 | J6 | PinHeader_2x03_P2.54mm_Vertical | 1 | ISP_Header 2×3 | 2.54mm 2×3 pin header | Generic | [LCSC search](https://www.lcsc.com/search?q=pin+header+2x3+2.54mm) |
| 33 | L1 | L_2512_6332Metric | 1 | L (Power Inductor) | Power inductor 2512 | Generic | [LCSC search](https://www.lcsc.com/search?q=power+inductor+2512) |
| 34 | R1, R2, R3 | R_0402_1005Metric | 3 | 10k | 10k resistor 0402 | Generic | [LCSC search](https://www.lcsc.com/search?q=10k+0402) |
| 35 | U1 | TQFP-32_7x7mm_P0.8mm | 1 | ATmega328P-A | ATMEGA328P-AU | Microchip — LCSC C14877 | [LCSC C14877](https://www.lcsc.com/product-detail/C14877.html) |
| 36 | U2, U3 | SSOP-24_5.3x8.2mm_P0.65mm | 2 | TB6612FNG | TB6612FNG | Toshiba — LCSC C141517 | [LCSC C141517](https://www.lcsc.com/product-detail/Motor-Driver-ICs_TOSHIBA-TB6612FNG-C-8-EL_C141517.html) |
| 37 | U4 | SOIC-8_3.9x4.9mm_P1.27mm | 1 | LM2596S-5.0 | LM2596S-5.0/NOPB | TI — LCSC C116713 | [LCSC C116713](https://www.lcsc.com/product-detail/C116713.html) |
| 38 | U5 | SOT-223-3_TabPin2 | 1 | LD1117S33TR | LD1117S33TR | ST — LCSC C86781 | [LCSC C86781](https://lcsc.com/product-detail/Linear-Voltage-Regulators-LDO_STMicroelectronics-LD1117S33TR_C86781.html) |
| 39 | Y1 | Crystal_SMD_3225-4Pin_3.2x2.5mm | 1 | 16MHz | X322516MOB4SI | YXC — LCSC C12668 | [LCSC C12668](https://www.lcsc.com/product-detail/C12668.html) |

other stuff

| Line | Item | Qty | Suggested Part | Link | Notes |
|---:|---|---:|---|---|---|
| 40 | Rear Left Drive Motor | 1 | 3V–6V brushed DC TT gearmotor | [LCSC search](https://www.lcsc.com/search?q=DC+motor+toy) | Match output shaft to chassis |
| 41 | Rear Right Drive Motor | 1 | 3V–6V brushed DC TT gearmotor | [LCSC search](https://www.lcsc.com/search?q=DC+motor+toy) | Matched pair with Motor A |
| 42 | Steering Motor | 1 | 3V–6V brushed DC TT gearmotor | [LCSC search](https://www.lcsc.com/search?q=DC+motor+toy) | Matched pair with Motor A/B |
| 43 | Battery | 1 | 7.4V 2S LiPo ~1500–2200mAh | [AliExpress example](https://www.aliexpress.com/item/1005007342294070.html) | Feeds motor rail; LM2596S bucks to 5V for Pi |
| 44 | Compression Springs | 4 | 35mm × 10mm dia steel spring | [Rays-TekSurplus example](https://www.rays-teksurplus.co.uk/2-x-helical-compression-springs-steel-length-35mm-diameter-10mm-f3-13337-p.asp) | 4 pcs; also search Amazon/AliExpress for multi-packs |

