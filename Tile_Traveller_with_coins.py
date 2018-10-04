old_platform = 0
direction = 0

def collect_coins(total):

    collect_coins = input("Pull a lever (y/n): ")
    if collect_coins in "yY":  
        total += 1
        print('You received 1 coins, your total is now {}.'.format(total))
        return total            
    if collect_coins in "nN":  
        return total   
    return 0 


def game_rules(direction,summa):

    platform = old_platform
    if platform == 1:
        if direction == 200:  #north
            platform = platform + 1
            summa = collect_coins(summa)
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        if direction == 100 or direction == 300 or direction == 400:
            print("Not a valid direction!")
    elif platform == 2:
        if direction == 200:   #north
            platform = platform + 3
            print("You can travel: (E)ast or (S)outh.")
        if direction == 300:  #south
            platform = platform - 1   
            print("You can travel: (N)orth.")
        if direction == 400:  #east
            platform = platform + 1  
            summa = collect_coins(summa) 
            print("You can travel: (S)outh or (W)est.")
            a = True
        if direction == 100:
            print("Not a valid direction!")
            a = False               
    elif platform == 3:
        if direction == 300: #south
            platform = platform + 1  
            print("You can travel: (N)orth.")
            a = True
        if direction == 100: #west
            platform = platform - 1
            summa = collect_coins(summa)   
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            a = True
        if direction == 200 or direction == 400: 
            print("Not a valid direction!")
            a = False
    elif platform == 4:
        if direction == 200:  #north
            platform = platform -1
            summa = collect_coins(summa)             
            print("You can travel: (S)outh or (W)est.")
            a = True
        if direction == 100 or direction == 300 or direction == 400:
            print("Not a valid direction!")
            a = False
    elif platform == 5: 
        if direction == 400: #east
            platform = platform + 1
            summa = collect_coins(summa) 
            print("You can travel: (E)ast or (W)est.")
            a = True
        if direction == 300: #south
            platform = platform - 3
            summa = collect_coins(summa) 
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            a = True
        if direction == 100 or direction == 200:
            print("Not a valid direction!")
            a = False
    elif platform == 6:
        if direction == 100:  #west
            platform = platform - 1
            print("You can travel: (E)ast or (S)outh.")    
            a = True
        if direction == 400: #east
            platform = platform + 1  
            print("You can travel: (S)outh or (W)est.")
            a = True
        if direction == 100 or direction == 200 or direction == 300:
            print("Not a valid direction!")
            a = False
    elif platform == 7:
        if direction == 300: #south
            platform = platform + 1 
            summa = collect_coins(summa)   
            print("You can travel: (N)orth or (S)outh.")
            a = True
        if direction == 100:  #west
            platform = platform - 1 
            summa = collect_coins(summa)  
            print("You can travel: (E)ast or (W)est.")
            a = True
        if direction == 200 or direction == 400:
            print("Not a valid direction!")
            a = False
    elif platform == 8:
        if direction == 200:  #north
            platform = platform - 1  
            print("You can travel: (S)outh or (W)est.")
            a = True
        if direction == 300: #south
            platform = platform + 1  
            print("Victory!")
        if direction == 100 or direction == 400:
            print("Not a valid direction!")
    
#    if a == True:
#        sum_coins += collect_coins()
    
    return platform, summa

summa = 0
collect = 0
while old_platform <= 9:
    if old_platform == 9:
        break
    if old_platform == 0:
        print("You can travel: (N)orth.")
        old_platform = old_platform + 1
    word = input("Direction: ")
    if word in "wW":
        direction = 100 #west
    elif word in "nN":
        direction = 200 #north
    elif word in "sS":
        direction = 300 #south
    elif word in "eE":
        direction = 400 #eastn

    platform,summa = game_rules(direction,summa)
    old_platform = platform

#def game_rules(direction):