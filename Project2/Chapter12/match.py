def fun(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "bad request"
        case _:     #default
            return "unknown status"
            

print (fun(77))