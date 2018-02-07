a = [5]

def update():
	a[0] = a[0]+1

def main():
	print(a[0])
	update()
	print(a[0])

if __name__ == '__main__':
	main()