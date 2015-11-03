#!/usr/bin/python
import argparse
import json
from datetime import datetime, timedelta



def computeParams(dataPath):
  values = []

  with open(dataPath, 'r') as infile:
    for line in infile:
      row = json.loads(line)
      values.append(row[1])

  return {"min": min(values), "max": max(values)}



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('data', metavar='/path/to/data.json', type=str)

  args = parser.parse_args()

  print computeParams(args.data)
