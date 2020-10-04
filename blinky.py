from nmigen import *
from nmigen_boards.ulx3s import ULX3S_85F_Platform


class Blinky(Elaboratable):
    def elaborate(self, platform):
        user_led = platform.request("led", 0)
        counter  = Signal(23)

        m = Module()
        m.d.sync += counter.eq(counter + 1)
        m.d.comb += user_led.o.eq(counter[-1])
        return m


if __name__ == "__main__":
    platform = ULX3S_85F_Platform()
    platform.build(Blinky(), do_program=True)