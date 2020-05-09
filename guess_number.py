import random
r = random.randint(1, 100)
count = 0
while True:
	num = input('1~100猜數字: ')
	count += 1
	num = int(num)
	if num == r :
		print("bingo!")
		print('你猜第',count,'次才成功')
		break
	elif num > r :
		print('再小一點')
	else :
		print('再大一點')
	print('你已經猜第',count,'次了')