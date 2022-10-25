print('Rock paper scissors')
print()
import random
def play():
    user=input("What's your choice? 'r' for rock,'s' for scissors and 'p' for paper:")
    computer=random.choice(['r','s','p'])
    if user==computer:
        return "It's a tie"
    if is_win(user,computer):
        return "You won!"

    return'You lost!'

def is_win(player,opponent):
    #r>s,s>p,p>r
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p')\
       or (player=='p' and opponent=='r'):
       return True
print(play())