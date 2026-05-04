speed = float(input())
limit = float(input())

if speed <= limit:
	print("未超速")
else:
	overspeed_ratio = (speed - limit) / limit * 100

	if overspeed_ratio <= 10:
		print("超速警告")
	elif overspeed_ratio <= 20:
		print("罚款100元")
	elif overspeed_ratio <= 50:
		print("罚款500元")
	elif overspeed_ratio <= 100:
		print("罚款1000元")
	else:
		print("罚款2000元")
