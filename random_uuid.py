import random

uuid_src = []
uuid_src.append(format(random.randint(0,0xffffffff), '08x'))
uuid_src.append(format(random.randint(0,0xffff), '04x'))
uuid_src.append(format(random.randint(0,0xffff), '04x'))
uuid_src.append(format(random.randint(0,0xffff), '04x'))
uuid_src.append(format(random.randint(0,0xffffffffffff), '012x'))
uuid = '-'.join(uuid_src)
print(uuid)