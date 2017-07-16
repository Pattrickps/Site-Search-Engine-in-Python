#!C:\Python27\python.exe

# -*- coding: UTF-8 -*-
import cgitb,cgi
cgitb.enable()
print("content-type:text/html")
print


def get_page(url):
    try:
        if url == "http://localhost/medisol/index.php":
            return ''' MediSol
EMPLOYERS
SERVICES
ABOUT US
CONTACT US
Candidate
I'm a customer

Lorem ipsum dolor sit amet
Rerum cum similique recusandae itaque molestiae labore sed dolor fugit, saepe facere eaque, aperiam eaque

ORDER NOW

Employer
I'm a Donor

vitae at culpa, molestias libero distinctio maxime cupiditate nulla eos

DONATE NOW

Brand

Sed ut perspiciatis unde omnis iste natus
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum

I want to ORDER >>

Let's better DONATE >>

MediSol.

Raising health standards for better living.At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat

LOCATIONS

Delhi
Mumbai
Gujarat
Rajasthan
Pune
Bangalore
Kolkata
NEWSLETTER

Be in the show
<a href="http://localhost/medisol/employers.php">EMPLOYERS</a>
<a href="http://localhost/medisol/services.php">SERVICES</a>
<a href="http://localhost/medisol/aboutus.php">ABOUTUS</a>
<a href="http://localhost/medisol/contactus.php">CONTACTUS</a>


you@email.com
FOLLOW US


blog >>
? 2016 MindSol

All Rights Reserved
'''

        elif url == "http://localhost/medisol/employers.php":
            return '''MediSol
EMPLOYERS
SERVICES
ABOUT US
CONTACT US
Brand

at iusto alias perferendis sequi ipsam nulla non voluptatum
Explicabo omnis repellat quo fugiat earum dicta quibusdam, dolorem aspernatur officiis molestias officia, explicabo quo nobis eum blanditiis, optio amet voluptatem corporis distinctio id ducimus quae, repudiandae error ex qui veniam quidem nobis reiciendis ab sit pariatur? Eligendi odit cumque impedit sit, ut rem fugiat voluptatum officiis blanditiis cumque natus numquam quaerat, sed est voluptatibus harum quis fugit esse expedita eaque delectus hic?Illum corporis vel ipsa excepturi aliquid commodi ex adipisci voluptate tempora natus, necessitatibus ipsam ipsum repellat aliquid exercitationem ut sunt ex iste, perspiciatis ipsa hic porro cumque temporibus incidunt, repellat eum ipsa libero voluptate eos qui harum quidem totam asperiores, cupiditate earum et nisi illum id inventore beatae? Alias sapiente quo reprehenderit mollitia aperiam, ullam facere sunt dignissimos labore beatae temporibus perspiciatis, minima ad aut nam. Cum illum aliquid pariatur accusantium laborum exercitationem distinctio, fuga quos adipisci ipsum obcaecati maxime quae tenetur molestias asperiores repellat officiis, officia repudiandae fuga dignissimos cupiditate reiciendis nisi error, rerum temporibus repellendus, ducimus porro maiores nobis quos incidunt corrupti sint, atque tempora accusamus placeat ab dolor ipsa nesciunt ex libero officiis.

LOCATIONS

Delhi
Mumbai
Gujarat
Rajasthan
Pune
Bangalore
Kolkata
NEWSLETTER

Be in the show


you@email.com
FOLLOW US


blog >>
? 2016 MindSol

All Rights Reserved
'''

        elif url == "http://localhost/medisol/services.php":
            return '''MediSol
EMPLOYERS
SERVICES
ABOUT US
CONTACT US
Brand

Corrupti illum vel, mollitia soluta omnis commodi voluptatum, dolor
voluptatem perferendis asperiores perspiciatis libero, voluptate dolorem id iusto assumenda quasi neque porro. Totam quas iste fugit natus, omnis cumque incidunt temporibus facere quasi illo. Assumenda at facere similique molestiae sit, sunt sint sapiente natus quisquam quo blanditiis ex numquam molestiae, neque deleniti quos iste voluptates enim ut possimus at? Iste quo quisquam nobis distinctio quis perspiciatis quaerat hic atque dolorem natus, omnis libero hic praesentium soluta nisi ipsum ab mollitia esse, amet commodi pariatur similique ad enim repellat, exercitationem dignissimos numquam veniam saepe pariatur aliquid architecto eum, quod error animi quis excepturi, aspernatur necessitatibus ducimus incidunt?Alias eveniet quam sequi tempore maiores, exercitationem laboriosam iusto necessitatibus possimus nemo architecto incidunt at maxime dolor doloribus, nostrum expedita temporibus ea sunt optio harum odit, nostrum distinctio laboriosam magni nisi totam suscipit. Dicta ut libero odio ullam iure delectus tenetur a dolore sed, enim est quas aliquid consequuntur adipisci harum repellat cum, enim odit iusto veritatis sint, deserunt culpa obcaecati at alias quod vitae qui.

LOCATIONS

Delhi
Mumbai
Gujarat
Rajasthan
Pune
Bangalore
Kolkata
NEWSLETTER

Be in the show


you@email.com
FOLLOW US


blog >>
? 2016 MindSol

All Rights Reserved
'''

        elif url == "http://localhost/medisol/aboutus.php":
            return '''MediSol
EMPLOYERS
SERVICES
ABOUT US
CONTACT US
Brand

Corrupti illum vel, mollitia soluta omnis commodi voluptatum, dolor
voluptatem perferendis asperiores perspiciatis libero, voluptate dolorem id iusto assumenda quasi neque porro. Totam quas iste fugit natus, omnis cumque incidunt temporibus facere quasi illo. Assumenda at facere similique molestiae sit, sunt sint sapiente natus quisquam quo blanditiis ex numquam molestiae, neque deleniti quos iste voluptates enim ut possimus at? Iste quo quisquam nobis distinctio quis perspiciatis quaerat hic atque dolorem natus, omnis libero hic praesentium soluta nisi ipsum ab mollitia esse, amet commodi pariatur similique ad enim repellat, exercitationem dignissimos numquam veniam saepe pariatur aliquid architecto eum, quod error animi quis excepturi, aspernatur necessitatibus ducimus incidunt?Alias eveniet quam sequi tempore maiores, exercitationem laboriosam iusto necessitatibus possimus nemo architecto incidunt at maxime dolor doloribus, nostrum expedita temporibus ea sunt optio harum odit, nostrum distinctio laboriosam magni nisi totam suscipit. Dicta ut libero odio ullam iure delectus tenetur a dolore sed, enim est quas aliquid consequuntur adipisci harum repellat cum, enim odit iusto veritatis sint, deserunt culpa obcaecati at alias quod vitae qui.

LOCATIONS

Delhi
Mumbai
Gujarat
Rajasthan
Pune
Bangalore
Kolkata
NEWSLETTER

Be in the show


you@email.com
FOLLOW US


blog >>
? 2016 MindSol

All Rights Reserved
'''
        elif url == "http://localhost/medisol/contactus.php":
            return '''MediSol
MediSol
EMPLOYERS
SERVICES
ABOUT US
CONTACT US
Contact Us
Lorem ipsum dolor sit amet, quot labitur placerat usu ex.
Novum propriae dissentiunt pri ut...Facilis a in, minus beatae error deserunt totam corporis non repellendus, quidem nemo non tempora voluptatibus officiis modi quia. Assumenda quo voluptatum neque porro beatae voluptas optio facere veniam labore, ullam iure vero ab, perferendis saepe deleniti nostrum delectus similique aut sit totam eum voluptatem.

Contact Us
Lorem ipsum dolor sit amet, quot labitur placerat usu ex. Novum propriae dissentiunt pri ut Vel veritus consulatu ea.

All Fileds Required..


Name

Phone

Email

comment
Submit
LOCATIONS

Delhi
Mumbai
Gujarat
Rajasthan
Pune
Bangalore
Kolkata
NEWSLETTER

Be in the show


you@email.com
FOLLOW US


blog >>
? 2016 MindSol

All Rights Reserved
'''

    except:
        return ""
    return ""

def get_links(content):
    links=[]
    while True:
        start=content.find('<a href=') #<a href="www.xyz.com"
        if start==-1:
            break
        start_point=content.find('"',start)
        end_point=content.find('"',start_point+1)
        url=content[start_point+1:end_point]
        links.append(url)
        content=content[end_point:]

    return links


def crawler(seed):
    tocrawl=[seed]
    crawled=[]
    index=[] #[[word,[url1,url2......],[word2,[url2,url3......]]
    while tocrawl:
        page_url=tocrawl.pop()
        #task1
        content=get_page(page_url)
        add_page_to_index(index,page_url,content)

        #task2
        #collecting all the links
        list2=get_links(content)
        #updating the tocrawl list
        for element in list2:
            if element not in tocrawl:
                tocrawl.append(element)
        #updating the crawleed list
        crawled.append(page_url)




    return index



def add_page_to_index(index,page_url,content):
    words=content.replace(',',' ').replace('!',' ').replace('<p>',' ').replace('</p>',' ').replace('<h1>',' ').replace('</h1>',' ').replace('.',' ').replace('@',' ').split()
    for word in words:
        value=check_word(word,page_url,index)
        if value==1:
            index.append([word,[page_url]])


def check_word(word,page_url,index):
    for entry in index:
        if entry[0]==word:
            if not page_url in entry[1]:
                entry[1].append(page_url)
            return 0
    return 1



index=crawler('http://localhost/medisol/index.php')
#print index
#print len(index)

def lookup(index,keyword):
    for entry in index:
        if entry[0].lower() == keyword.lower():
            return entry[1]

    return None


form = cgi.FieldStorage()
try:
    if form.has_key("searchbox"):
        searchterm = form.getvalue("searchbox")
        searchterm=searchterm.strip()
        l1=searchterm.split()
        print('<br>')
        print searchterm
        print l1

        d1={}
        for j in l1:
            d1[j]=lookup(index,j)
        print('<br>')
        print d1

        d2={}
        for item in d1:
            for i in d1[item]:
                d2.setdefault(i, []).append(item)
        print('<br>')
        print d2.items()

        for k,v in d2.items():
            s=' '.join(v)
            if len(s)==len(searchterm):
                print "%s" %(searchterm),"@", ('<a href="{0}">{0}</a>'.format(k))
            print('<br>')



except NameError:
    print "There was an error understanding your search request.  Please press the back button and try again."
except:
    print "Query Not Found:"





















