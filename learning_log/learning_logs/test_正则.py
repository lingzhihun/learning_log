import re
s = "ip='230.192.168.78', version = '1.0.0'"
res = re.search(r"ip='(?P<ip>\d+\.\d+\.\d+\.\d+)'", s)
print (res.group('ip'))  #通过命名分组来引用分组