data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # 餘數
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')



sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度為', sum_len/len(data), '個字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆長度小於100的留言')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
# lisr comprehension
# good = [d for d in data if 'good' in d]

bad = [('bad' in d) for d in data] 
# bad 裡會有一堆True跟False

# 文字計數程式
count_words = {}
for d in data:
	words = d.split() # split預設值是空白鍵
	for word in words:
		if word in count_words:
			count_words[word] += 1
		else:
			count_words[word] = 1
while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in count_words:	
		print(word, '出現過的次數為', count_words[word])
	else:
		print(這個字沒有出現過。)