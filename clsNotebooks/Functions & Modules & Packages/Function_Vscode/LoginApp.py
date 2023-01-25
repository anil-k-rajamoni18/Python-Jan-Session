from MongoUtil import fetchOneRecord
def login(inp_username ,inp_password):
    import hashlib
    encrp_pass = hashlib.md5(inp_password.encode()).hexdigest()
    data = fetchOneRecord(inp_username)
    if data is not None:
        if(data["username"]==inp_username):
            if(data["passwd"]==encrp_pass):
                return "LOGIN SUCCESS"
            else:
                return "Invalid passwd"

    else:
        return " Sorry !Invalid Username"


res = login(input("Enter the username: "),input("Enter the passwd: "))
print(res)