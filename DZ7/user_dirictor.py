from this import d
import telef
import dobavl_pol as book 

def surname_view():
    d = telef.get_surname()
    book.add_surname(d)
def telef_view():
    d0,d1,d2,d3,d4  = telef.get_telef(),telef.get_telef(),telef.get_telef()\
        ,telef.get_telef()
    d = d0,d1,d2,d3,d4
    book.add_telef(d)
    return d
def name_view():
    d = telef.get_name()
    book.add_name(d)
    return d
def number_view():
    d = telef.get_number()
    book.add_number(d)
    return d
def discription_view():
    d = telef.get_description()
    book.add_description(d)
    return d