user =(raw_input("enter your day")
user1 = row_input ("enter your meal time")
if user == 'Monday':
    if user1 == 'breakfast':
        print("poha")
    elif user1 == 'lunch':
        print("dal chawal")
    else:
        print("roti sabji")
elif user == 'tuesday':
    if user1 == 'breakfast':
        print("eggs")
    elif user1 == 'lunch':
        print("chhole chawal")
    else:
        print("kheer puri")
elif user == 'wednesday':
    if user1 == 'breakfast':
        print("sandwich")
    elif user1 == 'lunch':
        print("rajma chawal")
    else:
        print("saahi panir")
else:
    print("aaj to party krenge!")
