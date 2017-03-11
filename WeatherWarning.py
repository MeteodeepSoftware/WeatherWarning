from time import sleep  #sleep functions
	
from sense_hat import SenseHat  #imports sense hat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()  #receives pressure
pressure = round(pressure, 1)
pressure = str(pressure)

if pressure <= "995":   #if statement
    target1 = open('/var/www/meteodeep/weatherwarning.txt', 'w')
    target1.write(pressure)
    target1.close()
    
elif pressure >= "996":
    target1 = open('/var/www/meteodeep/weatherwarning.txt', 'w')
    target1.write("No Current Weather Warning")
    target1.close()

else:
    print("ERROR")


from subprocess import call  #dropbox upload
Upload = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /var/www/meteodeep/weatherwarning.txt /WeatherWarning.txt"
call ([Upload], shell=True)


# crontab
# 0 * * * * sudo /usr/bin/python3 /var/www/meteodeep/LivePressure.py
