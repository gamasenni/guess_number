import random
while True :
	start = input('請決定隨機數字開始值: ')
	start = int(start)
	end = input('請決定隨機數字結束值: ')	
	end = int(end)
	if end <= start :
		print('結束值不可<=開始值!! 請重新填寫。 ')
	else :
		break	



r = random.randint(start, end)
count = 0
while True:
	num = input('開始隨機猜數字: ')
	num = int(num)
	count += 1
	if num == r :
		print("bingo!")
		print('你猜第',count,'次才成功')
		break
	elif num > r :
		print('再小一點')
	else :
		print('再大一點')
	print('你已經猜第',count,'次了')