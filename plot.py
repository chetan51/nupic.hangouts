#!/usr/bin/python
import argparse
from datetime import datetime
import json

from matplotlib import pyplot



def plot(dataPath, resultsPath):
  with open(dataPath, 'r') as dataFile:
    with open(resultsPath, 'r') as resultsFile:

      timestamps = []
      messages = []
      anomalyScores = []

      # TODO: refactor this
      timestampsScatter = []
      messagesScatter = []
      anomalyScoresScatter = []

      while True:
        dataRow = dataFile.readline()
        resultRow = resultsFile.readline()

        if not dataRow or not resultRow:
          break

        data = json.loads(dataRow)
        result = json.loads(resultRow)

        timestamps.append(datetime.fromtimestamp(data[0]))
        messages.append(data[1])
        anomalyScores.append(result[1])

        if result[1] > 0.5:
          timestampsScatter.append(datetime.fromtimestamp(data[0]))
          messagesScatter.append(data[1])
          anomalyScoresScatter.append(result[1])

      pyplot.subplot(2, 1, 1)
      pyplot.title("Messages")
      pyplot.plot(timestamps, messages)

      pyplot.subplot(2, 1, 1)
      pyplot.title("Messages")
      pyplot.xlim(min(timestamps), max(timestamps))
      sizes = [40 for t in timestampsScatter]
      pyplot.scatter(timestampsScatter, messagesScatter, s=sizes)

      pyplot.subplot(2, 1, 2)
      pyplot.title("Anomaly Score")
      pyplot.plot(timestamps, anomalyScores)

      pyplot.show()



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('data', metavar='/path/to/data.json', type=str)
  parser.add_argument('results', metavar='/path/to/results.json', type=str)

  args = parser.parse_args()

  plot(args.data, args.results)
