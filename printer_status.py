import utime
from machine import Pin, SPI, idle
from PyRepRapComm import pyRepRapComm
import network
import st7920

##### SETUP CODE #####
main_screen_layout = [(4, 8, "Bed Temp:"),
                      (4, 16, "Noz Temp:"),
                      (4, 24, "X:"),
                      (60, 24, "Z:"),
                      (4, 32, "Y:"),
                      (4, 40, "Status:")]

# Setup SPI for the screen
vspi = SPI(2, baudrate=600000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(16, Pin.OUT)
screen = st7920.Screen(spi=vspi, slaveSelectPin=Pin(16))
screen.clear()
screen.redraw()
plot = screen.create_plotter()
unplot = screen.create_plotter(False)

# Setup Wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("WackyWednesday", "c3l3str0")

# Splash Screen while we wait forwifi connect
screen.write_string(22, 10, "RepRapFirmware", plot)
screen.write_string(24, 20, "Status Viewer", plot)
screen.write_string(20, 40, "By: Kurt Telep", plot)
screen.write_string(14, 50, "ktelep@gmail.com", plot)
screen.redraw()

print('Waiting for WLAN connection')
while not wlan.isconnected():
    idle() # save power while waiting
print('WLAN connection succeeded!')
utime.sleep_ms(3000)

# Connect to printer
printer = pyRepRapComm('192.168.1.73')
p_status = None

def draw_meter_graphical(perc, x1, y1, x2, y2, with_text=True):

    meter_width = None
    screen.fill_rect(x1, y1, x2, y2, unplot)

    if with_text:
        meter_width = (x2 - x1) - 21  # four characters for full meter
        text_x = x2 - 19
        if y2-y1 > 6:
            y2 = y1+6   # If we're displaying text, force font height

        # Write the text
        if perc < 100:  # Center if less than 100%
            screen.write_string(text_x+3, y1, str(perc)+'%', plot)
        else:
            screen.write_string(text_x, y1, str(perc)+'%', plot)
    else:
        meter_width = x2 - x1

    screen.rect(x1, y1, x1+meter_width, y2, plot)  # Outline of meter
    fill_amount = int(meter_width * (perc / 100))
    screen.fill_rect(x1, y1, x1+fill_amount, y2, plot)   # Meter Amount


def write_name(name="3D Printer"):
    """ Writes the name of the printer centered on the top row """
    screen.fill_rect(0, 0, 127, 7, plot)
    name_width = (len(name) * 6) - 1  # name width in pixels
    x1 = (124 - name_width) // 2
    screen.write_string(x1, 0, name, unplot)

def update_temps():
    temps = printer.get_printer_temps(p_status)
    screen.write_string(60, 8, temps["bed"]["formatted"], plot)
    screen.write_string(60, 16, temps["heads"][0]["formatted"], plot)

def update_pos():
    pos = printer.get_printer_position(p_status)
    screen.write_string(16, 24, str(pos[0]), plot)
    screen.write_string(16, 32, str(pos[1]), plot)
    screen.write_string(72, 24, str(pos[2]), plot)

def update_status():
    stat = printer.get_printer_status(p_status)
    print(stat[1])
    screen.write_string(46, 40, stat[1], plot)
    screen.write_string(4, 48, "GCODE FILE NAME HERE", plot)
    screen.write_string(4, 56, "123:45:67", plot)
    draw_meter_graphical(50, 59, 56, 123, 63)

def layout_mainscreen():
    for i in main_screen_layout:
        screen.write_string(i[0], i[1], i[2], plot)

def update_mainscreen():
    try:
        global p_status
        old_status = p_status
        p_status = printer.get_status_info(2)
    except OSError:
        print("Unable to get info")
        return

    screen.clear()
    layout_mainscreen()
    write_name("HyperCube Evolution")
    update_temps()
    update_pos()
    update_status()
    screen.redraw()

screen.clear()
layout_mainscreen()
screen.redraw()

#### ACTIVE LOOP ####
while True:
    utime.sleep_ms(1000)
    update_mainscreen()

