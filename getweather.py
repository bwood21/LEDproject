import pywapi

weather = pywapi.get_weather_from_weather_com('USIN0707')

temp = weather['current_conditions']['temperature']
condition = weather['current_conditions']['text'].lower()

farhTemp = (float(temp) * 1.8) + 32

print "West Lafayette: "
print "    Condition: " + condition
print "    Temperature: %.0f F" % (farhTemp)
