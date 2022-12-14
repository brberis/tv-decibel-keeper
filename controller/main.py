import time
import audioop
import math
import pyaudio
# with open('config.yml', 'r') as ymlfile:
#     CFG = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16 #CFG['audio']['format']
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=False,
                frames_per_buffer=CHUNK)

done = False

ac = 0
samples = []
avg = 0
max_db = 0

def ag_samples(sample):
    ''' collect samples and average if needed. '''
    global ac
    global samples
    global avg
    global max_db

    if ac < 1:
        if sample > 1:
            samples.append(sample)
            ac = ac+1
    else:
        avg = sum(samples) / len(samples)
        if float(avg) > float(max_db):
            max_db = "%.2f" % avg
        ac = 0
        samples = []

    return "%.2f" % avg

i = 0
sm = 0
while not done:

    total = 0
    data = stream.read(CHUNK,
                       exception_on_overflow=False)
    reading = audioop.max(data, 2)

    #dB scale
    total = 20 * (math.log10(abs(reading)))

    db = ag_samples(total)

    print(db)

    sm = (sm + float(db))     
    i += 1
    if i == 30:
        i = 0
        print('THE AVERAGE ' + str(sm / 30 ))
        sm = 0
        
    time.sleep(.005)

#clearing the resources
stream.stop_stream()
stream.close()
p.terminate()
