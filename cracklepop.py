# cracklepop python function
# divisible by 3: print crackle
# divisible by 5: print pop
# divisible by both: print cracklepop
for x in range(1, 100):
    print(x)
    if (x % 3 == 0 and x % 5 == 0):
        print("cracklepop")
    elif(x % 3 == 0):
        print("crackle")
    elif(x % 5 == 0):
        print("pop")

# to dos: make the  number be on its own line with its annotation if applicable
