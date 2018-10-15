a=dict()
Continue="y"
while Continue=="y":
    word=input("Lotfan kalame khod ra vared konid:")
    if word in a.keys():
        print("Antonym of " + word  +":" + a[word])
    else:
        Answer=input("Man nemidanam. Aya to midani?")
        if Answer=="y":
            a[word]=input("Motezad ra vard kon:")
    Continue=input("Aya mikhahid edame dahid?")
