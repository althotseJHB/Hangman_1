#TIP: use random.randint to get a random word from the list
import random

path = "/home/c4r4s3/problems/submission_001-hangman"

global chosen_letter


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    with open(file_name,'r') as some_words:

        some_words = open(file_name,'r')
        global words
        words = some_words.readlines()
        return words


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    global word_blank
    global word_blank1
    global random_word
    global chosen_word
    # global chosen_word1
    global chosen_letter
    length = len(words) - 1
    random_word = random.randint(0,length)
    chosen_word = words[random_word]
    index_letter = random.randint(0, len(chosen_word)-2)
    # hide_letter = ['_' for chosen_word in index_letter]
    chosen_letter = chosen_word[index_letter]
    word_blank = chosen_word[:index_letter] + "_" + chosen_word[index_letter+1:]
    guess_word = ("Guess the word: " + word_blank)
    # user_input = input("Guess the letter: " + word_blank)


    print(guess_word)
    # return word_blank1
    return chosen_word


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    global user_input
    global chosen_letter
    # global chosen_word1
    # print(chosen_word)
    user_input = input("Guess the missing letter: ")
    # if user_input in chosen_letter:
    #     print("correct")
    # else:
    #     print("Incorrect")

        # print(chosen_word1)

    return user_input


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')
