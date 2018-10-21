password = 'a123456'
x = 3
while x > 0:
	pw = input('請輸入密碼')
	x = x - 1
	if pw == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if x > 0:
			print('你還有', x, '次機會')
		else:
			print('帳號已鎖定')