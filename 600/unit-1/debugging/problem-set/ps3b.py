from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_list, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    best_word = ""
    best_score = -1

    for word in word_list:
        if is_valid_word(word, hand, None, True):
            word_score = get_word_score(word, HAND_SIZE)

            if word_score > best_score:
                best_score = word_score
                best_word = word
                # print "word: ", word
                # print "score: ", best_score
    return best_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    total_score = 0
    keep_playing = True

    while keep_playing:
        display_hand(hand)
        word = comp_choose_word(hand, word_list)

        if word == "":
            keep_playing = False
            break;

        word_score = get_word_score(word, HAND_SIZE)
        print "word: ", word
        print "word's score: ", word_score
        total_score += word_score
        hand = update_hand(hand, word)

    print "total score: ", total_score

#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    keep_playing = True
    user_input = ""

    while keep_playing:
        user_play_game(word_list)

        user_input = raw_input("Choose: 'u' (play again), 'c' (computer plays)\n")

        if user_input == "u":
            continue;
        else:
            comp_play_hand(deal_hand(HAND_SIZE), word_list)
            keep_playing = False

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)


