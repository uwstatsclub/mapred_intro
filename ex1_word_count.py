# Author : Jeeyoung kim (jeeyoungk@gmail.com)
# A program to calculate word count.

# This program can be executed by running:
# python dumbo/cmd.py start ex1_word_count.py -input book_dataset/pg10.txt -input book_dataset/pg1342.txt -output ex1_output

def mapper(key, value):
  # key - line number
  # value - line of text.
  for word in value.split():
    yield (word, 1)

def reducer(key, values):
  yield (key, sum(values))

def bigram_mapper(key, values):
  prev_word = None
  for word in values.split():
    if prev_word is not None:
      yield ((prev_word, word), 1)
    prev_word = word

if __name__ == "__main__":
  # Entry point to the program.
  import dumbo
  # dumbo.run(mapper, reducer)
  # run this to get bigram count, instead of word (unigram) count.
  dumbo.run(bigram_mapper, reducer)
