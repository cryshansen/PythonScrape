from lxml import html
import requests


#from urllib2 import urlopen
#tutorial http://docs.python-guide.org/en/latest/scenarios/scrape/



page = requests.get('http://www.bloomberg.com/quote/CVX:US')
tree = html.fromstring(page.content)
#this will create a list of buyers
stocks = tree.xpath('//div[@class="detailed-quote show"]/text()')
#this will create a list of stock values
prices = tree.xpath('//div[@data-view-uid="1|0_2_4"]/text()')
table = tree.xpath('//div[@class="data-table data-table_detailed"]/text()')
cellsClass = tree.xpath('//div[@class="cell cell__mobile-basic"]/text()')
cells = tree.xpath('//div[@class="cell "]/text()')
labels = tree.xpath('//div[@class="cell__label"]/text()')
values = tree.xpath('//div[@class ="cell__value cell__value_"]/text()')
downvalues = tree.xpath('//div[@class = "cell__value cell__value_down"]/text()')
print 'stocks:', stocks
print 'cellsClass:', cellsClass
print 'cells:', cells
print 'labels:', labels
print 'downvalues:', downvalues
print 'values:', values

f = open("test.txt","w") #open file with name test.txt

for i in range(len(labels)):
    if labels[i] == "\n                1 Yr Return\n            ":
        print labels[i].replace(" ","")
        print downvalues[1]

    elif labels[i] == "\n              YTD Return\n          ":
        print labels[i].replace(" ","")
        print downvalues[2]

 #   f.write(labels[i].replace(" ",""))
    
for i,j in zip(labels,values):
    if str(i) == "1 Yr Return":
        f.write("1 yr return:" + downvalues(i).replace(" ",""))
 #      f.write(str(i).replace(" ","")+","+ downvalues(i).replace(" ",""))
    elif str(i) == "YTD Return":
       f.write("ytd return:" + downvalues(i).replace(" ",""))
 #      f.write(str(i).replace(" ","")+","+downvalues(i).replace(" ",""))
    else:
       f.write(str(i).replace(" ","")+","+str(j).replace(" ",""))
f.close()



#Now we can do all sorts of cool stuff with it: we can analyze it using
#Python or we can save it to a file
#and share it with the world.

#Some more cool ideas to think about are modifying this script to iterate through the
#rest of the pages of this example dataset, or rewriting this application to use
#threads for improved speed.


#div class="data-table data-table_detailed"

