urls = [
"http://www.baidu.com/a.txt",
 "http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
 "https://www.google.co.jp/a.txt",
 "http://www.google.com/b.txt",
 "https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg"
 ];

def count(urls):
    ls=[]
    for link in urls:
#    print(link)
        link2 = link.split('/')
    #print(link2[-1])
        ls.append(link2[-1])
        #print(ls)
    d = dict()
    for fl in ls:
        if fl not in d:
            d[fl] = 1
        else:
            d[fl] = d[fl]+1
    print(d)

# {  'a.txt': 3, 'b.txt': 2, 'c.jpg': 2}

print(count(urls));
