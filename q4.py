# PTT最新 100 篇⽂文章中的標題、發⽂文時間、作者、內⽂文資訊

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.chun-wei.com')
#https://www.ptt.cc/bbs/NBA/index.html

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
print(counts)
