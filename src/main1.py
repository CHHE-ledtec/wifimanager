print("normal run")

# Here you can do your stuff
import oled_display

display_scl = Pin(22)
display_sda = Pin(21)
oled = oled_display.init_display(display_scl, display_sda)
oled.text('Display on', 0, 10)
oled.show()
#        oled.scroll(0,-11)
#        oled.text(str(i), 0, 49)
#        oled.show()
