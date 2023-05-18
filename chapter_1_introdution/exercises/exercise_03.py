import os
os.system('cls')

original_sentence = 'Getting to be happy in life has no secret or mystery; just accept yourself as you are and learn to live with what you have, fighting for what you want to have.'

amount_word_appeared = 0
letter_appears_more_times = ''

sentence = original_sentence.replace(' ', '')

i = 0
while i < len(sentence):
    current_letter = sentence[i]
    current_amount_word_appeared = sentence.count(current_letter)

    if amount_word_appeared < current_amount_word_appeared:
        amount_word_appeared = current_amount_word_appeared
        letter_appears_more_times = current_letter
    i += 1

print(f'The letter that appeared the most times was "{letter_appears_more_times}" and the number of repetitions was {amount_word_appeared} times.')
