import json

class Setores(object):


    def convert_list_json(self):

        sector_list = ['Secretária de Transparência',
                        'Secretária de Finanças, Orçamento e Contabilidade',
                        'Secretária de Patrimônio',
                        'Secretária de Administração de Contratações',
                        'Secretária de Gestão de Pessoas',
                        'Secretária de Infraestrutura',
                        'Secretária de Gestão de Informação e Documentação',
                        'Secretária de Tecnologia da Informação PRODASEN',
                        'Secretária de Editoração e Publicações',
                        'Secretária de Polícia Legislativa',
                        'Secretária de Apoio a Orgãos do Parlamento',
                        'Secretária de Atas e Diários',
                        'Secretária de Comissões',
                        'Secretária de Informação Legislativa',
                        'Secretária Legislativa do Congresso Nacional',
                        'Secretária Legislativa do Senado Federal',
                        'Secretária de Registro e Redação Parlamentar']

        with open("jsons/sectors.json", "w") as write_file:
             json.dump(sector_list, write_file)

    def list_sectors():

        sectors = open('jsons/sectors.json', 'r')
        list_sectors = json.load(sectors)
        sectors.close()

        return list_sectors

if __name__ == "__main__":

     Setores().convert_list_json()