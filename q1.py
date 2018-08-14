urls = [
"http://www.baidu.com/a.txt",
 "http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
 "https://www.google.co.jp/a.txt",
 "http://www.google.com/b.txt",
 "https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg"

 ];

ls = []
for link in urls:
#    print(link)
    link2 = link.split('/')
    #print(link2[-1])
    ls.append(link2[-1])
print(ls)
d = dict()
for fl in ls:
    if fl not in d:
        d[fl] = 1
    else:
        d[fl] = d[fl]+1 
print(d)
#for fl in link2[-1]:
#    print(fl)
# link2[-1]
#    for element in link.split('/'):
        #print(element)
#        ls.append(element)
#print(ls)
 #print(count(urls));

# {  'a.txt': 3, 'b.txt': 2, 'c.jpg': 2}
