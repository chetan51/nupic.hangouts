#!/usr/bin/python
import json
import csv
import sys



def process(dataPath):
  maxNumEvents = 0
  maxConversation = None

  with open(dataPath, 'r') as f:
    data = json.load(f)

    for conversation in data['conversation_state']:
      conversation = conversation['conversation_state']
      events = conversation['event']

      if len(events) > maxNumEvents:
        maxNumEvents = len(events)
        maxConversation = conversation

    conversation = maxConversation
    events = conversation['event']
    print "Conversation"
    print maxConversation['conversation']['participant_data']
    print len(events)
    print "================="
    for event in events:
      print event['timestamp']



if __name__ == "__main__":
  process(sys.argv[1])
