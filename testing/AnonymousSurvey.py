class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def printQuestion(self):
        print(self.question)

    def addResponse(self, response):
        self.responses.append(response)

    def printResponse(self):
        print("Responses we've received: ")
        for r in self.responses:
            print("- {}".format(r))