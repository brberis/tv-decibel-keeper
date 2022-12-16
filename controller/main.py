import time
import audioop
import math
import pyaudio
import yaml

from sonybraviaremote import TV, TVConfig

def on_auth():
    return input('Pincode: ')

config = TVConfig('192.168.50.226', 'Bravia')
tv = TV.connect(config, on_auth)

with open('../config.yml', 'r') as ymlfile:
    CFG = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    
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

    # print(db)

    sm = (sm + float(db))     
    i += 1
    if i == CFG['audio']['interval']:
        i = 0
        average = sm / CFG['audio']['interval']
        print('THE AVERAGE ' + str(average))
        if average > CFG['audio']['max_average']:
            print('HIT UP LIMIT')
            tv.volume_down(100)
            tv.volume_up(CFG['audio']['default_vol'])

        sm = 0
        
    time.sleep(.005)

#clearing the resources
stream.stop_stream()
stream.close()
p.terminate()
