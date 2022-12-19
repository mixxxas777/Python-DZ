def add_surname(d):

    with open ('telefon_book.bd', 'a') as file:
        file.write('surname: {}\n'
        
    .format (d))

def add_name(d):

    with open ('telefon_book.bd', 'a') as file:
        file.write('name: {}\n'
 .format (d))

def add_number (d):

from tabulate import tabulate1

prinr = ["Surname", "Name", "Phone_number", "Discription"]


def add_data(d):
    with open ('telefon_book.bd', 'a') as file:
        file.write('phone_number: {}\n'
 .format (d))
def add_description(d):
    
        file.write (tabulate(d, headers ='head', tablefmt="grid"·))


    with open ('telefon_book.bd', 'a') as file:
        file.write('discripion: {}\n'.format (d))
