(Just to be clear, I will be paying for this project myself)

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

| Board | Line | Designator | Qty | Info | Part | Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cam hat | 1 | C1, C4, C5, C7, C8, C10 | 6 | - | 10uF MLCC 0805 16V+ | (https://www.lcsc.com/search?q=10uF+0805) |
| Cam hat | 2 | C2 | 1 | - | 100pF MLCC 0402 NP0/C0G | (https://www.lcsc.com/search?q=100pF+0402+C0G) |
| Cam hat | 3 | C3, C6, C9, C11, C12, C13, C14, C15, C16, C17 | 10 | - | 100nF MLCC 0402 | (https://www.lcsc.com/search?q=100nF+0402) |
| Cam hat | 4 | D1 | 1 | Green LED | LED 0603 | (https://www.lcsc.com/search?q=LED+0603+green) |
| Cam hat | 5 | D2 | 1 | Red LED | LED 0603 | (https://www.lcsc.com/search?q=LED+0603+red) |
| Cam hat | 6 | D3 | 1 | - | PRTR5V0U2X,215 | (https://www.lcsc.com/product-detail/C12333.html) |
| Cam hat | 7 | J1 | 1 | USB C | HRO TYPE-C-31-M-12 | (https://www.lcsc.com/search?q=TYPE-C-31-M-12) |
| Cam hat | 8 | J3 | 1 | GPIO | 2.54mm 1x9 pin header | (https://www.lcsc.com/search?q=pin+header+1x9+2.54mm) |
| Cam hat | 9 | J4 | 1 | Mezzanine 2x15 conn (cam) | Hirose DF40C-30DS-0.4V | (https://www.lcsc.com/search?q=DF40C-30DS-0.4V) |
| Cam hat | 10 | R1, R2 | 2 | - | 5.1k resistor 0402 | (https://www.lcsc.com/search?q=5.1k+0402) |
| Cam hat | 11 | R3 | 1 | - | 1M resistor 0402 | (https://www.lcsc.com/search?q=1M+0402+resistor) |
| Cam hat | 12 | R4, R5 | 2 | - | 4.7k resistor 0402 | (https://www.lcsc.com/search?q=4.7k+0402) |
| Cam hat | 13 | R6, R7 | 2 | - | 68 ohm resistor 0402 | (https://www.lcsc.com/search?q=68R+0402+resistor) |
| Cam hat | 14 | R8, R9, R10 | 3 | - | 10k resistor 0402 | (https://www.lcsc.com/search?q=10k+0402) |
| Cam hat | 15 | SW1 | 1 | push button | Tactile switch TL3342 | (https://www.lcsc.com/search?q=TL3342+tactile+switch) |
| Cam hat | 16 | SW2, SW3 | 2 | push button (smaller) | Tactile switch B3U-1000P | (https://www.lcsc.com/search?q=B3U-1000P) |
| Cam hat | 17 | U1 | 1 | - | AMS1117-3.3 | (https://www.lcsc.com/product-detail/C6186.html) |
| Cam hat | 18 | U2 | 1 | - | AMS1117-1.8 | (https://www.lcsc.com/product-detail/C6185.html) |
| Cam hat | 19 | U3 | 1 | - | ESP32-S3 | (https://jlcpcb.com/partdetail/EspressifSystems-ESP32S3/C2913192) |
| Cam hat | 20 | Camera Module | 1 | - | OV5647 5MP CSI Camera Module | (https://www.sunfounder.com/products/ov5647-camera-module) |
| Cam hat | - | PCBA order | - | +94 usd | - | - |
| Motor hat | 21 | C1, C2 | 2 | - | 22pF MLCC 0402 NP0 | (https://www.lcsc.com/search?q=22pF+0402+NP0) |
| Motor hat | 22 | C3, C4, C10, C11, C12, C13, C14, C15 | 8 | - | 100nF MLCC 0402 | (https://www.lcsc.com/search?q=100nF+0402) |
| Motor hat | 23 | C5, C8, C9 | 3 | - | 10uF MLCC 0805 | (https://www.lcsc.com/search?q=10uF+0805) |
| Motor hat | 24 | C6, C16, C17 | 3 | - | 100uF electrolytic / ceramic 1210 | (https://www.lcsc.com/search?q=100uF+1210) |
| Motor hat | 25 | C7 | 1 | - | 220uF electrolytic 1210 | (https://www.lcsc.com/search?q=220uF+1210) |
| Motor hat | 26 | D1 | 1 | - | Schottky diode SMA package | (https://www.lcsc.com/search?q=schottky+diode+SMA) |
| Motor hat | 27 | J1 | 1 | GPIO | 2.54mm 1x4 pin header | (https://www.lcsc.com/search?q=pin+header+1x4+2.54mm) |
| Motor hat | 28 | J2 | 1 | Motor A | JST EH 2-pin vertical | (https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| Motor hat | 29 | J3 | 1 | Motor B | JST EH 2-pin vertical | (https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| Motor hat | 30 | J4 | 1 | Motor C | JST EH 2-pin vertical | (https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| Motor hat | 31 | J5 | 1 | Batt input | JST EH 2-pin vertical | (https://www.lcsc.com/search?q=B2B-EH-A+JST) |
| Motor hat | 32 | J6 | 1 | ISP | 2.54mm 2x3 pin header | (https://www.lcsc.com/search?q=pin+header+2x3+2.54mm) |
| Motor hat | 33 | L1 | 1 | - | Power inductor 2512 | (https://www.lcsc.com/search?q=power+inductor+2512) |
| Motor hat | 34 | R1, R2, R3 | 3 | - | 10k resistor 0402 | (https://www.lcsc.com/search?q=10k+0402) |
| Motor hat | 35 | U1 | 1 | - | ATMEGA328P-AU | (https://www.lcsc.com/product-detail/C14877.html) |
| Motor hat | 36 | U2, U3 | 2 | - | TB6612FNG | (https://www.lcsc.com/product-detail/Motor-Driver-ICs_TOSHIBA-TB6612FNG-C-8-EL_C141517.html) |
| Motor hat | 37 | U4 | 1 | - | LM2596S-5.0/NOPB | (https://www.lcsc.com/product-detail/C116713.html) |
| Motor hat | 38 | U5 | 1 | - | LD1117S33TR | (https://lcsc.com/product-detail/Linear-Voltage-Regulators-LDO_STMicroelectronics-LD1117S33TR_C86781.html) |
| Motor hat | 39 | Y1 | 1 | 16MHz Crystal | X322516MOB4SI 16MHz | (https://www.lcsc.com/product-detail/C12668.html) |
| Motor hat | - | PCBA order | - | +97 usd | - | - |
| Other | 40 | DC 6V Motor | 3 | - | 3V–6V brushed DC toy motor (TT gearmotor) | (https://www.lcsc.com/search?q=DC+motor+toy) |
| Other | 43 | Battery | 1 | for motors and rest of the system | 7.4V 2S LiPo ~1500–2200mAh | (https://www.aliexpress.com/item/1005007342294070.html) |
| Other | 44 | Spring | 4 | for suspension | 35mm × 10mm steel compression springs | (https://www.rays-teksurplus.co.uk/2-x-helical-compression-springs-steel-length-35mm-diameter-10mm-f3-13337-p.asp) |
