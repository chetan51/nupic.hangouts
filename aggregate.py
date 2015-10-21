#!/usr/bin/python
import csv
import sys

from nupic.data.file_record_stream import FileRecordStream
from nupic.data.aggregator import Aggregator



def aggregate(dataPath, outputPath):
  with FileRecordStream(dataPath) as reader:
    aggregator = Aggregator({'fields': [('messages', 'sum')],
                             'days': 1},
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
  aggregate(sys.argv[1], sys.argv[2])
