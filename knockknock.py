
import soundfile as sf
import sounddevice as sd

filePath="C:\\Users\\amadan7\\Downloads\\knock.wav"
data,fs=sf.read(filePath,dtype='float32')

print("Hello to knock knock application")
tint=int(input("Enter the time interval"))

def knockknock(tint):
    ticks=0
    count=0
    
    while(ticks<=tint):
        
        if(ticks!=tint):
            print(ticks)
            
            ticks=ticks+1
            continue
        else:
            print("Completed")
            while(count!=tint):
                sd.play(data,fs)
                sd.wait()
                count=count+1
            break
        



knockknock(tint)



