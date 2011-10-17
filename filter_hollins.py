# small script to filter hollins.dat, sample data for pagerank data set,
# obtained from http://www.limfinity.com/ir/

f = open('hollins.dat', 'r')
output = open('hollins.transformed', 'w')

line = f.readline()
num_pages, num_links = line.strip().split()
num_pages = int(num_pages)
num_links = int(num_links)

pageid_to_pages = {}
for i in range(num_pages):
  line = f.readline().strip()
  pageid, url = line.split()
  pageid = int(pageid)
  pageid_to_pages[pageid] = url

for i in range(num_links):
  line = f.readline().strip()
  sourceid, destid = line.split()
  sourceid = int(sourceid)
  destid = int(destid)
  output.write('%s\t%s\n' % (pageid_to_pages[sourceid], pageid_to_pages[destid]))
