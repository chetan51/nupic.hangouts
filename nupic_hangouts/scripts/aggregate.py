#!/usr/bin/python
import argparse
import csv

from nupic.data.file_record_stream import FileRecordStream
from nupic.data.aggregator import Aggregator



def aggregate(dataPath, outputPath, days=0, hours=0):
  with FileRecordStream(dataPath) as reader:
    aggregator = Aggregator({'fields': [('messages', 'sum')],
                             'days': days,
                             'hours': hours},
                            reader.getFields())

    with open(outputPath, 'w') as outfile:
      writer = csv.writer(outfile)

      writer.writerow(['timestamp', 'messages'])
      writer.writerow(['datetime', 'int'])
      writer.writerow(['T', ''])

      while True:
        inRecord = reader.getNextRecord()
        bookmark = reader.getBookmark()

        (aggRecord, aggBookmark) = aggregator.next(inRecord, bookmark)

        # reached EOF?
        if inRecord is None and aggRecord is None:
          break

        if aggRecord is not None:
          timestamp = aggRecord[0].strftime('%Y-%m-%d %H:%M:%S.0')
          writer.writerow([timestamp, aggRecord[1]])



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('data', metavar='/path/to/data.csv', type=str)
  parser.add_argument('output', metavar='/path/to/output.csv', type=str)
  parser.add_argument('-D', '--days', type=int, default=0)
  parser.add_argument('-H', '--hours', type=int, default=0)

  args = parser.parse_args()

  aggregate(args.data, args.output, days=args.days, hours=args.hours)
