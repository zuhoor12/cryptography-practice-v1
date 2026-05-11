from colorama import Fore

def dic(hash):
    hash = list(hash)
    hack = []
    
    if hash[-1] == "¿" and hash[-2] == "." and hash[0] == "Z":
        hash.remove("Z")
        hash.pop()
        hash.pop()
        for j in range(len(hash)):
            index = hash[j]
            hack.append(chr(ord(index)-4))
        hack.reverse()
        outcome = "".join(hack)
        return outcome
    else:
        print(Fore.RED+"False!\nHash is not right")
        return 1
        
          