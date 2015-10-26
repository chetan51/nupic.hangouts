#!/usr/bin/python
import argparse
import csv
from datetime import datetime, timedelta



def fillZeros(dataPath, outputPath, maxGap=float('inf')):
  gap = timedelta(seconds=maxGap)
  timeFormat = '%Y-%m-%d %H:%M:%S.0'

  with open(dataPath, 'r') as infile:
    reader = csv.reader(infile)

    with open(outputPath, 'w') as outfile:
      writer = csv.writer(outfile)

      for _ in range(3):
        writer.writerow(reader.next())

      lastTimestamp = None

      for row in reader:
        timestamp = datetime.strptime(row[0], timeFormat)
        value = row[1]

        if lastTimestamp is None:
          lastTimestamp = timestamp

        while (timestamp - lastTimestamp) > gap:
          lastTimestamp += gap

          writer.writerow([lastTimestamp.strftime(timeFormat), 0])

        writer.writerow([timestamp.strftime(timeFormat), value])
        lastTimestamp = timestamp



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('data', metavar='/path/to/data.csv', type=str)
  parser.add_argument('output', metavar='/path/to/output.csv', type=str)
  parser.add_argument('-m', '--max_gap', type=int, default=float('inf'))

  args = parser.parse_args()

  fillZeros(args.data, args.output, maxGap=args.max_gap)
