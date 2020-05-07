from lxml import html
import requests


#from urllib2 import urlopen
#tutorial http://docs.python-guide.org/en/latest/scenarios/scrape/
base_url = 'http://www.techvibes.com/company-directory/edmonton/'
tag_name='/tag/it-consulting'
##-----TODO ---- write a loop that loops through each page on directory
## to capture all companies in listing
count=1
while (count<5):
## page to scrape
   urlstring =base_url + str(count) +tag_name
   print count
   page = requests.get(urlstring)
   tree = html.fromstring(page.content)
   #get data looking for
   header = tree.xpath('//header/h1[@class="linked-heading"]/a/text()')# name of company
   link2 = tree.xpath('//section/a[@class="read-more-link"]/@href')# individual page for website link
 #  f= open("ITConsultantsTest.txt","a")#open and write to file
   for line in header:
       print line
 #      f.write(line +"\n")
 #  f.close()
           
# listing each subcategory's individual website from captured link
   for link in link2:
         pageUrl = 'http://www.techvibes.com'
         page2str =    pageUrl+link
         #print page2str
         page2=requests.get(page2str)
         tree2 = html.fromstring(page2.content)
         websites=tree2.xpath('//section[@id="content-about"]/dl[@class="dl-horizontal"]/dd/a/text()')
         f=open("ITConsultantsWebsites.txt","a")
         for site in websites:
             print site
             f.write(site+"\n")
         f.close()
   count = count+1

