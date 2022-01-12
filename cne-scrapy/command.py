from cmdline import cmd_parser
from cne import Cne, CneParser
from logger import logger
from utils import to_csv, get_full_name_csv


def get_dni_list_info_data_output(results):
    output_data = []
    for html_content, dni in results:
        dni_map_info = CneParser(html_content, dni).get_data()
        if dni_map_info is not None:
            output_data.append(dni_map_info)
    return output_data

def main():
    option = cmd_parser()
    dni_list = option.dni
    output_dir = option.output_dir
    csv_name = option.name

    if dni_list:
        cne = Cne(dni_list)
        logger.info(' Starting data extraction')
        cne.start()
        logger.info(' Parsing data')
        dni_list_info_data_output = get_dni_list_info_data_output(cne.results)
        logger.info(' Building Csv')
        filename_csv = get_full_name_csv(output_dir, csv_name)
        to_csv(filename_csv, dni_list_info_data_output)
        logger.info(' Csv created {}'.format(filename_csv))
    else:
        logger.warning(' Dni list is empty')

if __name__ == '__main__':
    main()