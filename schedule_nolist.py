#!/usr/bin/env python2.7

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
ENTRY_LIST = []

SEASON_COUNT1=1
SEASON_COUNT2=1
SEASON_COUNT3=1
SEASON_COUNT4=1
SEASON_COUNT5=1
SEASON_LIST = []

NICKNAME_ONE=''
NICKNAME_TWO=''
NICKNAME_THREE=''
NICKNAME_FOUR=''
NICKNAME_FIVE=''
NICKNAME_LIST = []

EPISODE_COUNT1=1
EPISODE_COUNT2=1
EPISODE_COUNT3=1
EPISODE_COUNT4=1
EPISODE_COUNT5=1
EPISODE_LIST = []

EPISODE_MAX1=0
EPISODE_MAX2=0
EPISODE_MAX3=0
EPISODE_MAX4=0
EPISODE_MAX5=0
MAX_LIST = []

MAX=0

RED='\033[0;31m'

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
   ENTRY_ONE = arg
   NICKNAME_ONE = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_COUNT1 = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_ONE = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_TWO = arg
   NICKNAME_TWO = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_COUNT2 = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_TWO = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_THREE = arg
   NICKNAME_THREE = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_COUNT3 = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_THREE = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_FOUR = arg
   NICKNAME_FOUR = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_COUNT4 = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_FOUR = arg
      else:
         usage(1)
if len(args) >= 1:
   arg = args.pop(0)
   ENTRY_FIVE = arg
   NICKNAME_FIVE = arg
   while len(args) and args[0].startswith('-') and len(args[0]) > 1:
      arg = args.pop(0)
      if arg == '-s':
         arg = args.pop(0)
         SEASON_COUNT5 = int(arg)
      elif arg == '-a':
         arg = args.pop(0)
         NICKNAME_FIVE = arg
      else:
         usage(1)

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

   if NUM_ENTRIES == 1:
      print_last(NICKNAME_ONE, SEASON_COUNT1, EPISODE_COUNT1)
      EPISODE_COUNT1 = EPISODE_COUNT1 + 1 
   else:
      if x < EPISODE_MAX1:
         if x <= EPISODE_MAX2 or x <= EPISODE_MAX3 or x <= EPISODE_MAX4 or x <= EPISODE_MAX5:
            print_episode(NICKNAME_ONE, SEASON_COUNT1, EPISODE_COUNT1)
            EPISODE_COUNT1 = EPISODE_COUNT1 + 1
         else:
            print_last(NICKNAME_ONE, SEASON_COUNT1, EPISODE_COUNT1)
            EPISODE_COUNT1 = EPISODE_COUNT1 + 1
      elif x == EPISODE_MAX1: 
         if x <= EPISODE_MAX2 or x <= EPISODE_MAX3 or x <= EPISODE_MAX4 or x <= EPISODE_MAX5:
            print_color(NICKNAME_ONE, SEASON_COUNT1, EPISODE_COUNT1, RED)
            EPISODE_COUNT1 = EPISODE_COUNT1 + 1
         else:
            print_last_color(NICKNAME_ONE, SEASON_COUNT1, EPISODE_COUNT1, RED)
            EPISODE_COUNT1 = EPISODE_COUNT1 + 1

   if NUM_ENTRIES >= 2:
      if x < EPISODE_MAX2:
         if x <= EPISODE_MAX3 or x <= EPISODE_MAX4 or x <= EPISODE_MAX5:
            print_episode(NICKNAME_TWO, SEASON_COUNT2, EPISODE_COUNT2)
            EPISODE_COUNT2 = EPISODE_COUNT2 + 1
         else:
            print_last(NICKNAME_TWO, SEASON_COUNT2, EPISODE_COUNT2)
            EPISODE_COUNT2 = EPISODE_COUNT2 + 1
      elif x == EPISODE_MAX2:
         if x <= EPISODE_MAX3 or x <= EPISODE_MAX4 or x <= EPISODE_MAX5:
            print_color(NICKNAME_TWO, SEASON_COUNT2, EPISODE_COUNT2, RED)
            EPISODE_COUNT2 = EPISODE_COUNT2 + 1
         else:
            print_last_color(NICKNAME_TWO, SEASON_COUNT2, EPISODE_COUNT2, RED)
            EPISODE_COUNT2 = EPISODE_COUNT2 + 1

   if NUM_ENTRIES >= 3:
      if x < EPISODE_MAX3:
         if x <= EPISODE_MAX4 or x <= EPISODE_MAX5:
            print_episode(NICKNAME_THREE, SEASON_COUNT3, EPISODE_COUNT3)
            EPISODE_COUNT3 = EPISODE_COUNT3 + 1
         else:
            print_last(NICKNAME_THREE, SEASON_COUNT3, EPISODE_COUNT3)
            EPISODE_COUNT3 = EPISODE_COUNT3 + 1
      elif x == EPISODE_MAX3:
         if x <= EPISODE_MAX4 or x <= EPISODE_MAX5:
            print_color(NICKNAME_THREE, SEASON_COUNT3, EPISODE_COUNT3, RED)
            EPISODE_COUNT3 = EPISODE_COUNT3 + 1
         else:
            print_last_color(NICKNAME_THREE, SEASON_COUNT3, EPISODE_COUNT3, RED)
            EPISODE_COUNT3 = EPISODE_COUNT3 + 1

   if NUM_ENTRIES >= 4:
      if x < EPISODE_MAX4:
         if x <= EPISODE_MAX5:
            print_episode(NICKNAME_FOUR, SEASON_COUNT4, EPISODE_COUNT4)
            EPISODE_COUNT4 = EPISODE_COUNT4 + 1
         else:
            print_last(NICKNAME_FOUR, SEASON_COUNT4, EPISODE_COUNT4)
            EPISODE_COUNT4 = EPISODE_COUNT4 + 1
      elif x == EPISODE_MAX4:
         if x <= EPISODE_MAX5:
            print_color(NICKNAME_FOUR, SEASON_COUNT4, EPISODE_COUNT4, RED)
            EPISODE_COUNT4 = EPISODE_COUNT4 + 1
         else:
            print_last_color(NICKNAME_FOUR, SEASON_COUNT4, EPISODE_COUNT4, RED)
            EPISODE_COUNT4 = EPISODE_COUNT4 + 1

   if NUM_ENTRIES >= 5:
      if x < EPISODE_MAX5:
         print_last(NICKNAME_FIVE, SEASON_COUNT5, EPISODE_COUNT5)
         EPISODE_COUNT5 = EPISODE_COUNT5 + 1
      elif x == EPISODE_MAX5:
         print_last_color(NICKNAME_FIVE, SEASON_COUNT5, EPISODE_COUNT5, RED)
         EPISODE_COUNT5 = EPISODE_COUNT5 + 1

