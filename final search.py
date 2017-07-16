#!C:\Python27\python.exe

# -*- coding: UTF-8 -*-
from collections import OrderedDict
import cgitb,cgi
cgitb.enable()

print ("Content-type: text/html")
print

'''import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="engy1")
x = conn.cursor()'''

def get_page(url):
    try:
        if url == "http://localhost/businessstylus2/aboutUs.php":
            return ''' info@businessstylus.com.au
1-000-333-Enquery
About Us
<p>Lorem ipsum dolor sit amet, quot labitur placerat usu ex.<br>
Novum propriae dissentiunt pri ut
We are a  complete IT  solution provider company headquartered at Sydney , Australia and office in India.
<h2>About My Company
<p>We are supporting businesses of every size and location with our expert and experienced professionals  to let them covert their dream to realities . </p>
<p>Your business may be a startup or a fully settled mid or large enterprise , we have solution for all your IT related requirement . Ranging from acting as digital media agency for your business , we can also support over stunning website design to comprehensive website and Mobile App development over various platforms .
</p>
<p>We understand your needs and so have customized solutions to match All Segments of  Small, Medium And Large Business Enterprises.</p>
<h2>Why Us
<p>Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis. Vero vivendum pro id, ex rebum epicurei partiendo cum. Lorem ipsum dolor sit amet, quot labitur placerat usu ex. </p>
<p>Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis. Vero vivendum pro id, ex rebum epicurei partiendo cum. Lorem ipsum dolor sit amet, quot labitur placerat usu ex. </p>
<a href="http://localhost/businessstylus2/index.php">Home</a>
<a href="http://localhost/businessstylus2/services.php">What We Do</a>
<a href="http://localhost/businessstylus2/portfolio.php">Our Work</a>
<a href="http://localhost/businessstylus2/portfolio.php">Our Work</a>
<a href="http://localhost/businessstylus2/magento.php">Magento</a>
<a href="http://localhost/businessstylus2/blog.php">Blog</a>
<a href="http://localhost/businessstylus2/contactUs.php">Contact us</a>
<a href=""><strong>About Us</strong></a>
a href="http://localhost/businessstylus2/aboutUs.php"><span>About Us</span></a>
Ecommerce Solutions
<a href="what-we-do/open-cart.php">Open Cart</a>
<a href="what-we-do/woocommerce.php">woocommerce</a>
Digital Media Marketing
<a href="what-we-do/ppc-google-awards.php">PPC / Google Adwords</a>
<a href="what-we-do/seo.php">SEO</a>
<a href="http://localhost/businessstylus2/portfolio.php">Our Work</a>
<a href="http://localhost/businessstylus2/blog.php">Blog</a>
<a href="http://localhost/businessstylus2/contactUs.php">Contact us</a>
'''

        elif url == "http://localhost/businessstylus2/index.php":
            return '''Digital Media <br><span>Marketing</span>
<p class="white">We promote to empower your business to rank better and convert visitors into customers with customized digital plan for your brand...</p>
Magento <br>
<span>Expert</span>
We let your business talk your customers while your care the rest . Enjoy the expertise of our magento experts to care your store better
E-Commerce <br>
<span>Development</span>
<p class="white">Get  creative and Responsive website design for your website which is not only aesthetically pleasing  but also delivers  desired results for you
<p>Your business may be a startup or a fully settled mid or large enterprise , we have solution for all your IT related requirement . Ranging from acting as digital media agency for your business , we can also support over stunning website design to comprehensive website and Mobile App development over various platforms .
We understand your needs and so have customized solutions to match All Segments of  Small, Medium And Large Business Enterprises.</p>
We follow a complete process for our website development
Apps Development
We have a complete team for your mobile app solution. So you may either need
Digital Marketing
We promote to empower your business to rank better and convert visitors
Magento Expert
We let your business talk your customers while your care the rest
Ecommerce Solutions
Get your store online with our e-commerce expertise and experience with magneto
take a Glimpse of our work
We deliver globally result-driven IT Solutions and have helped business of All Segments from start-up to Small, Medium And Large Business Enterprises grab more customer too
Our Happy clients
Dont just faith us , see what our Happy customers say about us
ecommerce
Dont just faith us , see what our Happy solution customers say about us
Tony Blair, USA
CEO of ABC
'''

        elif url == "http://localhost/businessstylus2/services.php":
            return '''Services
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis. Vero vivendum pro id, ex rebum epicurei partiendo cum. Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis. Vero vivendum pro id, ex rebum epicurei partiendo cum.
Service
Web Development
Lorem ipsum dolor sit amet, solution quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.
Service
Apps Development
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.
Service
Digital Marketing
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.
Service
Website Design
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.
Service
Magetnto Expert
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.
Service
Ecommerce Solutions
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.'''

        elif url == "http://localhost/businessstylus2/magento.php":
            return '''Services
Web Development
Apps Development
Digital Marketing
Website Design
Magento Expert
Ecommerce Solution
Request a Call Back

Email

Phone

comment
Submit
Magento
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis. Vero vivendum pro id, ex rebum epicurei partiendo cum. Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis. Vero vivendum pro id, ex rebum epicurei partiendo cum.

Service
Ecommerce Website Design
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.


 Service
Magento Development
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.


 Service
Magento Enterprise Developers
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.


 Service
Magento Integration Experts
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.


 Service
Magetnto Expert
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.


 Service
Magento SEO and Conversion Optimisation
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea. At est dicam democritum. Iudico quodsi propriae vix ex. Eos an labitur indoctum periculis.

'''
        elif url == "http://localhost/businessstylus2/contactUs.php":
            return '''
Contact Us
Lorem ipsum dolor sit amet, quot labitur placerat usu ex.
Novum propriae dissentiunt pri ut...
Contact Us
Home Contact Us
Contact Us
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea.
All Fileds Required..
Contact Info
Head Office
Address : L2 / 107 Alex Site Road
Cows Abcd Australia 2065
Phone : +61 (2) 8484 0404 1300 139 658
E-mail : contact@mycompany.com.au
India Office
Address : L2 / 107 Alex Site Road
Cows Abcd Australia 2065
Phone : +61 (2) 8484 0404 1300 139 658
E-mail : contact@mycompany.com.au
'''

        elif url == "http://localhost/businessstylus2/portfolio.php":
            return '''Our Work
Some text will goes Here

Ecommerce
CMS
Mobile
Web

STUDIO EUROPE
A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart.

READ MORE
TOP PERFUME
A wonderful serenity has taken possession of my entire soul like these sweet mornings of spring which I enjoy with my whole heart.

READ MORE

A wonderful serenity has taken possession of my entire soul like these sweet mornings of spring which I enjoy with my whole heart.

READ MORE
STUDIO EUROPE
A wonderful serenity has taken possession of my entire soul like these sweet mornings of spring which I enjoy with my whole heart.

READ MORE

STUDIO EUROPE
A wonderful serenity has taken possession of my entire soul like these sweet mornings of spring which I enjoy with my whole heart.

READ MORE
TOP PERFUME
A wonderful serenity has taken possession of my entire soul like these sweet mornings of spring which I enjoy with my whole heart.

READ MORE

A wonderful serenity has taken possession of my entire soul like these sweet mornings of spring which I enjoy with my whole heart.

READ MORE

'''

    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.replace(';',' ').replace('!',' !').replace('<p>',' ').replace('</p>',' ').replace('<h1>',' ').replace('</h1>',' ').replace('<h2>',' ').replace('</h2>',' ').split()
    for word in words:
        add_to_index(index, word, url)


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if not url in entry[1]:
                entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None


index=crawl_web('http://localhost/businessstylus2/aboutUs.php')
#print index


form = cgi.FieldStorage()
try:
    if form.has_key("searchbox"): #if "searchbox in form:"
        searchterm = form.getvalue("searchbox")
        l1=searchterm.split()
        print l1
        print('<br>')
        result_url=[]
        for i in l1:
            result_url.append(lookup(index,i))

#        print result_url
        print('<br>')


        d1={}
        for j in l1:
            d1[j]=lookup(index,j)

        OrderedDict(d1.items())
        print d1.items()
        print('<br>')
        d2={}
        for item in d1:
            for i in d1[item]:
                d2.setdefault(i, []).append(item)

        print d2
        for k,v in d2.items():
            print "%s" %(' '.join(v)),"@", ('<a href="{0}">{0}</a>'.format(k))
            print('<br>')

    result=lookup(index,searchterm)

except NameError:
    print "There was an error understanding your search request.  Please press the back button and try again."
except:
    print "Query Not Found:"

