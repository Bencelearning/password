password = 'a123456'
x = 3
while x > 0:
	pw = input('請輸入密碼')
	if pw == password:
		print('登入成功')
		break
	else:
		x = x -1
		print('密碼錯誤, 你還有', x, '次機會')
