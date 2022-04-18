from AnonymousSurvey import AnonymousSurvey

q1 = AnonymousSurvey("What's your hobby?")
q1.printQuestion()

hobbies = ["Reading", "Sleeping", "Listen to Music", "Sports", "Hiking"]
for hobby in hobbies:
    q1.addResponse(hobby)

q1.printResponse()

def getHobbiesResponses():
    return hobbies