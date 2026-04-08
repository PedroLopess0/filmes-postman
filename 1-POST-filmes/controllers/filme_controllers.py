from models.filme_models import Filme   
from db import db                        
import json                              
from flask import make_response         

def create_filme(filme_data):            
    novo_filme = Filme(                  
        titulo=filme_data['titulo'],     
        genero=filme_data['genero'],       
        diretor=filme_data['diretor']  
        ano de lancamento=filme_data['ano de lancamento']
        duracao=filme_data['duracao']
    )
    db.session.add(novo_filme)         
    db.session.commit()                  
    response = make_response(           
        json.dumps({                      
            'mensagem': 'Filme cadastrado com sucesso.',  
            'filme': novo_filme.json()  
        }, sort_keys=False)               
    )
    response.headers['content-Type'] = 'application/json'  
    return response                      

