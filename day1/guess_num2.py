import random

real_num = random.randrange(10)

for i in range(3):
    guess_num = raw_input('please guess the real num:').strip()
    if len(guess_num) == 0:
        continue
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print 'You need input interger instead of string'
    if guess_num > real_num:
        print 'wrong! you need try smaller'
    elif guess_num < real_num:
        print 'wrong!you need try bigger!'
    else:
        print 'Congratulations! you got it!',real_num
        break
else:
    print 'The real num is', real_num