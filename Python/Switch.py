http_status = 201

if http_status == 200 or http_status==201:
    print("Success")
elif http_status==400:
    print("Bad Request")
else :
    print("Unknown")
    
match http_status:
    case 200 | 201:
        print("Success!")
    case 400:
        print("Bad Request")
    case _:
        print("Unkown")