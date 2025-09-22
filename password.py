password = "khaled"
n = 3

for i in range(3):
    guess = input("guess the password: ")
    if guess == password:
        print("you have guessed correctly!!")
        break

    else:
        n = n - 1
        print("wrong guess you have",n,"attemps remainig")
        continue

    print("you have failed to guess the password")
