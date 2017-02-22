'''
Created on 15 de fev de 2017

@author: Gustavo
'''
from pprint import pprint

def jsonRead(field):
    import json

    with open ("perfil.json") as data_file :
        dataJson=json.load(data_file)
    
    return dataJson[field]
    

def main():
    
    campo=input("Qual campo quer pesquisar? Idade, nome, telefone ou id? ")
    s=jsonRead(campo)
    print(s)
    
main()