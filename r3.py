lines =[]
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ') # 清單分割,以空格(' ')來分
	time = s[0][:5] # 字串(可視同清單)分割,從0到4個字元位置,含開頭不含結尾)
	name = s[0][5:] # 字串(可視同清單)分割,從5到最後一個字元位置,含開頭不含結尾)
	print(name)