#!/usr/bin/env python2.7
# schedule_nonickname.py

import requests
import os
import sys
import re

# Global Variables

NUM_ENTRIES=1
ENTRY_ONE='Stargate+SG-1'
ENTRY_TWO=''
ENTRY_THREE=''
ENTRY_FOUR=''
ENTRY_FIVE=''
BOOK=''

SEASON_COUNT1=1
SEASON_COUNT2=1
SEASON_COUNT3=1
SEASON_COUNT4=1
SEASON_COUNT5=1

EPISODE_COUNT1=1
EPISODE_COUNT2=1
EPISODE_COUNT3=1
EPISODE_COUNT4=1
EPISODE_COUNT5=1

EPISODE_MAX1=0
EPISODE_MAX2=0
EPISODE_MAX3=0
EPISODE_MAX4=0
EPISODE_MAX5=0

MAX=0

# Usage Function

def usage(status=0):
   print '''Usage: {} [ -n NUM_ENTRIES -b BOOK ] ENTRY_ONE SEASON_COUNT1 ENTRY_TWO SEASON_COUNT2...
   -n	NUM_ENTRIES	Number of TV shows/movies to sort (default: 1)
   -b	BOOK		Includes 1 book in schedule'''.format(os.path.basename(sys.argv[0]))
   sys.exit(status)

# Parse command line options

args = sys.argv[1:]
while len(args) and args[0].startswith('-') and len(args[0]) > 1:
   arg = args.pop(0)
   if arg == '-n':
      arg = args.pop(0)
      NUM_ENTRIES = int(arg)
   elif arg == '-b':
      arg = args.pop(0)
      BOOK = arg
   elif arg == '-h':
      usage(0)
   else:
      usage(1)

if len(args) < 1:
   usage(1)

## Set entries for TV shows/movies to include

if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_ONE = arg
   arg = args.pop(0)
   SEASON_COUNT1 = int(arg)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_TWO = arg
   arg = args.pop(0)
   SEASON_COUNT2 = int(arg)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_THREE = arg
   arg = args.pop(0)
   SEASON_COUNT3 = int(arg)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_FOUR = arg
   arg = args.pop(0)
   SEASON_COUNT4 = int(arg)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_FIVE = arg
   arg = args.pop(0)
   SEASON_COUNT5 = int(arg)

# Main Execution

## Request info about each show
url = 'http://www.omdbapi.com/?'
req_one = requests.get(url+'t='+ENTRY_ONE+'&Season='+str(SEASON_COUNT1))
if NUM_ENTRIES >= 2:
   req_two = requests.get(url+'t='+ENTRY_TWO+'&Season='+str(SEASON_COUNT2))
if NUM_ENTRIES >= 3:
   req_three = requests.get(url+'t='+ENTRY_THREE+'&Season='+str(SEASON_COUNT3))
if NUM_ENTRIES >= 4:
   req_four = requests.get(url+'t='+ENTRY_FOUR+'&Season='+str(SEASON_COUNT4))
if NUM_ENTRIES >= 5:
   req_five = requests.get(url+'t='+ENTRY_FIVE+'&Season='+str(SEASON_COUNT5))

## Set number of episodes for each show
EPISODE_MAX1 = max([int(x['Episode']) for x in req_one.json()['Episodes']])
if NUM_ENTRIES >= 2:
   EPISODE_MAX2 = max([int(x['Episode']) for x in req_two.json()['Episodes']])
if NUM_ENTRIES >= 3:
   EPISODE_MAX3 = max([int(x['Episode']) for x in req_three.json()['Episodes']])
if NUM_ENTRIES >= 4:
   EPISODE_MAX4 = max([int(x['Episode']) for x in req_four.json()['Episodes']])
if NUM_ENTRIES >= 5:
   EPISODE_MAX5 = max([int(x['Episode']) for x in req_five.json()['Episodes']])

## Find largest amount of episodes in a season
MAX = max(EPISODE_MAX1, EPISODE_MAX2, EPISODE_MAX3, EPISODE_MAX4, EPISODE_MAX5)

## Iterate through and print alternating episodes of each season
for x in xrange(1, MAX+1):
   if x <= EPISODE_MAX1 and NUM_ENTRIES > 1 and (x <= EPISODE_MAX2 or x <= EPISODE_MAX3 or x <= EPISODE_MAX4 or x <= EPISODE_MAX5):
      print req_one.json()['Title']+'['+str(SEASON_COUNT1)+'.'+str(EPISODE_COUNT1)+']','-',
      EPISODE_COUNT1 = EPISODE_COUNT1 + 1
   elif x == EPISODE_MAX1 or NUM_ENTRIES == 1:
      print req_one.json()['Title']+'['+str(SEASON_COUNT1)+'.'+str(EPISODE_COUNT1)+']'
      EPISODE_COUNT1 = EPISODE_COUNT1 + 1

   if NUM_ENTRIES >= 2 and x <= EPISODE_MAX2 and (x <= EPISODE_MAX3 or x <= EPISODE_MAX4 or x <= EPISODE_MAX5):
      print req_two.json()['Title']+'['+str(SEASON_COUNT2)+'.'+str(EPISODE_COUNT2)+']','-',
      EPISODE_COUNT2 = EPISODE_COUNT2 + 1
   elif NUM_ENTRIES >= 2 and x <= EPISODE_MAX2:
      print req_two.json()['Title']+'['+str(SEASON_COUNT2)+'.'+str(EPISODE_COUNT2)+']'
      EPISODE_COUNT2 = EPISODE_COUNT2 + 1

   if NUM_ENTRIES >= 3 and x <= EPISODE_MAX3 and (x <= EPISODE_MAX4 or x <= EPISODE_MAX5):
      print req_three.json()['Title']+'['+str(SEASON_COUNT3)+'.'+str(EPISODE_COUNT3)+']','-',
      EPISODE_COUNT3 = EPISODE_COUNT3 + 1
   elif NUM_ENTRIES >= 3 and x <= EPISODE_MAX3:
      print req_three.json()['Title']+'['+str(SEASON_COUNT3)+'.'+str(EPISODE_COUNT3)+']'
      EPISODE_COUNT3 = EPISODE_COUNT3 + 1

   if NUM_ENTRIES >= 4 and x <= EPISODE_MAX4 and x <= EPISODE_MAX5:
      print req_four.json()['Title']+'['+str(SEASON_COUNT4)+'.'+str(EPISODE_COUNT4)+']','-',
      EPISODE_COUNT4 = EPISODE_COUNT4 + 1
   elif NUM_ENTRIES >= 4 and x <= EPISODE_MAX4:
      print req_four.json()['Title']+'['+str(SEASON_COUNT4)+'.'+str(EPISODE_COUNT4)+']'
      EPISODE_COUNT4 = EPISODE_COUNT4 + 1

   if NUM_ENTRIES >= 5 and x <= EPISODE_MAX5:
      print req_five.json()['Title']+'['+str(SEASON_COUNT5)+'.'+str(EPISODE_COUNT5)+']'
      EPISODE_COUNT5 = EPISODE_COUNT5 + 1
