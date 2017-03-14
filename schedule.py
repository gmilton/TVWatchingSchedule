#!/usr/bin/env python2.7

import requests
import os
import sys
import re

# Global Variables

NUM_ENTRIES=1
ENTRY_LIST = ['', '', '', '', '']
BOOK=''
SEASON_LIST = [1, 1, 1, 1, 1]
NICKNAME_LIST = ['','','','','']
EPISODE_LIST = [1, 1, 1, 1, 1]
MAX_LIST = [0, 0, 0, 0, 0]
MAX=0
RED='\033[0;31m'
REQ_LIST = [{}, {}, {}, {}, {}]
# Usage Function

def usage(status=0):
   print '''Usage: {} [ -n NUM_ENTRIES -b BOOK ] ENTRY_ONE [ -s SEASON -x NICKNAME ] ENTRY_TWO [ -s SEASON -x NICKNAME ]...
   -n	NUM_ENTRIES	Number of TV shows/movies to sort (default: 1)
   -b	BOOK		Includes 1 book in schedule
   -s	SEASON		Which season to call for a show (dafult: 1)
   -a	NICKNAME	Creates a alternative name for the show that can be displayed in lieu of the title'''.format(os.path.basename(sys.argv[0]))
   sys.exit(status)

# Print Function

def print_episode(NICKNAME, SEASON, EPISODE):
   print NICKNAME+'['+str(SEASON)+'.'+str(EPISODE)+']','-',

# Print in Color Function

def print_color(NICKNAME, SEASON, EPISODE, COLOR):
   print COLOR+NICKNAME+'['+str(SEASON)+'.'+str(EPISODE)+']'+'\033[38;5;247m','-',

# Print Last Function

def print_last(NICKNAME, SEASON, EPISODE):
   print NICKNAME+'['+str(SEASON)+'.'+str(EPISODE)+']'

# Print Last Line in Color Function

def print_last_color(NICKNAME, SEASON, EPISODE, COLOR):
   print COLOR+NICKNAME+'['+str(SEASON)+'.'+str(EPISODE)+']'+'\033[38;5;247m'

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
   ENTRY_LIST[0] = arg
   NICKNAME_LIST[0] = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_LIST[0] = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_LIST[0] = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_LIST[1] = arg
   NICKNAME_LIST[1] = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_LIST[1] = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_LIST[1] = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_LIST[2] = arg
   NICKNAME_LIST[2] = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_LIST[2] = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_LIST[2] = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_LIST[3] = arg
   NICKNAME_LIST[3] = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_LIST[3] = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_LIST[3] = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_LIST[4] = arg
   NICKNAME_LIST[4] = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_LIST[4] = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_LIST[4] = arg
      else:
         usage(1)

# Main Execution

## Request info about each show and set number of episodes for each show
url = 'http://www.omdbapi.com/?'
i = 0
while i < NUM_ENTRIES:
   REQ_LIST[i] = requests.get(url+'t='+ENTRY_LIST[i]+'&Season='+str(SEASON_LIST[i]))
   MAX_LIST[i] = max([int(x['Episode']) for x in REQ_LIST[i].json()['Episodes']])
   i = i + 1

## Find largest amount of episodes in a season
MAX = max(MAX_LIST)

## Iterate through and print alternating episodes of each season
for x in xrange(1, MAX+1):

   if x < MAX_LIST[0]:
      if x <= MAX_LIST[1] or x <= MAX_LIST[2] or x <= MAX_LIST[3] or x <= MAX_LIST[4]:
         print_episode(NICKNAME_LIST[0], SEASON_LIST[0], EPISODE_LIST[0])
         EPISODE_LIST[0] = EPISODE_LIST[0] + 1
      else:
         print_last(NICKNAME_LIST[0], SEASON_LIST[0], EPISODE_LIST[0])
         EPISODE_LIST[0] = EPISODE_LIST[0] + 1
   elif x == MAX_LIST[0]:
      if x <= MAX_LIST[1] or x <= MAX_LIST[2] or x <= MAX_LIST[3] or x <= MAX_LIST[4]:
         print_color(NICKNAME_LIST[0], SEASON_LIST[0], EPISODE_LIST[0], RED)
         EPISODE_LIST[0] = EPISODE_LIST[0] + 1
      else:
         print_last_color(NICKNAME_LIST[0], SEASON_LIST[0], EPISODE_LIST[0], RED)
         EPISODE_LIST[0] = EPISODE_LIST[0] + 1

   if NUM_ENTRIES >= 2:
      if x < MAX_LIST[1]:
         if x <= MAX_LIST[2] or x <= MAX_LIST[3] or x <= MAX_LIST[4]:
            print_episode(NICKNAME_LIST[1], SEASON_LIST[1], EPISODE_LIST[1])
            EPISODE_LIST[1] = EPISODE_LIST[1] + 1
         else:
            print_last(NICKNAME_LIST[1], SEASON_LIST[1], EPISODE_LIST[1])
            EPISODE_LIST[1] = EPISODE_LIST[1] + 1
      elif x == MAX_LIST[1]:
         if x <= MAX_LIST[2] or x <= MAX_LIST[3] or x <= MAX_LIST[4]:
            print_color(NICKNAME_LIST[1], SEASON_LIST[1], EPISODE_LIST[1], RED)
            EPISODE_LIST[1] = EPISODE_LIST[1] + 1
         else:
            print_last_color(NICKNAME_LIST[1], SEASON_LIST[1], EPISODE_LIST[1], RED)
            EPISODE_LIST[1] = EPISODE_LIST[1] + 1

   if NUM_ENTRIES >= 3:
      if x < MAX_LIST[2]:
         if x <= MAX_LIST[3] or x <= MAX_LIST[4]:
            print_episode(NICKNAME_LIST[2], SEASON_LIST[2], EPISODE_LIST[2])
            EPISODE_LIST[2] = EPISODE_LIST[2] + 1
         else:
            print_last(NICKNAME_LIST[2], SEASON_LIST[2], EPISODE_LIST[2])
            EPISODE_LIST[2] = EPISODE_LIST[2] + 1
      elif x == MAX_LIST[2]:
         if x <= MAX_LIST[3] or x <= MAX_LIST[4]:
            print_color(NICKNAME_LIST[2], SEASON_LIST[2], EPISODE_LIST[2], RED)
            EPISODE_LIST[2] = EPISODE_LIST[2] + 1
         else:
            print_last_color(NICKNAME_LIST[2], SEASON_LIST[2], EPISODE_LIST[2], RED)
            EPISODE_LIST[2] = EPISODE_LIST[2] + 1

   if NUM_ENTRIES >= 4:
      if x < MAX_LIST[3]:
         if x <= MAX_LIST[4]:
            print_episode(NICKNAME_LIST[3], SEASON_LIST[3], EPISODE_LIST[3])
            EPISODE_LIST[3] = EPISODE_LIST[3] + 1
         else:
            print_last(NICKNAME_LIST[3], SEASON_LIST[3], EPISODE_LIST[3])
            EPISODE_LIST[3] = EPISODE_LIST[3] + 1
      elif x == MAX_LIST[3]:
         if x <= MAX_LIST[4]:
            print_color(NICKNAME_LIST[3], SEASON_LIST[3], EPISODE_LIST[3], RED)
            EPISODE_LIST[3] = EPISODE_LIST[3] + 1
         else:
            print_last_color(NICKNAME_LIST[3], SEASON_LIST[3], EPISODE_LIST[3], RED)
            EPISODE_LIST[3] = EPISODE_LIST[3] + 1

   if NUM_ENTRIES >= 5:
      if x < MAX_LIST[4]:
         print_last(NICKNAME_LIST[4], SEASON_LIST[4], EPISODE_LIST[4])
         EPISODE_LIST[4] = EPISODE_LIST[4] + 1
      elif x == MAX_LIST[4]:
         print_last_color(NICKNAME_LIST[4], SEASON_LIST[4], EPISODE_LIST[4], RED)
         EPISODE_LIST[4] = EPISODE_LIST[4] + 1

