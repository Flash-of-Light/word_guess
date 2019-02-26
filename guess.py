secret_word = "velociraptor"
guess = ""
guess_count = 0
guess_limit = 3
you_lose = False

while guess != secret_word and not(you_lose):
    if guess_count < guess_limit:
        guess = input("Enter your guess:")
        guess_count += 1
    else:
        you_lose = True

if you_lose:
    print("you lose gg")
else:
    print("You guessed the word!")