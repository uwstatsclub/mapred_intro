# Author : Jeeyoung kim (jeeyoungk@gmail.com)
# Program to filter the input data.

# This program can be executed by running:
# python dumbo/cmd.py ex2_filter.py -input example_student_dataset -output ex2_output

def mapper(key, value):
  # key - line number.
  # value - student id, student name, separated by tab.
  (student_id, student_name) = value.split('\t')
  if student_name.lower().startswith('j'):
    # Get only the users. 
    yield (student_id, student_name)

if __name__ == "__main__":
  # Entry point to the program.
  import dumbo
  dumbo.run(mapper)
