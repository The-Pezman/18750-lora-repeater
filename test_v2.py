###There's something wrong with the normal rak811 library for the recently produced set of parts we purchased... supposedly this is an option


from rak811v2 import Rak811v2

print('init')

lora = Rak811v2()
print(lora._serial)
print(lora._serial._serial)
print(lora._serial._serial.port)

lora.hard_reset()

resp = lora.get_info()
print(resp)
for x in resp:
    print('\t',x)