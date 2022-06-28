#! /usr/bin/python3

# Left-justified version of anagram script

# Open the word file and read it in one swoop.
txt_file = 'dict.txt'
with open(txt_file) as word_file: 
    word_data = word_file.readlines()

# Process all the words into their root signatures and matches 
sig_dict = {}  # EMPTY DICTIONARY TO WRITE RESULTS INTO
for word in word_data:
  word = word.strip() # REMOVE TRAILING \n
  if len(word) >= 4: # WORD MUST BE AT LEAST 4 CHARS LONG
    word = word.lower() # ELIMINATE CASE SO THAT "Lois" AND "soil" MATCH'''
    signature = ''.join(sorted(word)) # signature of ['Lois', 'soil', 'oils'] all reduce to "ilos"
    # IF signature IS NEW, CREATE NEW DICTIONARY KEY WITH word AS VALUE INSIDE A LIST
    if signature not in sig_dict: 
      sig_dict[signature] = [word]
    # OTHERWISE JUST APPEND THE word AS NEW ENTRY IN VALUE LIST 
    else:
      sig_dict[signature].append(word)

# Evaluate the contents of sig_dict and only keep the entries that meet criteria: 
#  (number of matching words >= number of letters in signature)
for signature in sig_dict:
  word_length = len(signature) 
  list_length = len(sig_dict[signature])
  if list_length >= word_length:
    word_list = ','.join(sig_dict[signature])
    print(word_list)
    
    
