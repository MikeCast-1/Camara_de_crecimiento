import LCD


temp = 25
hum = 63
soil = 73
light = True
pump = True
peltier = True

LCD.print_temp(temp)

LCD.print_hum(hum)

LCD.print_soil_hum(soil)

LCD.print_peltier_status(peltier)

LCD.print_light_status(light)

LCD.print_pump_status(pump)
