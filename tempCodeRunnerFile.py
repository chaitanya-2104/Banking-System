  file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            pass
            #print(f"{item.accNo:23}","FGHJKLFGHJK", f"{item.name:20s}", " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("No records to display")