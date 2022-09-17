from pygame import mixer
import geocoder
from datetime import date, datetime
import prayerTime as pt
import time


def getLocationData():
    global city, coordinate, currentDate, UTC_offset

    ip = geocoder.ip("me")
    city = ip.city
    coordinate = ip.latlng
    currentDate = date.today()

    ts = time.time()
    UTC_offset = ((datetime.fromtimestamp(ts) -  datetime.utcfromtimestamp(ts)).total_seconds())/3600
    
    

    print("City: ", city)

def updatePrayerTime():
    global fazar_time, duhar_time, asar_time, magrib_time, isha_time, prayer_times

    prayTimes = pt.PrayTimes()
    prayer_times = prayTimes.getTimes(date.today(), coordinate, UTC_offset)    
    fazar_time   = str(prayer_times["fajr"])
    duhar_time   = str(prayer_times["dhuhr"]) 
    asar_time    = str(prayer_times["asr"])
    magrib_time  = str(prayer_times["maghrib"]) 
    isha_time    = str(prayer_times["isha"])
    print(prayer_times)



if __name__=="__main__":
    getLocationData()
    updatePrayerTime()
    mixer.init()


    while True:
        try:
            
            if currentDate != date.today():
                updatePrayerTime()
            
            nowHour = datetime.now().hour
            nowMin  = datetime.now().minute

            if nowHour<10:
                nowHour='0' + str(nowHour) 
            if nowMin<10:
                nowMin='0' + str(nowMin)  



            currentTime = str(nowHour) + ":" +str(nowMin)
            
            if currentTime == fazar_time:
                fazarAzan = mixer.Sound('Fajar.wav')
                fazarAzan.play()

            elif  currentTime == duhar_time or currentTime == asar_time or currentTime == magrib_time or currentTime == isha_time :
                otherAzan = mixer.Sound('azan1.wav')
                otherAzan.play()
                

            time.sleep(10)
            
            print("TIME -> ", currentTime, "\tDate -> ", date.today(), "\tPrayer time ->", prayer_times)
        
        except KeyboardInterrupt:
            print("Exciting....")
            exit()



