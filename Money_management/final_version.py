
class Record:
    """Represent a record."""
    def __init__(self,category, item, amount):
        self._category = category
        self._item = item 
        self._amount = int(amount)

    #getters

    @property
    def get_Category(self) :
        return self._category

    @property
    def get_item(self) :
        return self._item

    @property
    def get_amount(self) :
        return self._amount


class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        #a = Record('food','pizza',500)
        self._records = []
        self._balance = 0
        try:
            lista = []
            lista_records = []
            balance_aux=0
        #reading
            with open('records.txt','r') as fh:
                lines = [x for x in fh.readlines()]
                
                #getting first element (balance)
                self._balance = int(lines[0])
                #print(f'balance {balance}')
                del lines[0]    #subracting it from main data

                #making a list of tuples
                lista += tuple([i.split() for i in lines])
                #print(lista)

                #Now, checking the values of the input
                for x,y in enumerate(lista):
                    #print(y)
                    lista_records = [Record(y[0],y[1],y[2])] #if it doesn't convert -> means there is an exception while reading   
                    #balance_aux= int(y[2]) 
                    if(categories.is_category_valid(str(lista[x][0]),categories._categories)):
                        self._records += lista_records.copy()
                     #   self._balance += balance_aux
                    else:
                        print('The specified category is not in the category list.\n You can check the category list by command "view categories".\nFail to add a record.')
                
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
                self._balance = int(input("""Hello and welcome to PyMoney! 
                Please insert how much money you have:"""))
            except:
                print('Invalid value for money. Set to 0 by default.')
                self._balance = 0

        except ValueError: 
            print('Invalid format in records.txt, Deleting the contents - (balance is 0 by default)')
            self._balance=0
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
        lista.clear()

 
    def add(self,categories):
        '''
            insert a new record:
                1. check if item exists in a category
                2. if so, then add it is added to the list
        '''
        lista = []
        lista_records  = []
        balance_aux =0
        try:
            message = input('''\nWould you mind adding an expense or income?
            (description, amount)\n''') 
            tup_ax = message.split(",")
                    #making a list of tuples
            lista += tuple(i.split() for i in tup_ax)

            for x,y in enumerate(lista):
                print(y)
                lista_records += [Record(y[0],y[1],y[2])] #if it doesn't convert -> means there is an exception while reading   
                balance_aux+= int(y[2]) 
                #we need a for loop here later, for multiple entries 
            if(categories.is_category_valid(str(lista[0][0]),categories._categories)):
                self._records += lista_records.copy()
                self._balance += balance_aux
            else:
                print('The specified category is not in the category list.\n You can check the category list by command "view categories".\nFail to add a record.')
            
        except IndexError:
            print('The input format is corrupted. Please use the following one: category description amount')    
        except ValueError: 
            print('Amount is not a number. Please add items again')    
        except:
            print("item/s cannot be added")


    def view(self):
        '''
        show balance and records
        '''
        try:
            print('''\tHere is your information\n
            Category:\t Description:\t \tAmount:
            -------------------------------------------------''')

            for i in self._records:
                print(f'\t{i._category:15}\t {i._item:15}\t {i._amount:8d} ')
            print('\t----------------------------------------------------')
            print(f'\tYour balance is: {self._balance}')
        except:
            print('nothing to see here...\n')
 


    def delete(self):
        ind = []
        try:
            val = input('''Which record do you want to delete?
            (insert category, description and amount): ''')
            val = val.split()
            #finding the item present in the list. 
            ind = [int(x) for x,y in enumerate(self._records) if (y._category== val[0] and y._item == val[1] and y._amount==int(val[2]))]
            #print(type(ind[0]))
            if(len(ind)>1):
                print('Many elements detected, please select an element by its index to delete:')
                for i in ind:
                    print(f'ind: {ind[i]}')
                ind[0] = int(input('please, write the index to delete: '))

            self._balance -= int(self._records[ind[0]]._amount) 
            del self._records[ind[0]] #delete item
        except ValueError:
            print('The input format is corrupted. Please use the following one: description amount')
        except IndexError: 
            print("item/s not found")
        except: 
            print('item cannot be deleted')


 
    def find(self, target):
        '''
        find the items & a global balance for the category inquired. 
        '''
        try:
            records_filtered = list(filter(lambda x: x._category in target ,self._records))
            #print(records_filtered)
            #balance = reduce(lambda a,b: int(a[2])+int(b[2]),records_filtered)
            balance = 0
            print('\tCategory: \t Description:\t \t Amount:') 
            for i in records_filtered:
                print(f'\t{i._category:15}\t {i._item:15}\t {i._amount:8d} ')
                balance+= int(i._amount)
            print('\t-------------------------------------------------')   
            print(f'\tYour balance is: {balance}')
        except:
            print('ooops, the category cannot be found')
 

    def save(self):
        '''
        store data into "records.txt"
        '''
        try:
            with open("records.txt",'w') as fh:
                fh.write(f'{self._balance}\n')
                for x in self._records:
                    fh.write(f'{x._category} {x._item} {x._amount}\n')
        except:
            print('Are you sure? the file was not saved')

class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        # 1. Initialize self._categories as a nested list.
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway','MRT']], 'income', ['salary', 'bonus']]
 

    def view(self,categories,prefix=()):
        '''
        show defined categories
        '''
        if type(categories) in {list, tuple}:
            count = 0
            for v in categories: 
                if type(v) not in {list,tuple}:
                    count+=1
                self.view(v,prefix+(count,))
        else:
            see = ' '*5*(len(prefix)-1)
            see += '-' + categories
            print(see)
 

    def is_category_valid(self,category, categories):
        ''''
        Check whether the arg (category) is in the list of categories
        return value: True or False
        '''
        if type(categories) == list:
                for i, v in enumerate(categories):
                    p = self.is_category_valid(category, v)
                    if p == True:
                        return p
        return categories == category
 

    
    def find_subcategories(self,category):
        '''
        find a category and subcategories
        return a list
        '''
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                if(found==True):
                    #print(f'here we go {categories}')
                    #print(f'here cat  {category}')
                    for index, child in enumerate(categories):
                        yield from find_subcategories_gen(category, child,True)
                    
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child,False)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list and found == False:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.   
                        #print(f'INSIDE: {categories}')
                        yield from find_subcategories_gen(category,categories[index:index + 2],True)
            else:
                #if(found==True):
                #    print(f'go {categories}')
                if (categories == category or found==True):
                    yield categories

        
        return  [x for x in find_subcategories_gen(category,self._categories)]


import sys
 
# class definitions here
 
categories = Categories()
records = Records()
 
while True:
    command = input('\nWhat do you want to do (add / view / view categories / find / delete / exit)? ')
    if command == 'add':
        records.add(categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        records.delete()
    elif command == 'view categories':
        categories.view(categories._categories)
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        print(target_categories)
        records.find(target_categories)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')
