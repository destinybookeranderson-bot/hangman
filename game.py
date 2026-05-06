import random

# Word list
words = ["python", "hangman", "computer", "programming", "developer", "keyboard"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Create display
display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
import random

def play_hangman():
    words = ['python', 'circuit', 'adventure', 'keyboard', 'mountain', 'galaxy']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("--- Welcome to Hangman ---")
    
    while attempts > 0:
        # Show progress (e.g., p _ t h _ n)
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed: {', '.join(guessed_letters)}")

        if "_" not in display_word:
            print(f"🎉 Winner! You found the word: {word}")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please type one letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already tried '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Nope! '{guess}' isn't there.")

    if attempts == 0:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
import random

# Visual stages of the hangman (0 to 6 lives)
import random

# Social Media Theme: Trending Topics, Apps, and Internet Slang
WEIBO_THEMES = {
    "Apps": ["weibo", "wechat", "tiktok", "douyin", "xiaohongshu"],
    "Internet Slang": ["trending", "influencer", "hashtag", "viral", "algorithm"],
    "Entertainment": ["superstar", "premiere", "concert", "backstage", "fandom"]
}

def get_hangman_art(lives):
    stages = [
        "      \n      \n      \n      ", # 0 lives lost
        "      \n  O   \n      \n      ", # 1 life lost
        "      \n  O   \n  |   \n      ", # 2 lives lost
        "      \n  O   \n /|   \n      ", # 3 lives lost
        "      \n  O   \n /|\\  \n      ", # 4 lives lost
        "      \n  O   \n /|\\  \n /    ", # 5 lives lost
        "      \n  O   \n /|\\  \n / \\  "  # 6 lives lost (Game Over)
    ]
    return stages[lives]

def play_weibo_hangman():
    print("--- 📱 WEIBO EDITION HANGMAN 📱 ---")
    category = random.choice(list(WEIBO_THEMES.keys()))
    word = random.choice(WEIBO_THEMES[category]).lower()
    guessed_letters = []
    lives_lost = 0
    max_lives = 6

    while lives_lost < max_lives:
        print(f"\n{get_hangman_art(lives_lost)}")
        display = [char if char in guessed_letters else "_" for char in word]
        print(f"Category: {category} | Word: {' '.join(display)}")
        
        if "_" not in display:
            score = (max_lives - lives_lost) * 100
            print(f"🎉 SUCCESS! The word was {word.upper()}.")
            print(f"Your Score: {score} pts")
            print(f"📢 [Share to Weibo]: I just guessed '{word.upper()}' with {max_lives - lives_lost} lives left! Can you beat me? #WeiboHangman")
            return

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
            print("❌ Invalid or repeated guess.")
            continue

        guessed_letters.append(guess)
        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            lives_lost += 1
            print(f"❌ No '{guess}' here. {max_lives - lives_lost} lives left.")

    print(get_hangman_art(6))
    print(f"💀 GAME OVER! The word was: {word.upper()}")

if __name__ == "__main__":
    play_weibo_hangman()
import turtle

def draw_part(lives_left):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(2)
    
    if lives_left == 5: # Head
        t.penup(); t.goto(0, 70); t.pendown()
        t.circle(20)
    elif lives_left == 4: # Body
        t.penup(); t.goto(0, 70); t.setheading(270); t.pendown()
        t.forward(60)
    elif lives_left == 3: # Left Arm
        t.penup(); t.goto(0, 50); t.setheading(225); t.pendown()
        t.forward(30)
    elif lives_left == 2: # Right Arm
        t.penup(); t.goto(0, 50); t.setheading(315); t.pendown()
        t.forward(30)
    elif lives_left == 1: # Left Leg
        t.penup(); t.goto(0, 10); t.setheading(225); t.pendown()
        t.forward(30)
    elif lives_left == 0: # Right Leg
        t.penup(); t.goto(0, 10); t.setheading(315); t.pendown()
        t.forward(30)

def setup_gallows():
    screen = turtle.Screen()
    screen.title("Graphic Hangman")
    t = turtle.Turtle()
    t.speed(0); t.penup(); t.goto(-100, -100); t.pendown()
    t.forward(200); t.backward(100); t.left(90) # Base
    t.forward(200); t.right(90); t.forward(100) # Pole & Beam
    t.right(90); t.forward(30); t.hideturtle() # Rope

def play_graphic_hangman():
    setup_gallows()
    word = "TURTLE"
    guessed = []
    lives = 6

    while lives > 0:
        display = "".join([c if c in guessed else "_" for c in word])
        print(f"Word: {display}")
        
        if "_" not in display:
            print("Winner!")
            break
            
        guess = input("Letter: ").upper()
        if guess in word:
            guessed.append(guess)
        else:
            lives -= 1
            draw_part(lives)

    turtle.done()

if __name__ == "__main__":
    play_graphic_hangman()
