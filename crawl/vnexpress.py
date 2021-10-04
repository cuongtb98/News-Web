import requests
from bs4 import BeautifulSoup
import re
import json
from underthesea import classify
from requests_html import HTMLSession
from newspaper import Article
from rake_nltk import Rake
import mysql.connector
from underthesea import word_tokenize

session = HTMLSession()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Snews"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE IF NOT EXISTS store_posts(ID INT AUTO_INCREMENT PRIMARY KEY, Image TEXT, Title TEXT, Link TEXT, Content TEXT, Keyword TEXT, Description TEXT, Summary TEXT, Category TEXT)")
 
def mining(Title, Link, Image, Content, Keyword, Description, Summary, Category):
    sql="SELECT title, link FROM SnewStore_productdev WHERE Title = %s and Link = %s"
    val=(Title, Link)
    try:   
        mycursor.execute(sql, val)
    except Exception as e:
        print(e)
    myresult=mycursor.fetchall()
    flag=len(myresult)
    if(flag<1):
        sql = "insert ignore into SnewStore_productdev(id, title, link, image, content, keyword, description, summary, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = ('null',Title, Link, Image, Content, Keyword, Description, Summary, Category)
        try:
            mycursor.execute(sql, val)
        except Exception as e:
            print(e)
        mydb.commit()
        print('=> Inserted scholarship with Title: ', Title)
    else:
        print("=> post have been inserted ")


def getURL_post_vnexpress(id_post):
    link = 'https://m.facebook.com/'+str(id_post)
    source = session.get(link)
    soup = BeautifulSoup(source.text, 'html.parser')
    content = soup.find(class_='touchable')
    link_post = 'https://vnexpress.net/'+content['href'].split('https%3A%2F%2Fvnexpress.net%2F')[1]
    link_request = requests.get(link_post)
    link_post_process = link_request.url
    return link_post_process

def get_title(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text)
    try:
        title = soup.find('h1', class_='title-detail')
        return title.text
    except:
        return ''

def get_content(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    try:
        content1 = soup.find('div', class_='sidebar-1').find('p', class_='description')
        content2 = soup.find('article', class_='fck_detail')

        content = content1.text + '\n\n\n' + content2.text
        content = re.sub('\n{2,}', '\n\n', content)
        return content
    except:
        return ''

def get_summary(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    summary = article.summary
    return str(summary)

def get_keywords(content):
    punctuations = ".,;:?!()'\""
    stopwords = open('stopwords.txt').read().splitlines()
    r = Rake(stopwords, punctuations,min_length=1, max_length=5)
    text = content.replace('\n','').replace('  ','')
    sentence = text
    sentence_word_tokenzine = word_tokenize(sentence)
    sentence_word_tokenzine_processed = [i.replace(' ','_') for i in sentence_word_tokenzine]
    sentence_processed = ' '.join(sentence_word_tokenzine_processed)
    r.extract_keywords_from_text(sentence_processed)
    c = r.get_ranked_phrases_with_scores()
    a = [i for i in c if len(i[1])<30]
    if len(a)>1:
        b = a[0][1] + ', '+ a[1][1]
        return str(b)
    else:
        return a[0][1]

def get_category(content):
    a = classify(content)
    return a

posts = 100
api_fb = 'https://graph.facebook.com/262700667105773?fields=feed.limit('+str(posts)+')&access_token=EAAAAZAw4FxQIBAOuh0MLHcQjodZChPVi69KSGWgpZCvV91tVHoShi3A4rx2JJYm7j1lOX5VXgZCwTZAPZCevua7arc00qi2P2IhrfBb6V7U3mJWD47b3rpnZC94XQFvZAYVgWJFHIlUpM7PXzakUvF1v4RlpIspksxlP5dgwz3D5EQZDZD'
source = requests.get(api_fb)
data = json.loads(source.text)


'''
Id
Image
Title
Link
Content
Keyword
Description
Summary
Category
'''

for num, itm in enumerate(data['feed']['data']):
    try:
        print('_________ '+str(num)+' __________')
        url = getURL_post_vnexpress(itm['id'])
        Image = 'https://s1.vnecdn.net/vnexpress/restruct/i/v388/v2_2019/pc/graphics/logo.svg'
        Title = get_title(url)
        Link = url
        Content = get_content(url)
        Keyword = get_keywords(Content)
        Description = itm['message']
        Summary = get_summary(url)
        processor_category = get_category(Content)
        if processor_category[0] == 'doi_song':
            Category = 1
        elif processor_category[0] == 'the_thao':
            Category = 2
        elif processor_category[0] == 'suc_khoe':
            Category = 3
        elif processor_category[0] == 'khoa_hoc':
            Category = 4
        elif processor_category[0] == 'du_lich':
            Category = 5
        else:
            Category = 0

        posts = {
        'Title': Title,
        'Link': Link,
        'Image': Image,
        'Content': Content,
        'Keyword': Keyword,
        'Description': Description,
        'Summary': Summary,
        'Category': str(Category)
        }
        mining(posts['Title'], posts['Link'], posts['Image'], posts['Content'], posts['Keyword'], posts['Description'], posts['Summary'], posts['Category'])
    except:
        pass


