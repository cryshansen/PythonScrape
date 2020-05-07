
import lxml.html

html = lxml.html.parse('http://www.techvibes.com/company-directory/edmonton/tag/it-consulting')

#html = lxml.html.parse("http://pypi.python.org/pypi") # can take an url, a filename or an object with a .read() method
packages = html.xpath('//article/section/header/a/text()') # get the text inside all "<tr><td><a ...>text</a></td></tr>"
print packages
