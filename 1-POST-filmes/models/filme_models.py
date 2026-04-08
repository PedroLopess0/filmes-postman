from db import db                       

class Comida(db.Model):                  
    __tablename__ = 'comidas'              

    titulo = db.Column(db.Integer, primary_key=True)          
    genero = db.Column(db.String(80), nullable=False)    
    diretor = db.Column(db.String(80), nullable=False)      
    ano de lancamento = db.Column(db.Integer, nullable=False) 
    duracao = db.Column(db.Integer, nullable=False)


        return {
    def json(self):                                
            'titulo': self.titulo,         
            'genero': self.genero,    
            'diretor': self.diretor,      
            'ano de lancamento': self.ano de lancamento
            'duracao': self.duracao           
        }