import hangman_art
import hangman_word
import random

dict_keys = []
for x in hangman_word.word_dict.keys():
    dict_keys.append(x)

life = 7
score = 0
end_of_game = False
display_word_len = []
chosen_category = ""
chosen_word = ""
one_word_display = ""
restart = ""

def play():
    global life, end_of_game, score, display_word_len, chosen_category, chosen_word, one_word_display, restart

    print(hangman_art.logo)
    game_mode = input(f"Please choose difficulty level.Easy/Medium/Hard : ").lower()

    # Choose word according to difficulty level
    def choose_word():
        global display_word_len
        global chosen_category
        global chosen_word
        global one_word_display
        if game_mode == "easy" or game_mode == "medium":
            chosen_category = random.choice(dict_keys)
            chosen_word = (random.choice(hangman_word.word_dict[chosen_category])).lower()
            display_word_len = []
            # print(chosen_word)
            for _ in range(0, len(chosen_word)):
                display_word_len.append("_")
            if game_mode == "easy":
                one_word_display = random.randint(0, len(chosen_word)-1)
                display_word_len[one_word_display] = chosen_word[one_word_display]
        else:
            chosen_word = (random.choice(hangman_word.word_list)).lower()
            display_word_len = []
            # print(chosen_word)
            for _ in range(0, len(chosen_word)):
                display_word_len.append("_")

    choose_word()
    while not end_of_game:
        print(f"{' '.join(display_word_len)}")
        # clearing hint depending on difficulty level
        if game_mode == "hard":
            guessed_word = input(f"Guess a word: ").lower()
        else:
            guessed_word = input(f"Guess a word from {chosen_category} category: ").lower()

        # Checking guessed word in chosen word
        for position in range(len(chosen_word)):
            if guessed_word == chosen_word[position]:
                display_word_len[position] = guessed_word
        # If choose wrong word then reduce life
        if guessed_word not in chosen_word:
            print(f"You've chosen wrong word. You lost a life.")
            print(hangman_art.stages[life-1])
            life -= 1
            if life == 0:
                print(f"You've lost the game. The word was '{chosen_word}'. Your final Score is: {score}")
                restart = input(f"Do you want to restart game? Type yes/no. ").lower()
                end_of_game = True

        # Guessing new word if user score one
        if "_" not in display_word_len:
            score += 1
            if score == 1:

                print(f"You successfully guess one word ({chosen_word}).your Score is: {score}")
            else:
                print(f"You successfully guess another word ({chosen_word}).your Score is: {score}")
            choose_word()


play()
while restart == "yes":
    life = 7
    score = 0
    end_of_game = False
    display_word_len = []
    chosen_category = ""
    chosen_word = ""
    one_word_display = ""
    play()
