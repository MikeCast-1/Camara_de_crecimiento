from RPLCD.i2c import CharLCD

deg = (
                 0b11100,
                 0b10100,
                 0b11100,
                 0b00000,
                 0b00000,
                 0b00000,
                 0b00000,
                 0b00000,
            )


lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)
lcd.clear()

lcd._set_cursor_mode('blink')
lcd.create_char(0, deg)

Temp_pos =[0,0]
Hum_pos = [0,12]

Soil_pos=[1,0]

Lights_Pos =[3,0]
Pump_Pos =[3,8]

temp_val = 24
temp_char = str(temp_val)
hum_val = 65
hum_char = str(hum_val)

lcd.write_string('Temp:')
lcd.write_string(temp_char)
lcd.write(0)
lcd.write_string('C')

lcd._set_cursor_pos(Hum_pos)
lcd.write_string('Hum:')
lcd.write_string(hum_char)
lcd.write_string('%')

lcd._set_cursor_pos(Lights_Pos)
lcd.write_string('Luz:')
lcd.write_string('ON')

lcd._set_cursor_pos(Pump_Pos)
lcd.write_string('Riego:')
lcd.write_string('ON')

