def main():
	time = input("Enter a time of day: ")
	print(time) 
	items = input("Enter a plural noun: ")
	print(items)
	name = input("Enter a name: ")
	name = name.capitalize()
	print(name)
	sentence = input("Enter a sentence: ")
	sentence = sentence.upper()
	print(sentence)
	verb = input("Enter a verb: ")
	print(f"The time is {time} and the {items} are being {verb} by {name} .")
#  items = dolls
#  name = stephen sedoll
#  example_dictionary = {"scream":"the future is made of dolls", "froze":"shake my head"}

# name = name.capitalize()
# x = scream.upper()

# print(x)

# print (name)

if __name__ == '__main__':
	main()
