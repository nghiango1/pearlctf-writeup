import socket
import time
import math
import sys
import signal
import contexto.guess as ct


# ctrl+c handler:


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    print('Results:')
    print(finder.results)
    sys.exit(0)


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


def crafted(word="you"):
    return word + '\n'


def guess_order(value, max=1000):
    total_words = 1700
    if value < 1:
        value = 1
    return math.trunc(total_words/value)


signal.signal(signal.SIGINT, signal_handler)
black_list = []


while True:
    s = Netcat('dyn.ctf.pearlctf.in', 30021)
    buf = s.read()
    next_word = None
    finder = ct.Finder()
    for i in range(5):
        if next_word is not None:
            next_word = finder.guess_next()
            while next_word in black_list:
                next_word = finder.guess_next()
        else:
            next_word = "person"
        data = bytes(crafted(next_word), 'ascii')
        s.write(data)
        time.sleep(1)
        buf = s.read()
        try:
            order = guess_order(
                float(buf.decode("ascii").split(":")[1].split('\n')[0]))
        except Exception as _:
            print("blacklist this word", next_word)
            break
        finder.add_result(next_word, order)
        print(order, '\n', buf.decode("ascii"), next_word)
    s.close()
