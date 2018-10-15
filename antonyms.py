Antonyms=dict()
Continue='y'
while Continue=='y':
    Word=input("Please enter your word:")
    if Word in Antonyms.keys():
        print("The antonym of "+Word+" is :"+Antonyms[Word])
    else:
        print("The antonym of "+Word+" does not exist!!!")
        KnowTheAntonym=input("Do you know the antonym of "+Word+" ?")
        if KnowTheAntonym=='y':
            Antonym=input("Please enter the antonym of "+Word+":")
            Antonyms[Word]=Antonym
    Continue=input("Do you want to try another word?")