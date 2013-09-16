#!/usr/bin/python

# Gets stuff from Resident Advisor's awesome 'RA Recommends' section
# Note: this is just regexing the HTML... so may stop working if page structure changes
# This is not written by, or affiliated with Resident Advisor at all

# 2013 oldhill // MIT license

import urllib2
import re


def getResidentData():
  # grab all the data...
  web_page = urllib2.urlopen('http://www.residentadvisor.net/reviews.aspx?format=recommend')
  all_the_html = web_page.read()
  demarcator = 'pb2' # surrounds records of recommended stuff
  relevant_block = re.findall(demarcator+'(.*?)'+demarcator, all_the_html, re.DOTALL)[0]
  # zeroing in...
  relevant_string = re.findall('class=music>'+'(.*?)'+'</a', relevant_block, re.DOTALL)[0]
  return relevant_string


def recommendedArtist():
  relevant_set = getResidentData()
  artist = relevant_set.split('-')[0].strip()
  return artist

  
def recommendedWork():
  relevant_set = getResidentData()
  work = relevant_set.split('-')[1].strip()
  return work


# Use this to test; it should print artist and album/track name on command line
def main():
  
  test_artist = recommendedArtist()
  test_work = recommendedWork()

  print '\n>>>>>>>>>>>>>>>>>\n'
  print test_artist
  print test_work
  print '\n>>>>>>>>>>>>>>>>>\n'


if __name__ == '__main__':
    main()
