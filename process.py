#!/usr/bin/python
import csv
import datetime
import json
import os
import sys



def process(dataPath, outputDir):
  maxNumEvents = 0
  maxConversation = None

  with open(dataPath, 'r') as infile:
    data = json.load(infile)

  for conversationState in data['conversation_state']:
    conversation = conversationState['conversation_state']
    conversationId = conversation['conversation_id']['id']
    events = conversation['event']

    events = [event for event in events if event['event_type'] == 'REGULAR_CHAT_MESSAGE']

    textFileName = "{0}_{1}.txt".format(conversationId, len(events))
    csvFileName = "{0}_{1}.csv".format(conversationId, len(events))
    jsonFileName = "{0}_{1}.json".format(conversationId, len(events))

    with open(os.path.join(outputDir, textFileName), 'w') as outfile:
      outfile.write(json.dumps(conversation['conversation']['participant_data']))

    with open(os.path.join(outputDir, csvFileName), 'w') as outfile:
      writer = csv.writer(outfile)

      writer.writerow(['timestamp', 'messages'])
      writer.writerow(['datetime', 'int'])
      writer.writerow(['T', ''])

      for event in events:
        timestampString = str(event['timestamp'])[:10]
        timestampRaw = datetime.datetime.fromtimestamp(int(timestampString))
        timestamp = timestampRaw.strftime('%Y-%m-%d %H:%M:%S.0')
        writer.writerow([timestamp, 1])

    with open(os.path.join(outputDir, jsonFileName), 'w') as outfile:
      for event in events:
        timestampString = str(event['timestamp'])[:10]
        timestamp = int(timestampString)
        outfile.write(json.dumps([timestamp, 1]))
        outfile.write("\n")



if __name__ == "__main__":
  process(sys.argv[1], sys.argv[2])
