from __future__ import annotations
from client import *
from document import *


if __name__ == "__main__":
    
    # Inicialização
    
    author = Author()
    admin = Admin()
    user = User()
    document = Document()
    
    # Teste Dinâmica
    
    document.render(author)
    author.publish(document)
    document.render(author)
    admin.review(document, False)
    document.render(admin)
    admin.publish(document)
    document.render(admin)
    document.expire()
    document.render(author)
    author.publish(document)
    document.render(author)
    admin.review(document, True)
    document.render(admin)
    document.expire()

    # Teste Erro (realize um por vez)
    # document.render(user)
    # document.expire()
    # admin.review(document, True)
    # user.publish(document)

    author.publish(document)

    # Teste Erro 2 (Um por vez)
    # document.expire()
    # author.review(document, True)
    # admin.publish(document)

    admin.review(document, True)

    # Teste Erro 3 (Um por vez)
    # admin.review(document, True)
    # admin.publish(document)