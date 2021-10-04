from rake_nltk import Rake
from underthesea import word_tokenize
# Do nltk không có stopwords tiếng Việt, nên bạn cần cần có danh sách stopwords này.
# https://github.com/ltkk/vietnamese-stopwords/blob/master/stopwords.txt
punctuations = ".,;:?!()'\""
stopwords = open('stopwords.txt').read().splitlines()
r = Rake(stopwords, punctuations)

sentence = 'Lập Trình Không Khó là một blog. cá nhân của Nguyễn Văn Hiếu'
def get_keywords(content):
    punctuations = ";:?!()'\""
    stopwords = open('stopwords.txt').read().splitlines()
    r = Rake(stopwords, punctuations,min_length=1, max_length=5)
    text = content.replace('\n','').replace('  ','')
    sentence = text
    sentence_word_tokenzine = word_tokenize(sentence)
    sentence_word_tokenzine_processed = [i.replace(' ','_') for i in sentence_word_tokenzine]
    sentence_processed = ' '.join(sentence_word_tokenzine_processed)
    r.extract_keywords_from_text(sentence_processed)
    c = r.get_ranked_phrases_with_scores()
    a = [i for i in c if len(i[1])<15]
    if len(a)>1:
        b = a[0][1] + ', '+ a[1][1]
        return str(b)
    else:
        return a[0][1]
a = get_keywords(sentence)

print(a)