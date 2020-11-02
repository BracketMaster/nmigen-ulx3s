from nmigen import *
from maeri.gateware.platform.ulx3s.ulx3s85f import ULX3S_85F_Platform


class Switch(Elaboratable):
    def elaborate(self, platform):

        m = Module()
        for count in range(4):
            led = platform.request("led", count)
            sw = platform.request("switch", count)
            m.d.comb += led.eq(sw)

        return m


if __name__ == "__main__":
    platform = ULX3S_85F_Platform()
    platform.build(Switch(), do_program=True)