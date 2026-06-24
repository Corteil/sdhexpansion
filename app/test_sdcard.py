from machine import SDCard
from system.hexpansion.config import HexpansionConfig
import vfs

# absolute bare minimum code to get the SD card mounted at /sd
# you need to call this function with the number of the hexpansion slot
# that you have plugged in to

def testsdcard(hexp_id):
    config = HexpansionConfig(hexp_id)
    
    # set up the SPI device, we specify all the pins and max out at 10MHz
    # SPI 2 is used for the CTX graphics driver, SPI1 can be used by python code
    #hspi = SPI(1, 10000000, sck=self.config.pin[1], mosi=self.config.pin[2], miso=self.config.pin[3])

    # SD card power switch must turn on (active low = off) first
    config.ls_pin[0].init(config.ls_pin[0].OUT)
    config.ls_pin[0].on()

    sd = SDCard(slot=3, sck=config.pin[2], cs=config.pin[0], mosi=config.pin[1], miso=config.pin[3])

    vfs.mount(sd, "/sd")
