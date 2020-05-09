import random
r = random.randint(1, 100)
while True:
	num = input('猜數字')
	num = int(num)
	if num == r :
		print("bingo!")
		break
	elif num > r :
		print('再小一點')
	else :
		print('再大一點')