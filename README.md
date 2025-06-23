FlexFan:
The FlexFan is a PWM-controlled fan unit that can be adapted into various fan setups using PVC drain pipes and 3D-printed parts.

For this project, I used a Delta fan rated 4.5A. However, any PWM-controllable fan that fits in the 93x93 mm space will work. By modifying some of the parts a little, you should also be able to use a different size drain pipe; the original design is made for 110 mm diameter pipes.

In addition to the 3D-printed parts, you will need:

* A board and screws for mounting.
* Fan
  * A PWM fan smaller than 93x93 mm
  * PVC pipes, 110 mm, of your choice
  * M4 screws with matching nuts (can be replaced with glue).
  * A power supply capable to power the fan. I used a Mean Well LPV-60-12.
* 5V power
  * A 220V socket
  * 5V transformer (standard USB charger).
  * USB-A to Micro-USB
  #### Or
  * DC-DC 12V to 5V Buck Converter
* Control unit:
  * Raspberry Pi Pico
  * 5V relay
  * 2x 2N2222A transistors
* UI (optional):
  * 5x 3V LEDs and current-limiting resistors
  * A button to set the timer.
  * DIP switch, 4-position, for fan setting
  * Power switch
 

>This work is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
>
>You are free to:
>- Share — copy and redistribute the material in any medium or format
>- Adapt — remix, transform, and build upon the material
>
>Under the following terms:
>- Attribution — You must give appropriate credit.
>- NonCommercial — You may not use the material for commercial purposes.
