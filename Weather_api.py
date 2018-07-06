import pyowm

owm = pyowm.OWM('a37d52498d921ddd4cc6a66b903ce12f')
observation = owm.weather_at_place('koforidua,ghana')
w = observation.get_weather()
observationc = owm.weather_at_place('koforidua,ghana')
wc = observationc.get_location()

print "The Wind level is " + str(w.get_wind())
print "The temperature level is " + str(w.get_temperature()['temp'] - 273)
print "The Pressure Level is " + str(w.get_pressure()['press'])
print "The humidity level is " + str(w.get_humidity())

print "The highest city  is " + str(c.get_pressure())

