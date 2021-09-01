def create_user(splitmessage):
    try:
        with open('market.txt','r') as file:
            if splitmessage[1] in file.read():
                return 2
            else:
                raise ValueError
    except:
        try:
            print(splitmessage[1])
            try:
                f = open("market.txt","a")
            except:
                f = open("market.txt","w")
            f.write(splitmessage[1] + "\n")
        except:
            return 1
    
    
    return 0