# Author : Jeeyoung kim (jeeyoungk@gmail.com)
# A program to calculate word count.

# This program can be executed by running:
# python dumbo/cmd.py start ex1_word_count.py -input book_dataset/pg10.txt -input book_dataset/pg1342.txt -output ex1_output
import re;

def normalize(word):
  return re.sub('[^a-z]', '', word.lower())

def mapper(key, value):
  # key - line number
  # value - line of text.
  for word in value.split():
    normalized = normalize(word)
    if normalized:
      yield (normalized, 1)

def reducer(key, values):
  yield (key, sum(values))

def bigram_mapper(key, values):
  prev_word = None
  for word in values.split():
    cur_word = normalize(word)
    if prev_word and cur_word:
      yield ((prev_word, cur_word), 1)
    prev_word = cur_word

if __name__ == "__main__":
  # Entry point to the program.
  import dumbo
  # dumbo.run(mapper, reducer)
  # run this to get bigram count, instead of word (unigram) count.
  # dumbo.run(bigram_mapper, reducer)
