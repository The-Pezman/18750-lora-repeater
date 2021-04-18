###There's something wrong with the normal rak811 library for the recently produced set of parts we purchased... supposedly this is an option

import messages
import time
import rak811v2
from datetime import datetime
import Adafruit_DHT
Rak811v2 = rak811v2.Rak811v2

## Device address
dev_addr = 0x02 ## Client

### Destination address
dest_addr = 0x01 ## Gateway

#### Setting configs
print('init')

lora = Rak811v2()

print('Reset radio')
lora.hard_reset()

print('Get version')
v = lora.version
print(v[0])


print('\nSet configuration modes for LoRa p2p')
lora.set_config('lora:work_mode:1')
resp = lora.get_info()
# print(resp)
for x in resp:
    print('\t',x)


print('\nSet self as sender mode')
lora.set_config('lorap2p:transfer_mode:2')
resp = lora.get_info()
# print(resp)
for x in resp:
    print('\t',x)


print('\nSet P2P parameters')
lora.set_config('lorap2p:915000000:10:0:1:8:16')
resp = lora.get_info()
for x in resp:
    print('\t',x)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
#### End of configs

### Messages to transmit

i=1
while True:
    print()
    print('loop iter %d' % i)
    print()
    
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    data_to_send = [round(humidity, 2), round(temperature, 2), datetime.now()]
    print('Sending "%s"' % data_to_send)

    message = messages.TXMessage(i, dest_addr, data_to_send)
    tx_bytes = message.get_bytes()

    # lora.send_lorap2p(str_to_send)
    lora.send_lorap2p(tx_bytes)
    print('Sent')

    time.sleep(30)
    i+=1
