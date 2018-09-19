
platform = 0
direction = 0

while platform <= 10:
    if platform == 0:
        print("You can travel: (N)orth.")
        platform = platform + 1
    word = input("Direction: ")
    if word in "wW":
        direction = 100 #west
    elif word in "nN":
        direction = 200 #north
    elif word in "sS":
        direction = 300 #south
    elif word in "eE":
        direction = 400 #east

    if platform == 1:
        if direction == 200:  #north
            platform = platform + 1
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
            print("You can travel: (S)outh or (W)est.")
        if direction == 100:
            print("Not a valid direction!")               
    elif platform == 3:
        if direction == 300: #south
            platform = platform + 1  
            print("You can travel: (N)orth.")
        if direction == 100: #west
            platform = platform - 1  
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        if direction == 200 or direction == 400: 
            print("Not a valid direction!")
    elif platform == 4:
        if direction == 200:  #north
            platform = platform -1            
            print("You can travel: (S)outh or (W)est.")
        if direction == 100 or direction == 300 or direction == 400:
            print("Not a valid direction!")
    elif platform == 5: 
        if direction == 400: #east
            platform = platform + 1
            print("You can travel: (E)ast or (W)est.")
        if direction == 300: #south
            platform = platform - 3
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        if direction == 100 or direction == 200:
            print("Not a valid direction!")
    elif platform == 6:
        if direction == 100:  #west
            platform = platform - 1
            print("You can travel: (E)ast or (S)outh.")    
        if direction == 400: #east
            platform = platform + 1  
            print("You can travel: (S)outh or (W)est.")
        if direction == 100 or direction == 200 or direction == 300:
            print("Not a valid direction!")
    elif platform == 7:
        if direction == 300: #south
            platform = platform + 1   
            print("You can travel: (N)orth or (S)outh.")
        if direction == 100:  #west
            platform = platform - 1  
            print("You can travel: (E)ast or (W)est.")
        if direction == 200 or direction == 400:
            print("Not a valid direction!")

    elif platform == 8:
        if direction == 200:  #north
            platform = platform - 1    
            print("You can travel: (S)outh or (W)est.")
        if direction == 300: #south
            platform = platform + 1  
            print("Victory!")
            break
        if direction == 100 or direction == 400:
            print("Not a valid direction!")