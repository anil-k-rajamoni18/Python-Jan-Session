def userData(username , passwd):
    d={}
    d["username"]=username
    d["passwd"]=genereteEn(passwd)
    return d

# userData("Kumar123","September")

def genereteEn(passwd):
    import hashlib
    
    return hashlib.md5(passwd.encode()).hexdigest()


# genereteEn("Hemanth")