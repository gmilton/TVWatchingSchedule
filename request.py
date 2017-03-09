#!/usr/bin/env python2.7

import requests
import os
import sys
import re

# Global Variables

# Usage Function

# Parse command line options

# Main Execution

url = 'http://www.omdbapi.com/?'
r = requests.get(url)
dictionary = r.json()
