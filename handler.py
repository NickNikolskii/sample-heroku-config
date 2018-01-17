def handle_message(message, nickname="user"):
    '''handles message: 
    @message - text of recieved message
    @nickname - nickname of sender

    @returns - text of response
    '''

    if message == "SendMeSad":
        answer = "(╥﹏╥)"
    elif message == "SendMeHappy":
        answer = "(͡° ͜ʖ ͡°)"
    elif message == "SendMeMad":
        answer = "ᕙ( ︡'︡益'︠)ง"
    elif message == "SendMeLove":
        answer = "<3"
    elif message == "SendMeВедмідь":
        answer = "ʕ•ᴥ•ʔ"
    elif message == "SendMeIDontKnownWhat":
        answer = "¯\_(ツ)_/¯"
    elif message == "GiveMeDiretide":
        answer = "༼ つ ◕_◕ ༽つ"
    elif message == "Goodbye":
        answer = "Goodbye" + " " + nickname
    return answer


if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
