# FlexFan
FlexFan is a PWM controlled fan unit witch can turn into any kind of fan you would like using PVC drain pipes and 3D-printed parts!

For this project i have used a [delta fan](https://www.delta-fan.com/pfr0912xhe-sp00.html) rated 4.5A. But any PWM controllable fan that fit in the 93x93mm space will work. By modificating some of the parts a littel, you should also be able to use another size for the drain pipes, the original design is made for 110mm diameter.

Except the 3D-printed parts you wioll need:
* Board + skrews for mounting
* Fan
  * A PWM fan smaller than 93x93mm
  * PVC pipes 110mm of your choice
  * M4 skrews with matching nuts (can be replaced with glue)
  * A powersupply enugh to mpower the fan, i used [Mean Well lpv-60-12](https://www.meanwell.com/Upload/PDF/LPV-60/LPV-60-SPEC.PDF)
* 5v power
  * 220v socket
  * 5v transformator (standard usb charger)
  * usb-A to micro-usb
  #### or
  * dc-dc 12v to 5v buck converter
* Control unit
  * Raspberry pi pico
  * 5v relay
  * 2x 2n2222a transistor
* UI (optional)
   * 5x 3v LED + current limiting resistor
   * Button to set timer
   * DIP switch 4pos, fan setting
   * Lever, power
 

>This work is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
>
>You are free to:
>- Share — copy and redistribute the material in any medium or format
>- Adapt — remix, transform, and build upon the material
>
>Under the following terms:
>- Attribution — You must give appropriate credit.
>- NonCommercial — You may not use the material for commercial purposes.
