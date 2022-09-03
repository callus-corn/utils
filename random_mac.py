import random

mac_src = []
for i in range(6):
    mac_byte = random.randint(0,0xff)
    if i==0:
        mac_byte = mac_byte & 0b1111_1110
    mac_src.append(format(mac_byte, '02x'))
mac = ':'.join(mac_src)
print(mac)
