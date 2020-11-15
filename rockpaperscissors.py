print("Credit for code and program: https://www.youtube.com/channel/UCYfSGNQSzCKp-QLL4pFKqvA")
print()

import random

while True:
    print('Game Starting..')

    choices = ['Rock', 'Paper', 'Scissors']  # bot choices
    bot = random.choice(choices)

    player = input('Rock, Paper or Scissors:')
    player = player.lower()
    player = player.strip()
    if (player == 'rock') or (player == 'paper') or (player == 'scissors'):
        """
            it is better to have a block filled with
         at least some code instead of leaving it as just 'pass'
        """
        print()
    else:
        bad_input = True
        while bad_input:
            player = input('Rock, Paper or Scissors:')  # you input
            player = player.lower()
            player = player.strip()
            if (player == 'rock') or (player == 'paper') or (player == 'scissors'):
                print()
                bad_input = False
                break
            else:
                continue



    """
        upper case your 
    choice just for the looks
    """
    player = player.title()
    print(f'You chose {player}')
    print(f'Opponent chose {bot}\n')


    bot_win = 'Opponent wins.\n\n\n\n'
    player_win = 'You win!\n\n\n\n'


    # Check for winner
    player = player.lower()
    bot = bot.lower()


    if bot == 'rock' and player == 'scissors':
        print(bot_win)
    elif bot == 'paper' and player == 'rock':
        print(bot_win)
    elif bot == 'scissors' and player == 'paper':
        print(bot_win)

    elif player == 'rock' and bot == 'scissors':
        print(player_win)
    elif player == 'paper' and bot == 'rock':
        print(player_win)
    elif player == 'scissors' and bot == 'paper':
        print(player_win)

    else:
        print('Tie!\n\n\n\n')

    continue
