Second assignment

BOM:

Raspberry Pi 4

Breadboard

3x 220 Ohm resistor

RGB Led (with common (-))

Rotary encoder

9x wire

![image](https://github.com/tichyv/Second-assignment/assets/149083694/fa24cb5d-967f-4fa7-a346-d3a1668a7d9d)

RGB Led is inserted into J column of the breadboard. Next every row with catode needs to be connected to the second half of the breadboard using 220 Ohm resistor (resistors go in 1d-1f, 3d-3f and 4d-4f). First row is connected to pin 11 (GPIO 17), third row is connected to pin 13 (GPIO 27) and fourth row is connected to pin 15 (GPIO 22). Common anode is connected by linking 2f to pin 09.
To plug rotary encoder we need to connect VCC (+) to 3.3V on pin 17, ground to ground pin 34.
SIA is connected to pin 36 (GPIO 16), SIB is connected to pin 38 (GPIO 20) and SW is connected to pin 40 (GPIO 21). 

![395491629_309942601839648_6711018915088658323_n](https://github.com/tichyv/Second-assignment/assets/149083694/73535d95-1f86-4fb7-a9a8-91b4e4dfc307)

![395677355_886722466188627_346877357152447646_n](https://github.com/tichyv/Second-assignment/assets/149083694/5ec81c37-d718-49e6-a0a7-83969af9b780)
