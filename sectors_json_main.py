import json

class Setores(object):

     def convert_list_json(self):

          sector_list = ['Nucleo de Modernizacao da Atividade Legislativa',
                         'SEDOL',
                         'asdadsa',
                         'BRASILIA',
                         'MAGDA']

          with open("jsons/sectors.json", "w") as write_file:
               json.dump(sector_list, write_file)

if __name__ == "__main__":

     Setores().convert_list_json()