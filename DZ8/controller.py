from data_processing import get_data_from_console
from model import read_db, add_to_db, export_to_csv
from view_mod import show_base as sb


def controller(number):
    match number:
        case '0':
            sb(read_db())
            return "*"
        case '1':

            return "*"
        case '2':
            return "*"
        case '3':
            export_to_csv()
            return "*"
        case '4':
            add_to_db(get_data_from_console())
            return "*"
        case '5':
            export_to_csv()
            return "*"
        case '6':
            # import_from_txt()
            return "*"
        case '7':
            return "*"
        case '8':
            return "-"
