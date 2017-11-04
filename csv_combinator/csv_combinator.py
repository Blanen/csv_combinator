import re
import os
from csv import DictReader, DictWriter


class Combinator:
    """ bla
    """
    def __init__(self, filepath, filepath_out):
        self.dir = os.path.dirname(filepath)
        self.filepath_out = filepath_out

    def combine(self, regex, folder_parameter, file_inc_parameter):
        output_list = []
        if not os.path.exists(self.dir):
            raise FileNotFoundError()
        for root, dirs, files in os.walk(self.dir, topdown=True):
            file_counter = 1
            for file_ in files:
                fullpath = root + '\\' + file_
                if not fullpath[-3:] == 'csv':
                    # TODO: Customize exception
                    raise Exception()
                re.search(regex, fullpath)
                with open(fullpath, 'r') as file_:
                    reader = DictReader(file_)
                    for row in reader:
                        output_dict = row
                        output_dict.update({folder_parameter:file_counter, file_inc_parameter: file_counter})
                        output_list.append(output_dict)
            file_counter += 1
        with open(self.filepath_out, 'w', newline='') as csvfile:
            dictWriter = DictWriter(csvfile, output_list[0].keys())
            dictWriter.writeheader()
            for dict_ in output_list:
                dictWriter.writerow(dict_)