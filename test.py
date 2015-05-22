#! /usr/local/bin/python

word_data = open('sample_dict.txt').readlines()
for line in word_data:
  line = line.strip()
  print line
