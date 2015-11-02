#!/usr/bin/python
import csv
from datetime import datetime
import json
import os
import sys
import time



def convert(dataPath, outputPath):
  with open(dataPath, 'r') as infile:
    reader = csv.reader(infile)

    for _ in xrange(3):
      reader.next()

    with open(outputPath, 'w') as outfile:
      for row in reader:
        timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.0')
        timestamp = int(time.mktime(timestamp.timetuple()))
        outfile.write(json.dumps([timestamp, int(row[1])]))
        outfile.write("\n")



if __name__ == "__main__":
  convert(sys.argv[1], sys.argv[2])
