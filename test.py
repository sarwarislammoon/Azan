from pygame import mixer
import geocoder
from datetime import date, datetime
import prayerTime as pt
import time
import sys
import os

# Set stdout to line-buffered
sys.stdout = open(sys.stdout.fileno(), 'w', 1)



# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))


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
    prayTimes.adjust({"maghrib": "-5 min"})
    prayer_times = prayTimes.getTimes(date.today(), coordinate, UTC_offset)    
    fazar_time   = str(prayer_times["fajr"])
    duhar_time   = str(prayer_times["dhuhr"]) 
    asar_time    = str(prayer_times["asr"])
    magrib_time  = str(prayer_times["maghrib"]) 
    isha_time    = str(prayer_times["isha"])
    print(prayer_times)







if __name__=="__main__":
    try :
        getLocationData()
    except Exception as e:
        print(e)
    
    try :
        updatePrayerTime()
    except Exception as e:
        print(e)
    try :
        mixer.init()
    except Exception as e:
        print(e)
   
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
            
            if currentTime != fazar_time:
                try:
                    print(currentTime, ":\t", "Playing Fazar Azan")
                    fazarAzan = mixer.Sound('Fajar.wav')
                    channel=fazarAzan.play()
                    while channel.get_busy():
                            time.sleep(0.1)
                except Exception as e:  
                    print(e)
                    #print("Fail to play azan ...")


            elif  currentTime == duhar_time or currentTime == asar_time or currentTime == magrib_time or currentTime == isha_time :
                try:
                    print(currentTime, ":\t", "Playing Azan")
                    otherAzan = mixer.Sound('azan1.wav')
                    channel=otherAzan.play()
                    while channel.get_busy():
                            time.sleep(0.1)
                except Exception as e:  
                    print(e)
                    #print("Fail to play azan ...")

            time.sleep(10)
            
            print("TIME -> ", currentTime, "\tDate -> ", date.today(), "\tPrayer time ->", prayer_times)
        
        except KeyboardInterrupt:
            print("Exciting....")
            exit()



