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

# SDRAM Example
``python3 test_sdram.py`` programs a an example to test
the ULX3S's SDRAM memory into the ULX3S.

And nMigen wrapper around ``sdram/sdram_controller.v`` is
provided in ``sdram_controller.py``. It should be pretty
easy to browse ``sdram_controller.py`` and determine how
to interface with the SDRAM. Note that the SDRAM controller
has no burst mode support at the moment.

After programming the ULX3s with ``test_sdram.py``, you 
should be able to press the right button below the LED's
on the ULX3s and see the values in a loop in the following
pattern:

 - 0x78
 - 0x56
 - 0x34
 - 0x12

The controller writes ``0x12345678``
to the SDRAM, reads it back, and displays a byte at a time
to the LEDs. Once the four bytes finish displaying, the state
machine restarts by writing 0x12345678 and continues the 
write-read-display loop.

The SDRAM controller present a memory with 4-byte lines.
0x0 and 0x4 are seperated by 4-bytes.
The SDRAM controller presents a total of 8,388,608 lines
or addresses.
Thus the controller presents a total of 32MiBs in the memory.
