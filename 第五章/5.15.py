stu_list = [
	['201801', 'zhangyi'], ['201802', 'zhanger'], ['201803', 'zhangsan'], ['201804', 'zhangsi'],
	['201805', 'wangyi'], ['201806', 'wanger'], ['201807', 'wangsan'], ['201808', 'wangsi'],
	['201809', 'liyi'], ['201810', 'lier'], ['201811', 'lisan'], ['201812', 'lisi'],
	['201813', 'zhaoyi'], ['201814', 'zhaoer'], ['201815', 'zhaosan'], ['201816', 'zhaosi'],
	['201817', 'zhouyi'], ['201818', 'zhouer'], ['201819', 'zhousan'], ['201820', 'zhousi']
]

num = input().strip()

low = 0
high = len(stu_list) - 1
found = False

while low <= high:
	mid = (low + high) // 2
	if stu_list[mid][0] == num:
		print(stu_list[mid][0], stu_list[mid][1], sep = '')
		found = True
		break
	if stu_list[mid][0] < num:
		low = mid + 1
	else:
		high = mid - 1

if not found:
	print('None')
