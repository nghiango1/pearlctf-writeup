import time
import socket


class Netcat:
    """ Python 'netcat like' module """

    def __init__(self, ip, port):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """
        return self.socket.recv(length)

    def read_until(self, data):
        """ Read data into the buffer until we have data """
        while data not in self.buff:
            self.buff += self.socket.recv(1024).decode("ascii")

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def write(self, data):
        self.socket.send(data)

    def close(self):
        self.socket.close()


def crafted(f=None, position=None):
    result = '\'"'
    result += str(f) + '"\'\n'
    return result


whitelist = "_acdefhk"
unicode_range = 1114111
result = {}

# Check for black list
# for intValue in range(unicode_range):
#     s = Netcat('dyn.ctf.pearlctf.in', 30016)
#     data = bytes(crafted(chr(intValue)), 'utf-8')
#     s.write(data)
#     buf = s.read_until(">>>")
#     count = 0
#     while True:
#         count += 1
#         if count == 5:
#             break
#         time.sleep(1)
#         buf = s.read()
#         if len(buf) != 0:
#             break
#     print(intValue, buf[-45:])
#     if buf[-20:] not in result:
#         result[buf[-20:]] = []
#     result[buf[-20:]].append(intValue)
#     s.close()

black_list = """33
35
36
37
38
42
44
47
48
49
50
51
52
53
54
55
56
57
58
59
60
62
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
87
88
89
90
91
93
94
95
98
100
101
102
103
105
106
107
108
109
110
111
112
115
116
117
118
120
121
122
123
125
126
178
179
185
186
188
189
190
306
307
319
320
329
383
452
453
454
455
456
457
458
459
460
497
498
499"""
black_list = black_list.split('\n')
sample = ""
white_list = []

import string

for i in range(580):
    valid = chr(int(i))
    if str(i) not in black_list:
        white_list += valid
        if valid in string.printable:
            print(chr(int(i)), end='')
    else:
        sample += valid

print()
print(sample)
