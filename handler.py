def handle_message(message, nickname="user"):
    '''handles message: 
    @message - text of recieved message
    @nickname - nickname of sender

    @returns - text of response
    '''

    answer = 'Hi, ' + nickname + '! '
    answer += 'Your message is ' + str(len(message)) + ' charachters long.'

    return answer


if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
