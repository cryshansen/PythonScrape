from lxml import html
import requests

# https://www.khanacademy.org/math/algebra2 relearn algebra?

base_url = "http://www.ca.dividendinvestor.com/index.php" #?"symbol=RTU_U
php_addOn = "?symbol="
symbol="XEI"
urlstring =base_url + php_addOn + symbol #+base_end
print urlstring
page = requests.get(urlstring) #, verify=False
#verif= false exposes to man in middle attacks
#requests.exceptions.SSLError: [Errno 1] 
tree = html.fromstring(page.content)
#get data looking for
stock_name = tree.xpath('//tr[@bgcolor="B0C1D9"]/td[@class]/text()')
stock_info = tree.xpath('//td[@class="hyper13"]/text()')
stock_vals = tree.xpath('//td[@class="hyper13"]/div/text()')

print stock_name #cleanse this value from \n types \t types and white space.
print stock_info
print stock_vals
f= open("StockDividendList.txt","w")#open and write to file
for info in stock_vals:
    #put a condition in looking for no alpha numeric values to skip over?
    #double check it matches up to the 'headers' created in stock info
    #clease the data from the \n values and the \t values in the array prior
    #to printing so it is all one line and white space.
    print(info)
    f.write(info +", ")
f.close()

#https://www.standardandpoors.com/en_US/web/guest
