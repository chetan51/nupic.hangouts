#!/usr/bin/python
import argparse
import json
import os

from nupic_hangouts.scripts.aggregate import aggregate
from nupic_hangouts.scripts.fill_zeros import fillZeros
from nupic_hangouts.scripts.convert_unicorn import convert
from nupic_hangouts.scripts.compute_params import computeParams
from nupic_hangouts.scripts.plot import plot



def model(dataPath, outputDir):
  if not os.path.exists(outputDir):
    os.makedirs(outputDir)

  base = os.path.basename(dataPath)
  base = os.path.splitext(base)[0]

  print "Converting data..."
  aggregatedPath = os.path.join(outputDir, base + ".csv")
  aggregate(dataPath, aggregatedPath, hours=1)

  filledPath = os.path.join(outputDir, base + "_filled.csv")
  fillZeros(aggregatedPath, filledPath, maxGap=3600)

  convertedPath = os.path.join(outputDir, base + "_filled.json")
  convert(filledPath, convertedPath)

  params = computeParams(convertedPath)

  print "Running model..."

  resultsPath = os.path.join(outputDir, base + "_results.json")
  if os.path.exists(resultsPath):
    os.remove(resultsPath)
  command = ("cat {0} | python -m unicorn_backend.model_runner"
             " --model hangouts"
             " --stats '{1}' > {2}").format(
               convertedPath, json.dumps(params), resultsPath)
  os.system(command)

  print "Plotting results..."

  plot(convertedPath, resultsPath)



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('data', metavar='/path/to/data.csv', type=str)
  parser.add_argument('output', metavar='/path/to/output', type=str)

  args = parser.parse_args()

  model(args.data, args.output)
