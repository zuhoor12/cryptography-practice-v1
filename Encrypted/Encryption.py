def Encrypt(password):
    password = list(password)
    password.reverse()
    hash_of_password = ["Z"]
    for i in range(len(password)):
        text = password[i]
        
        hash_of_password.append(chr(ord(text)+4))
    hash_of_password.append(".¿")
    hash = "".join(hash_of_password)
    return hash
    
    
    
