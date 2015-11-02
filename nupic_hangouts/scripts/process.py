#!/usr/bin/python
import csv
from datetime import datetime
import json
import os
import sys



def process(dataPath, outputDir):
  maxNumEvents = 0
  maxConversation = None

  if not os.path.exists(outputDir):
    os.makedirs(outputDir)

  with open(dataPath, 'r') as infile:
    data = json.load(infile)

  for conversationState in data['conversation_state']:
    conversation = conversationState['conversation_state']
    conversationId = conversation['conversation_id']['id']
    events = conversation['event']

    events = [event for event in events if event['event_type'] == 'REGULAR_CHAT_MESSAGE']
    events = sorted(events, key=lambda event: event['timestamp'])

    textFileName = "{0}_{1}.txt".format(conversationId, len(events))
    csvFileName = "{0}_{1}.csv".format(conversationId, len(events))

    with open(os.path.join(outputDir, textFileName), 'w') as outfile:
      outfile.write(json.dumps(conversation['conversation']['participant_data']))

    with open(os.path.join(outputDir, csvFileName), 'w') as outfile:
      writer = csv.writer(outfile)

      writer.writerow(['timestamp', 'messages'])
      writer.writerow(['datetime', 'int'])
      writer.writerow(['T', ''])

      for event in events:
        timestampString = str(event['timestamp'])[:10]
        timestampRaw = datetime.fromtimestamp(int(timestampString))
        timestamp = timestampRaw.strftime('%Y-%m-%d %H:%M:%S.0')
        writer.writerow([timestamp, 1])



if __name__ == "__main__":
  process(sys.argv[1], sys.argv[2])
