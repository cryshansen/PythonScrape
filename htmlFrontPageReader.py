from lxml import html
import requests

#read more page
#pageUrl = 'http://www.techvibes.com'


#page = requests.get(page2str)
##tree = html.fromstring(page.content)
#section = tree.xpath('//section')

#tree.xpath('//section[@id="content-about"]/dl[@class="dl-horizontal"]/dd/a/text()')
# get the text inside all "<tr><td><a ...>text</a></td></tr>"


#edmonton technology companies directory with subcategorys called tag
fr_pageUrl = 'http://www.techvibes.com/company-directory/edmonton'
fr_page = requests.get(fr_pageUrl)
fr_tree = html.fromstring(fr_page.content)
fr_section = fr_tree.xpath('//section/div[@class="row"]/div[@class="span4"]/ul[@class="unstyled"]/li/a/@href')

f= open("SponsorCategories.txt","w")#open and write to file
for tag in fr_section:
    #print tag.split("/", 4)
    data= tag.split("/", 4)
    print data[4]
    f.write(data[4]+"\n")
    #find a way to strip off the /company-directory/edmonton/tag/ piece of the link.
    #then can loop through all pages for the subcategories names and websites.
f.close()
