spam = ['apples', 'bananas', 'tofu', 'cats']
def list_things(items):
	for i in range(len(items)-2):
		print(items[i], end = ', ')
	print(items[-2]+' and '+items[-1])
list_things(spam)