# ULX3s by Example

Some quick ulx3s examples for the FPGA
using nMigen.

# Dependencies

You can install the following dependencies with
``pip3 install -r requirements.txt``

 - [nmigen](https://github.com/nmigen/nmigen)
 - [nmigen-boards](https://github.com/nmigen/nmigen-boards)

You will also need to build and install
[openFPGALoader](https://github.com/trabucayre/openFPGALoader)
to program the ULX3S.

# Running

Do ``python blinky.py`` and you should see D0 flashing
on the board.

Run ``switch.py`` and flipping one of the four switches
should now toggle up to four of the LEDs on the ULX3S
board.
