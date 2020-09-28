#!/usr/bin/env python3

import time
import json
import psutil
import datetime
import argparse


def erase():
    # erase files
    f = open('json_text.json', 'w')
    f.close()
    f = open('plain_text.txt', 'w')
    f.close()


class GetSystemInfo:
    def __init__(self, number):
        self.date = str(datetime.datetime.today().__format__("%Y-%m-%d-%H-%M-%S-%f"))
        self.cpu_idle = str(psutil.cpu_times()[3])
        self.vm_available = str(psutil.virtual_memory()[1])
        self.disk_free = str(psutil.disk_usage("/")[2])
        self.array = {
            "Snapshot": str(number),
            "Timestamp": self.date,
            "CPU": self.cpu_idle,
            "VM": self.vm_available,
            "Disk": self.disk_free
        }

    def savejson(self):
        with open("json_text.json", "a+") as file_json:
            file_json.write(json.dumps(self.array) + "\n")
        file_json.close()

    def savetxt(self):
        st = " | ".join(map(' : '.join, self.array.items()))
        with open("plain_text.txt", "a+") as file_plain:
            file_plain.write(st + "\n")

    def prt(self):
        print(self.array)


parser = argparse.ArgumentParser()
parser.add_argument('-i', help="Interval between snapshots", type=int, default=30)
parser.add_argument("-t", help="Output file type", default="txt")
args = parser.parse_args()


def main():
    erase()
    num = 0
    while True:
        num += 1
        obj = GetSystemInfo(num)
        # obj.prt()
        if args.t == "json":
            obj.savejson()
        else:
            obj.savetxt()
        time.sleep(args.i)
