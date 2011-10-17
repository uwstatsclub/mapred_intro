# Author : Jeeyoung kim (jeeyoungk@gmail.com)
# Program to invert the given index.

# you can run this program by:
# dumbo start ex3_inverted_index.py -input hollins.transformed -output ex3_output

def mapper(key, value):
  # key - line number
  # value - source URL, dest URL.
  source_url, dest_url = value.strip().split('\t')
  yield (dest_url, source_url)

def reducer(key, values):
  # use this reducer to calculate indegrees, rather than list all.
  yield (key, sum(1 for value in values))

if __name__ == "__main__":
  # Entry point to the program.
  import dumbo
  dumbo.run(mapper)

  # run with reducer that calculates indegree instead,
  # by commenting the above line and uncommenting this.
  # dumbo.run(mapper, reducer)
