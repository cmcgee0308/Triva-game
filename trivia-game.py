print('Welcome to the Trivia Game!')
answer = input('Are you ready to start? Enter yes or no: ')
score = 0
total_questions = 3
 
if answer.lower()=='yes':
    answer=input('\nQuestion 1: What is the largest desert in the world? Enter (a, b or c) \na. Mojave \nb. Sahara \nc. Gobi \n')
    if answer.lower()=='b':
        score += 1
        print('\nCorrect!')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('\nQuestion 2: What is the largest human organ? Enter (a, b or c) \na. Intestines \nb. Skin \nc. Liver \n')
    if answer.lower()=='b':
        score += 1
        print('\nCorrect!')
    else:
        print('Wrong Answer :(')
 
    answer=input('\nQuestion 3: In Finding Nemo, what species of fish is Nemo? Enter (a, b or c) \na. Clownfish \nb. Pufferfish \nc. Goldfish \n')
    if answer.lower()=='a':
        score += 1
        print('\nCorrect!')
    else:
        print('Wrong Answer :(')
 
print('Game over! Your score is',score)
percent=(score/total_questions)*100
print('You got:',format (percent, ',.2f'), 'percent correct!')
print('GOODBYE!')