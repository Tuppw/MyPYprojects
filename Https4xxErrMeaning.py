r = 0
def error(x):
    match x:
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 402:
            return "Payment Required"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 405:
            return "Method Not Allowed"
        case 406:
            return "Not Acceptable"
        case 407:
            return "Proxy Authentication Required"
        case 408:
            return "Request Timeout"
        case 409:
            return "Conflict"
        case 410:
            return "Gone"
        case 411:
            return "Length Required"
        case 412:
            return "Precondition Failed"
        case 413:
            return "Payload Too Large"
        case 414:
            return "URI Too Long"
        case 415:
            return "Unsupported Media Type"
        case 416:
            return "Range Not Satisfiable"
        case 417:
            return "Expectation Failed"
        case 418:
            return "I\'m a teapot"
        case 421:
            return "Misdirected Request"
        case 422:
            return "Unprocessable Content"
        case 423:
            return "Locked"
        case 424:
            return "Failed Dependency"
        case 425:
            return "Too Early"
        case 426:
            return "Upgrade Required"
        case 428:
            return "Precondition Required"
        case 429:
            return "Too Many Requests"
        case 431:
            return "Request Header Fields Too Large"
        case 451:
            return "Unavailable For Legal Reasons"
    raise ValueError("Not a 4xx Value")

while r == 0:
    r = 1
    print(error(int(input("What is the 4xx error code? "))))
    r = 0
