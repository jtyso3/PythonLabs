print('What is your name?')
name = str(input())
print('How old are you?')
age = int(input())

  if name == 'Alice':
       print('Hi, Alice.')
   elif age < 12:
       print('You are not Alice, kiddo.')
❶ elif age > 100:
       print('You are not Alice, grannie.')
   elif age > 2000:
       print('Unlike you, Alice is not an undead, immortal vampire.')