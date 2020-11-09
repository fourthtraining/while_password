#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確 就印出"登入成功!"
#如果不正確 就印出 "密碼錯誤!還有_次機會"
#這是用<=寫的方式

password = 'a123456'
i = 3 #剩餘機會
while i <= 3:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		i = i - 1 #
		print('密碼錯誤! 還有', i,'次機會')
		if i == 0:
		 	print('您帳號已被鎖定')
		 	break