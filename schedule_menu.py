#!/usr/bin/env python2.7
# schedule_menu.py

import requests
import os
import sys

# Global Variables
NUM_ENTRIES=1
ENTRY_LIST = ['', '', '', '', '']
BOOK=''
SEASON_LIST = [1, 1, 1, 1, 1]
NICKNAME_LIST = ['','','','','']
EPISODE_LIST = [1, 1, 1, 1, 1]
WATCHED_LIST = [0, 0, 0, 0, 0]
MAX_LIST = [0, 0, 0, 0, 0]
MAX=0
RED='\033[0;31m'
DEFAULT_COLOR='\033[38;5;247m'
REQ_LIST = [{}, {}, {}, {}, {}]

# Usage Function
def usage(status=0):
   print '''Usage: {} [ -n NUM_ENTRIES -b BOOK ] ENTRY_ONE [ -s SEASON -x NICKNAME ] ENTRY_TWO [ -s SEASON -x NICKNAME ]...
   -n	NUM_ENTRIES	Number of TV shows/movies to sort (default: 1)
   -b	BOOK		Includes 1 book in schedule (FEATURE NOT IMPLEMENTED YET)
   -s	SEASON		Which season to call for a show (default: 1)
   -a	NICKNAME	Creates a alternative name for the show that can be displayed in lieu of the title
   -w	WATCHED		Marks number of episodes already watched and removes from list'''.format(os.path.basename(sys.argv[0]))
   sys.exit(status)

# Print Function
def print_episode(INDEX):
   print DEFAULT_COLOR+NICKNAME_LIST[INDEX]+'['+str(SEASON_LIST[INDEX])+'.'+str(EPISODE_LIST[INDEX])+']','-',

# Print in Color Function
def print_color(INDEX, COLOR):
   print COLOR+NICKNAME_LIST[INDEX]+'['+str(SEASON_LIST[INDEX])+'.'+str(EPISODE_LIST[INDEX])+']'+DEFAULT_COLOR,'-',

# Print Last Function
def print_last(INDEX):
   print DEFAULT_COLOR+NICKNAME_LIST[INDEX]+'['+str(SEASON_LIST[INDEX])+'.'+str(EPISODE_LIST[INDEX])+']'

# Print Last Line in Color Function
def print_last_color(INDEX, COLOR):
   print COLOR+NICKNAME_LIST[INDEX]+'['+str(SEASON_LIST[INDEX])+'.'+str(EPISODE_LIST[INDEX])+']'+DEFAULT_COLOR

# Returns 1 if show is not last in row
def show_to_right(CURRENT_EP, INDEX):
   if CURRENT_EP <= max([MAX_LIST[j] for j in xrange(INDEX+1, NUM_ENTRIES+1)]) and CURRENT_EP > min([WATCHED_LIST[k] for k in xrange(INDEX+1, NUM_ENTRIES)]):
      return 1
   else:
      return 0

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
for i in xrange(0, NUM_ENTRIES):
   if len(args) >= 1:
      arg = args.pop(0)
      ENTRY_LIST[i] = arg
      NICKNAME_LIST[i] = arg
      while len(args) and args[0].startswith('-') and len(args[0]) > 1:
         arg = args.pop(0)
         if arg == '-s':
            arg = args.pop(0)
            SEASON_LIST[i] = int(arg)
         elif arg == '-a':
            arg = args.pop(0)
            NICKNAME_LIST[i] = arg
	 elif arg == '-w':
	    arg = args.pop(0)
	    WATCHED_LIST[i] = int(arg)
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
MAX_LIST.append(0)

## Find largest amount of episodes in a season
MAX = max(MAX_LIST)

## Iterate through and print alternating episodes of each season
for x in xrange(1, MAX+1):
   for i in xrange(0, NUM_ENTRIES):
      if x < MAX_LIST[i] and x > WATCHED_LIST[i]:
         if show_to_right(x, i):
	    print_episode(i)
            EPISODE_LIST[i] = EPISODE_LIST[i] + 1
         else:
            print_last(i)
            EPISODE_LIST[i] = EPISODE_LIST[i] + 1
      elif x == MAX_LIST[i] and x > WATCHED_LIST[i]:
         if show_to_right(x,i):
            print_color(i, RED)
            EPISODE_LIST[i] = EPISODE_LIST[i] + 1
         else:
            print_last_color(i, RED)
            EPISODE_LIST[i] = EPISODE_LIST[i] + 1
      elif x <= WATCHED_LIST[i]:
         EPISODE_LIST[i] = EPISODE_LIST[i] + 1

