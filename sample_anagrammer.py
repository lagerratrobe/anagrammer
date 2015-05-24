#! /usr/local/bin/python

from bisect import bisect_left

def binary_search(word_list, word):   
    lo = 0
    hi = len(word_list)    
    pos = bisect_left(word_list, word, lo, hi)          
    return (True if pos != hi and word_list[pos] == word else False) 

word_dict = {}

with open('sample_dict.txt') as word_data:
  for word in word_data.readlines():
    word = word.strip()
    length = len(word)
    if length >= 4 and length not in word_dict:
      word_dict[length] = [word]
    elif length >= 4:
      word_dict[length].append(word)

print binary_search(word_dict[5], "resin")

#print binary_search(word_dict[8], "wrangler")
