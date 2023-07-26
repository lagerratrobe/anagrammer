def getSignature(word):
  '''Converts a word into its "signature", ie lower case alpha sorted set of letters'''
  word = word.lower() # ELIMINATE CASE SO THAT "Lois" AND "soil" MATCH'''
  signature = ''.join(sorted(word))
  return signature