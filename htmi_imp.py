from cgitb import html
from user_dirictor import surname_view
from user_dirictor import name_view
from user_dirictor import phone_number_view
from user_dirictor import discription_view


def create():
    style= 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '·='.format(style, surname_view())
    html += '·='.format(style,name_view())
    html += '+='.format(style, phone_number_view())
    html += '+='.format(style, discription_view())
    html += ' </body>\n<html>'
    with open('index.html','w') as page:
        page.write(html)
