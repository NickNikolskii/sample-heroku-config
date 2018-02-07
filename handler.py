from random import choice
Smiles = [["(╥﹏╥)", 0], ["(͡° ͜ʖ ͡°)", 0], ["( ︡'︡益'︠)ง", 0], ["<3", 0], ["ʕ•ᴥ•ʔ", 0], ["¯\_(ツ)_/¯", 0], ["(つ ◕_◕ )つ", 0]]
MostPopular = Smiles[0][0]
maxx = 0
def handle_message(message, nickname="user"):
    global Smiles, MostPopular, maxx
    if message == "SendMeSad":
        answer = Smiles[0][0]
        Smiles[0][1] += 1
        if Smiles[0][1] > maxx:
            maxx = Smiles[0][1]
            MostPopular = Smiles[0][0]
    elif message == "SendMeHappy":
        answer = Smiles[1][0]
        Smiles[1][1] += 1
        if Smiles[1][1] > maxx:
            maxx = Smiles[1][1]
            MostPopular = Smiles[1][0]
    elif message == "SendMeMad":
        answer = Smiles[2][0]
        Smiles[2][1] += 1
        if Smiles[2][1] > maxx:
            maxx = Smiles[2][1]
            MostPopular = Smiles[2][0]
    elif message == "SendMeLove":
        answer = Smiles[3][0]
        Smiles[3][1] += 1
        if Smiles[3][1] > maxx:
            maxx = Smiles[3][1]
            MostPopular = Smiles[3][0]
    elif message == "SendMeВедмідь":
        answer = Smiles[4][0]
        Smiles[4][1] += 1
        if Smiles[4][1] > maxx:
            maxx = Smiles[4][1]
            MostPopular = Smiles[4][0]
    elif message == "SendMeIDontKnownWhat":
        answer = Smiles[5][0]
        Smiles[5][1] += 1
        if Smiles[5][1] > maxx:
            maxx = Smiles[5][1]
            MostPopular = Smiles[5][0]
    elif message == "GiveMeDiretide":
        answer = Smiles[6][0]
        Smiles[6][1] += 1
        if Smiles[6][1] > maxx:
            maxx = Smiles[6][1]
            MostPopular = Smiles[6][0]
    elif message == "Random":
        r = choice(Smiles)
        answer = Smiles[r][0]
        Smiles[r][1] += 1
        if Smiles[r][1] > maxx:
            maxx = Smiles[r][1]
            MostPopular = Smiles[r][0]
    elif message == "MostPopular":
        answer = MostPopular
    elif message == "ShowMeStats":
        Smiles = sorted(Smiles, key=lambda x: x[1], reverse=True)
        answer = ""
        m = 1
        for i in Smiles:
            answer += str(m) + " - " + i[0] + " with " + str(i[1]) + " call(s)" + "\n"
            m += 1
    elif message == "Goodbye":
        answer = "Goodbye" + " " + nickname
    return answer

#hgggfnfjcgh'gh';ldhjd;k
if __name__ == "__main__":
    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
