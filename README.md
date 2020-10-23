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

# Serial Example

Forms a serial loopback between the ULX3S and the
host computer. You will need to plug in the ULX3S
USB2 as well as the USB1 into the host machine for
this to work.

Once the loopback bitstream is flashed to the ULX3S,
you should see a new ACM tty device under ``/dev`` on
most unix machines. You can use ``screen /dev/tty.XXX``
to connect to it.

You can also flash the bitstream to the FPGA using
``openFPGALoader -b ulx3s -f build/top.bit``.

Now, you can unplug the ULX3s and only plug US2 into
the host machine. The serial loopback should still work
with screen.