#!/bin/python3
feedbacknum = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '051910']
feedbackyn = ['YES', 'NO', 'MORE', 'HELP', 'RESET']
feedback = ''
yn = ''
enc = ''
name = ''

def loading():
    print(' ')
    print('Loading...')
    i = 0
    for i in range(4):
        print('Loading...')
        i ++ 1
    print(' ')
def off():
    print('Thank you')
    loading()
    print('Admin Mode OFF')
    quit()
def message():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newMessage = ''
  
    message = input('Please enter a message to be encrypted or de-crypted. Note: Using - in front of the key will de-crytpt: ')

    key = input('Now enter an encryption key: ')
    key = int(key)

    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character
        
    loading()
    print('Your new message is: ', newMessage)
def reset():
    print(' ')
    print('Reseting...')
    loading()
    message()
    off()
name = ''
print(' ')
name = input("What's your name? ")
print('Well hello', name ,'!')
print('Welcome to JudEncrypt!')
print(' ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
  
message = input('Please enter a message to be encrypted or de-crypted. Note: Using - in front of the key will de-crytpt: ')

key = input('Now enter an encryption key: ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character
        
loading()
print('Your new message is: ', newMessage)
print(' ')

print('Thank you for using JudEncrypt,', name ,'!')
print("This will not be saved in any way.")
feedbackbool = input('Before you leave, would you like to submit feedback(Yes/no)?: ').upper()
while feedbackbool not in feedbackyn:
    feedbackbool = input('Before you leave, would you like to submit feedback(Yes/no)?: ').upper()
if feedbackbool == 'YES':
    feedback = input('On a scale of one to ten, how would you rate your experience? ')
    while feedback not in feedbacknum:
            feedback = input('On a scale of one to ten, how would you rate your experience? ')
    loading()
    print('You anwsered', feedback)
    print('Thank you!')
else:
    print('Ok! Bye', name , '!')
if feedback == ('051910') and name == ('Jude') or feedback == ('PIPSKIN!') and name == ('jude'):
    loading()
    print('Admin Mode ON')
    yn = input('Would you like to play a game? Yes/no/more/help/reset: ').upper()
    while yn not in feedbackyn:
        yn = input('Would you like to play a game? Yes/no/more/help/reset: ').upper()
    if yn == ('YES'):
        loading()
        scramble()
        off()
    elif yn == ('MORE'):
        loading()
        enc = input('Would you like to encrypt something? yes/no ').upper()
        if enc == ('YES'):
           message
        else:
            print('You said', enc)
            off()
    elif yn == ('HELP'):
        print('Type "quit()" to exit help')
        help()
    elif  yn == ('RESET'):
        reset()
    else:
        off()