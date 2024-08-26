import numpy as np
import pandas as pd
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle


data=pd.read_csv("bollywod dataset.csv")
data.drop(columns='story',inplace=True)
data.drop(columns='tagline',inplace=True)
data.drop(columns='wiki_link',inplace=True)
data.drop(columns='release_date',inplace=True)
data.drop_duplicates(inplace=True)
data.drop_duplicates(subset=['imdb_id'])
data['actors']=data['actors'].str.replace(' ','').str.replace('|',' ').str.split().str.slice(0,5)


ps=PorterStemmer()
data['summary']=data['summary'].str.replace('Add a Plot\xa0»','')

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

data['summary']=data['summary'].apply(stem)
data.reset_index(drop=True,inplace=True)

data['genres']=data['genres'].str.replace('|',' ').astype(str)
data['title']=data['title'].astype(str)
data['actors']=data['actors'].str.join(' ').astype(str)
data['keyword']=data['summary']+' '+data['actors']+' '+data['genres']+' '+data['title']
data.drop(columns=['actors','summary'], inplace=True)
data['keyword']=data['keyword'].str.replace('.',' ')
data['keyword']=data['keyword'].str.replace('nan','')



cv=CountVectorizer(max_features=50000, stop_words=['is','to','my','the','a','and','so','then','of','he','she','as','in','if'])
vectors=cv.fit_transform(data['keyword']).toarray()

similarity=cosine_similarity(vectors)

a=[]
for i in data['title']:
    a.append(i)

pickle.dump('a',open('a.pkl','wb'))
df=data[['imdb_id','title','keyword','year_of_release']]
pickle.dump(similarity,open('sim.pkl','wb'))
pickle.dump(df,open('df.pkl','wb'))
x=a[0:4286]
pickle.dump(x,open('x.pkl','wb'))
print("done")