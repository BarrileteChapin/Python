#Assigment2 --- 108006207



def initialize(balance,records):
    try:
        lista = []
        #reading
        with open('records.txt','r') as fh:
            lines = [x for x in fh.readlines()]
            
            #getting first element (balance)
            balance = int(lines[0])
            #print(f'balance {balance}')
            del lines[0]    #subracting it from main data

            #making a list of tuples
            lista += tuple([i.split() for i in lines])
            #print(lista)

            #Now, checking the values of the input
            for x,y in enumerate(lista):
                y[1] = int(y[1]) #if it doesn't convert -> means there is an exception while reading   
            #    print(f'{y[1]}')
            #print('li')
            #print(lines)

    except FileNotFoundError :
        print(''' 
        /$$$$$$$            /$$      /$$                                        
        | $$__  $$          | $$$    /$$$                                        
        | $$  \ $$ /$$   /$$| $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$
        | $$$$$$$/| $$  | $$| $$ $$/$$ $$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$
        | $$____/ | $$  | $$| $$  $$$| $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  | $$
        | $$      | $$  | $$| $$\  $ | $$| $$  | $$| $$  | $$| $$_____/| $$  | $$
        | $$      |  $$$$$$$| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$
        |__/       \____  $$|__/     |__/ \______/ |__/  |__/ \_______/ \____  $$
                /$$  | $$                                            /$$  | $$
                |  $$$$$$/                                           |  $$$$$$/
                \______/                                             \______/ ''')

        try:
            balance = int(input("""Hello and welcome to PyMoney! 
            Please insert how much money you have:"""))
        except:
            print('Invalid value for money. Set to 0 by default.')
            balance = 0

    except ValueError: 
        print('Invalid format in records.txt, Deleting the contents - (balance is 0 by default)')
        balance=0
        with open('records.txt', 'w') as fh:
            fh.write('0')
    except: 
        print('oops! something unexpected happened')
    else: 
        print('''                                                  
        _ _ _     _                      _           _   
        | | | |___| |___ ___ _____ ___   | |_ ___ ___| |_ 
        | | | | -_| |  _| . |     | -_|  | . | .'|  _| '_|
        |_____|___|_|___|___|_|_|_|___|  |___|__,|___|_,_|                                             
        ''')
        records = lista.copy()
    lista.clear()

    return balance,records
    


def add(balance, records):
    
    lista = []
    balance_aux =0
    try:
        message = input('''\nWould you mind adding an expense or income?
        (description, amount)\n''') 
        tup_ax = message.split(",")
            #making a list of tuples
        lista += tuple(i.split() for i in tup_ax)
            #print(lista)
            #Now, checking the values of the input
            
        for x,y in enumerate(lista):
            y[1] = int(y[1]) #if it doesn't convert -> means there is an exception while reading   
            balance_aux+= y[1]    
    except IndexError:
        print('The input format is corrupted. Please use the following one: description amount')    
    except ValueError: 
        print('Amount is not a number. Please add items again')    
    except:
        print("item/s cannot be added")
    else:
        records += lista.copy()
        balance += balance_aux

    return balance,records


def view(balance, records):
    try:
        print('''\tHere is your information
            Description:\t Amount:
            --------------------------------''')

        for i, j in enumerate(records):
            print(f'\t{j[0]}\t {j[1]}')
        print('\t-----------------------------')
        print(f'\tYour balance is: {balance}')
    except:
        print('nothing to see here...\n')
        

def delete(records):

    ind = []
    
    try:
        val = input('''Which record do you want to delete?
        (insert description and amount): ''')
        val = val.split()
        #finding the item present in the list. 
        ind = [int(x) for x,y in enumerate(records) if (y[0]== val[0] and y[1]==int(val[1]))]
        #print(type(ind[0]))
        del records[ind[0]] #delete item
   
    except ValueError:
        print('The input format is corrupted. Please use the following one: description amount')
    except IndexError: 
        print("item/s not found")
    except: 
        print('item cannot be deleted')

    return records 

def save(balance, records):
    try:
        with open("records.txt",'w') as fh:
            fh.write(f'{balance}\n')
            for x,y in enumerate(records):
                fh.write(f'{y[0]} {y[1]}\n')
    except:
        print('Are you sure? the file was not saved')

if __name__ == '__main__':
    records = []
    balance = 0
    balance, records = initialize(balance,records)
    while True:
        command = input('\nWhat do you want to do (add / view / delete / exit)? ')
        if command == 'add':
            balance, records = add(balance,records)
        elif command == 'view':
            view(balance,records)
        elif command == 'delete':
            records = delete(records)
        elif command == 'exit':
            save(balance,records)
            print("Bye Bye!")
            break
        else:
            print('Invalid command. Try again.\n')

