def reverse_string():
	user_string = str(input("Please enter a sentence you would like reversed: "))
	reverse_string = " ".join(user_string.split()[::-1])
	print (reverse_string)


if __name__ == "__main__":
	reverse_string()	
