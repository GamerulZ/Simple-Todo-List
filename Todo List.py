import os

def clear():
    os.system('cl||clear')

titel = '''
************  ************  ********      ************
************  ************  *********     ************
    ****      ****    ****  ****    ****  ****    ****
    ****      ****    ****  ****    ****  ****    ****
    ****      ****    ****  ****    ****  ****    ****
    ****      ************  *********     ************
    ****      ************  ********      ************
'''

menu = '''
1 - Add to the list
2 - Read the list
0 - Exit
'''

menu2 = '''
0 - Go back
'''

list = []

itemIndex = 0

i = 0



while True:
    clear()
    print(titel)
    print(menu)
    inp = input(">")

    if inp == "1":
        clear()
        print(titel)
        print(menu2)
        while True:
            add = input(">")
            itemIndex += 1
            if add == "0":
                break
            else:
                clear()
                print(titel)
                print(menu2)
                print(f"{itemIndex} items added")
                list.append(add)
    elif inp == "2":
        clear()
        print(titel)
        print(menu2)
        while True:  
            for name in list:
                i += 1
                print(f"{i}. {name}")

            back = input(">")

            if back == "0":
                break
            else:
                clear()
                print(titel)
                print(menu2)
                print("Pleas enter a valid comand!")
    elif inp == "0":
        break