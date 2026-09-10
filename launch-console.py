name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) My favorite subjects")
    print("4) Exit")
    choice = input("Pick 1-3: ")
    if choice == "1":
        print("My name is Aditya Adapa. I am a currently a junior in the Liberal Arts and Science Academy High School. I live in Austin, Texas, and I love to code!")
    elif choice == "2":
        print("My goal is to apply my knowledge of computer science and technology to the field of environmental science.")
    elif choice == "3":
        print("My favorite subjects are generally math and physics, although recently I have been enjoying English a lot more recently!")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")