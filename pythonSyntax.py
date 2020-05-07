#for num in range(10,20):  #to iterate between 10 to 20
 #  for i in range(2,num): #to iterate on the factors of the number
 #if num%i == 0:
 #j=num/i          #to calculate the second factor
 #print '%d equals %d * %d' % (num,i,j)
 #break #to move to the next number, the #first FOR
 #else: print num 'is a prime number'
 
count=0
while (count<5):
## page to scrape
   urlstring =base_url + str(count) +tag_name
    print urlstring
    count = count+1


# file system samples
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


from os import walk

f = []
for (dirpath, dirnames, filenames) in next(walk(mypath)):
    checksum_files.extend(os.path.join(dirpath,filename in filenames) break
    f.extend(filenames)
    break
