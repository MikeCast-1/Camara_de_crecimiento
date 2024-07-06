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
lcd.create_char(0, deg)

TEMP_POS =[0,0]
HUM_POS = [0,12]

SOIL_POS=[1,0]

PELTIER_POS =[2,0]

LIGHT_POS =[3,0]
PUMP_POS =[3,9]

def print_temp(tempVal):
	lcd._set_cursor_pos(TEMP_POS)
	lcd.write_string('Temp:')
	temp_char = str(tempVal)
	lcd.write_string(temp_char)
	lcd.write(0)
	lcd.write_string('C')

def print_hum(humVal):
	lcd._set_cursor_pos(HUM_POS)
	lcd.write_string('Hum:')
	hum_char = str(humVal)
	lcd.write_string(hum_char)
	lcd.write_string('%')

def print_soil_hum(soilVal):
	lcd._set_cursor_pos(SOIL_POS)
	lcd.write_string('H_Suelo:')
	soil_char = str(soilVal)
	lcd.write_string(soil_char)
	lcd.write_string('%')

def print_light_status(status):
	lcd._set_cursor_pos(LIGHT_POS)
	lcd.write_string('Luz:')
	if status == 0:
		lcd.write_string('OFF')
	else:
		lcd.write_string('ON')

def print_pump_status(status):
	lcd._set_cursor_pos(PUMP_POS)
	lcd.write_string('Riego:')
	if status == 0:
		lcd.write_string('OFF')
	else:
		lcd.write_string('ON')

def print_peltier_status(status):
	lcd._set_cursor_pos(PELTIER_POS)
	lcd.write_string('Celda Peltier:')
	if status == 0:
		lcd.write_string('OFF')
	else:
		lcd.write_string('ON')
