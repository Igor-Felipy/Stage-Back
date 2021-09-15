from operator import pos
from app import db 

#Classe criada para o login de ambas as partes (Estudante e Empresa)
class UserLogin(db.Model):
    __tablename__ = "User"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    user_type = db.Column(db.String)
    cpf_cnpj = db.Column(db.String)


    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def __repr__(self):
        return "<User %r>" % self.username


#Essa classe vai ser responsavel pelos projetos/vagas
class Post(db.Model):
    __tablename__ = "Post"
    
    id = db.Column(db.Integer, primary_key=True)
    post_kind = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, date, post_kind, title, description):
        self.post_kind = post_kind
        self.title = title
        self.description = description
        self.date = date

    def __repr__(self):
        return "<Post %r>" % self.title


#Classe criada para fazer os posts de um projeto
class Media(db.Model):
    __tablename__ = "Media"

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    description = db.Column(db.String)
    post_id = db.Column(db.Integer, db.Foreign_key('Post.id'))

    post = db.relationship('Post', foreign_keys=post_id)


    def __init__(self, link, description, post_id):  
        self.link = link
        self.description = description
        self.post_id = post_id

    def __repr__(self):
       return "<Media %r>" % self.link
