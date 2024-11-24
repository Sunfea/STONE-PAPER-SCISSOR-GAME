def Game():
    import random
    u = int(input('1 for stone, 2 for paper and 3 for scissor: '))
    c = random.randint(1, 3)
    if u>3:
        print("Invalid Input ❌")
        return Game()
    else:
        pass
        if c == 1:
            print('Computer: Stone')
        elif c == 2:
            print('Computer: Paper')
        else:
            print('Computer: Scissor')

        if u == 1:
            print('You: Stone')
        elif u == 2:
            print('You: Paper')
        else:
            print('You: Scissor')
        def Result():
            if(u==c):
                print('Ressult: Match Draw 🙏')
            elif(c==1 and u==3):
                print('Result: You Lose😑')
            elif(c==2 and u==1):
                print('Result: You Lose😑')
            elif(c==3 and u==2):
                print('Result: You Lose 😑')
            else:
                print('Result: You Won, yeahh✌️')
        Result()
        return Game()
Game()