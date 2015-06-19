
def sendText (numbers, message):
    for i in range len(numbers):
        server.sendmail('Your Team', numbers[i], message)