import json

class inputdata:
    def __init__(self):
        True
        
    def read1_list(self):
        # for reading also binary mode is important
        with open('Num.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list
        
    def read2_list(self):
        # for reading also binary mode is important
        with open('ActiveHour.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def read3_list(self):
        # for reading also binary mode is important
        with open('Frequency.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def read4_list(self):
        # for reading also binary mode is important
        with open('StationName.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def read5_list(self):
        # for reading also binary mode is important
        with open('StationCode.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list
