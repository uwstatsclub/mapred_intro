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

if __name__ == "__main__":
  # Entry point to the program.
  import dumbo
  dumbo.run(mapper, reducer)
