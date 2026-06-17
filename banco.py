from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://paula:fatec@cluster0.vff9tgy.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercadoLivre

#####  USUÁRIOS  #####

### CREATE
def create_usuario():
    global db
    mycol = db.usuario
    mycol.create_index([("cpf", ASCENDING)], unique=True)
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = ''
    end = []
    while (key.upper() != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {       
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) 
        key = input("Deseja cadastrar um novo endereço (Digite N para sair)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end }
    try:
        x = mycol.insert_one(mydoc)
        print("Usuário criado com sucesso! :D\n")
    except DuplicateKeyError:
        print("Erro: já existe um usuário com esse CPF :O\n")

### DELETE
def delete_usuario(cpf):
    #Delete
    global db
    mycol = db.usuario
    myquery = {"cpf": cpf}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o usuário :(\n")
    print("\nBye bye...\n")

### READ
def read_usuario(cpf):
    global db
    mycol = db.usuario
    if not cpf:
        mydoc = mycol.find().sort("nome")
    else:
        mydoc = mycol.find({"cpf": cpf})
    for x in mydoc:
        print(f"Nome: {x.get('nome')} {x.get('sobrenome')}")
        print(f"CPF: {x.get('cpf')}")
        enderecos = x.get("end", [])
        if not enderecos:
            print("  Nenhum endereço cadastrado :/\n")
        else:
            for i, e in enumerate(enderecos, start=1):
                print("ENDEREÇO")
                print(f"Rua: {e.get('rua')}, Nº: {e.get('num')}")
                print(f"Bairro: {e.get('bairro')}")
                print(f"Cidade: {e.get('cidade')} - {e.get('estado')}")
                print(f"CEP: {e.get('cep')}")

### UPDATE

def update_usuario(cpf):
    global db
    mycol = db.usuario
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)
    if not mydoc:
        print("\nUsuário não encontrado! :(\n")
        return
    print("USUÁRIO")
    print(mydoc)
    nome = input("Mudar Nome: ")
    if nome:
        mydoc["nome"] = nome
    sobrenome = input("Mudar Sobrenome: ")
    if sobrenome:
        mydoc["sobrenome"] = sobrenome
    if "end" in mydoc and len(mydoc["end"]) > 0:
        endereco = mydoc["end"][0]
        print("ENDEREÇO")
        print(endereco)
        key = input("\nDeseja editar o endereço? (S/N): ")
        if key.upper() == 'S':
            rua = input("Nova Rua: ")
            if rua:
                endereco["rua"] = rua
            num = input("Novo Número: ")
            if num:
                endereco["num"] = num
            bairro = input("Novo Bairro: ")
            if bairro:
                endereco["bairro"] = bairro
            cidade = input("Nova Cidade: ")
            if cidade:
                endereco["cidade"] = cidade
            estado = input("Novo Estado: ")
            if estado:
                endereco["estado"] = estado
            cep = input("Novo CEP: ")
            if cep:
                endereco["cep"] = cep
            mydoc["end"][0] = endereco
    mycol.update_one(myquery, {"$set": mydoc})
    print("\nUsuário atualizado com sucesso! :D\n")

#####  VENDEDORES  #####

### CREATE
def create_vendedor():
    global db
    mycol = db.vendedor
    mycol.create_index([("cpf", ASCENDING)], unique=True)
    print("\nInserindo um novo vendedor\n")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = ''
    end = []
    while (key.upper() != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {       
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) 
        key = input("Deseja cadastrar um novo endereço (Digite N para sair)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end }
    try:
        x = mycol.insert_one(mydoc)
        print("\nVendedor inserido com sucesso! :D\n")
    except DuplicateKeyError:
        print("\nErro: já existe um usuário com esse CPF :O\n")

### DELETE
def delete_vendedor(cpf):
    global db
    mycol = db.vendedor
    myquery = {"cpf": cpf}
    mydoc = mycol.delete_one(myquery)
    print("\nDeletado o usuário D:\n")

### READ
def read_vendedor(cpf):
    global db
    mycol = db.vendedor
    if not cpf:
        mydoc = mycol.find().sort("nome")
    else:
        mydoc = mycol.find({"cpf": cpf})
    for x in mydoc:
        print(f"Nome: {x.get('nome')} {x.get('sobrenome')}")
        print(f"CPF: {x.get('cpf')}")
        enderecos = x.get("end", [])
        if not enderecos:
            print("Nenhum endereço cadastrado :/")
        else:
            for i, e in enumerate(enderecos, start=1):
                print("ENDEREÇO")
                print(f"Rua: {e.get('rua')}, Nº: {e.get('num')}")
                print(f"Bairro: {e.get('bairro')}")
                print(f"Cidade: {e.get('cidade')} - {e.get('estado')}")
                print(f"CEP: {e.get('cep')}")
        produtos = x.get("produtos", [])
        if not produtos:
            print("\nVendedor não possui produtos cadastrados :(\n")
        else:
            for i, e in enumerate(produtos, start=1):
                print("PRODUTOS")
                print(f"Produto: {e.get('nomeProduto')}")
                print(f"Preço: {e.get('preco')}")
                print(f"Descrição: {e.get('descricao')}")

### UPDATE

def update_vendedor(cpf):
    global db
    mycol = db.vendedor
    myquery = {"cpf": cpf}
    mydoc = mycol.find_one(myquery)
    if not mydoc:
        print("\nVendedor não encontrado! :(\n")
        return
    print("VENDEDOR")
    print(mydoc)
    nome = input("Mudar Nome: ")
    if nome:
        mydoc["nome"] = nome
    sobrenome = input("Mudar Sobrenome: ")
    if sobrenome:
        mydoc["sobrenome"] = sobrenome
    if "end" in mydoc and len(mydoc["end"]) > 0:
        endereco = mydoc["end"][0]
        print("ENDEREÇO")
        print(endereco)
        key = input("\nDeseja editar o endereço? (S/N): ")
        if key.upper() == 'S':
            rua = input("Nova Rua: ")
            if rua:
                endereco["rua"] = rua
            num = input("Novo Número: ")
            if num:
                endereco["num"] = num
            bairro = input("Novo Bairro: ")
            if bairro:
                endereco["bairro"] = bairro
            cidade = input("Nova Cidade: ")
            if cidade:
                endereco["cidade"] = cidade
            estado = input("Novo Estado: ")
            if estado:
                endereco["estado"] = estado
            cep = input("Novo CEP: ")
            if cep:
                endereco["cep"] = cep
            mydoc["end"][0] = endereco
    mycol.update_one(myquery, {"$set": mydoc})
    print("\nVendedor atualizado com sucesso! :D\n")

#####  PRODUTOS  #####

### CREATE
def get_ID():
    global db
    counters = db.counters
    result = counters.find_one_and_update(
        {"_id": "produtoId"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=True
    )
    return result["seq"]

def create_produto():
    global db
    mycol = db.produtos
    mycolVend = db.vendedor
    nomeProduto = input("Nome: ")
    preco = input("Preço: ")
    descricao = input("Descrição: ")
    cpf = input("CPF do vendedor: ")
    vendedor = mycolVend.find_one({"cpf": cpf})
    if not vendedor:
        print("\nVendedor não existe! D: \n")
        return
    id = get_ID()
    mydoc = {
        "id": id,
        "nomeProduto": nomeProduto,
        "preco": preco,
        "descricao": descricao,
        "cpfVendedor": cpf 
    }
    mycol.insert_one(mydoc)
    print("\nProduto criado com sucesso :D!")

### DELETE
def delete_produto(id):
    global db
    mycol = db.produtos
    result = mycol.delete_one({"id": int(id)})
    if result.deleted_count:
        print("\nProduto deletado com sucesso :O\n")
    else:
        print("\nProduto não existe :/\n")

### READ
def read_produto(id):
    global db
    mycol = db.produtos
    if not id:
        mydoc = mycol.find().sort("id", 1)
    else:
        mydoc = mycol.find({"id": int(id)})
    for x in mydoc:
        vendedor = db.vendedor.find_one({"cpf": x.get("cpfVendedor")})
        print(f"Produto: {x.get('nomeProduto')}")
        print(f"Preço: {x.get('preco')}")
        print(f"Descrição: {x.get('descricao')}")
        print(f"Vendedor: {vendedor.get('nome') if vendedor else 'N/A'}")

### UPDATE
def update_produto(id):
    global db
    mycol = db.produtos
    produto = mycol.find_one({"id": int(id)})
    if not produto:
        print("\nProduto não encontrado :/\n")
        return
    print("Update de produto, pressione ENTER para manter informações")
    nomeProduto = input("Novo nome: ")
    preco = input("Novo preço: ")
    descricao = input("Nova descrição: ")
    novoProduto = {}
    if nomeProduto:
        novoProduto["nomeProduto"] = nomeProduto
    if preco:
        novoProduto["preco"] = preco
    if descricao:
        novoProduto["descricao"] = descricao
    mycol.update_one({"id": int(id)}, {"$set": novoProduto})
    print("\nProduto atualizado com sucesso! :D\n")

#####  COMPRAS  #####

### CREATE
def create_compra(cpf):
    mycolUser = db.usuario
    mycolProd = db.produtos
    mycolComp = db.compras
    usuario = mycolUser.find_one({"cpf": cpf})
    if not usuario:
        print("Usuário não existe :(")
        return
    key = ''
    compras = []
    while (key.upper() != 'N'):
        try:
            id = input("Produto comprado (ID): ")
        except:
            print("ID inválido :(")
            continue
        produto = mycolProd.find_one({"id": int(id)})
        if not produto:
            print("Produto não existe!")
            continue
        compras.append({
            "id": produto.get("id"),
            "nomeProduto": produto.get("nomeProduto"),
            "preco": produto.get("preco")
        })
        key = input("Adicionar mais produtos? (N para sair) ")

    myDoc = {
        "usuario": {
            "cpf": usuario.get("cpf"),
            "nome": usuario.get("nome")
        },
        "compras": compras
    }
    mycolComp.insert_one(myDoc)
    print("\nCompra registrada com sucesso! $$\n")

### DELETE
def delete_compra(cpf):
    global db
    mycol = db.compras
    result = mycol.delete_one({"usuario.cpf": cpf})
    if result.deleted_count:
        print("\nHistórico deletado com sucesso :O\n")
    else:
        print("\nHistórico não existe :/\n")

### READ
def read_compras(cpf):
    global db
    mycol = db.compras
    if not cpf:
        mydoc = mycol.find().sort("usuario.cpf", 1)
    else:
        mydoc = mycol.find({"usuario.cpf": cpf})
    for x in mydoc:
        usuario = x.get("usuario", {})
        compras = x.get("compras", [])
        print(f"Usuário: {usuario.get('nome')}")
        print(f"CPF: {usuario.get('cpf')}")
        for p in compras:
            print(f"ID: {p.get('id')}")
            print(f"Nome: {p.get('nomeProduto')}")
            print(f"Preço: {p.get('preco')}")
 
### UPDATE
def update_compra(cpf):
    global db
    mycol = db.compras
    compra = mycol.find_one({"usuario.cpf": cpf})
    if not compra:
        print("\nCompra não encontrada\n")
        return
    produtos = compra.get("compras", [])
    opc = ''
    while opc.upper() != 'N':
        print("\n1 - Adicionar Produto (N para sair)")
        print("2 - Remover Produto")
        opc = input("Selecione uma opção: ")
        if opc == '1':
            try:
                produto_id = int(input("ID do produto: "))
            except:
                print("Produto não existe! :O")
                continue
            prod = db.produtos.find_one({"id": produto_id})
            if not prod:
                print("Produto não existe! :O")
            else:
                produtos.append({
                    "id": prod.get("id"),
                    "nomeProduto": prod.get("nomeProduto"),
                    "preco": prod.get("preco")
                })
                print("\nProduto adicionado a compras :D!\n")
        elif opc == '2':
            if not produtos:
                print("Compra vazia :/")
                continue
            print("\nProdutos na compra:")
            for i, p in enumerate(produtos):
                print(f"{i} - {p.get('nomeProduto')}")
            try:
                indice = int(input("Selecione um produto: "))
                if 0 <= indice < len(produtos):
                    removido = produtos.pop(indice)
                    print(f"{removido.get('nomeProduto')} removido!")
                else:
                    print("Produto inválido! :(")
            except:
                print("Produto inválido! :(")
        mycol.update_one({"usuario.cpf": cpf}, {"$set": {"compras": produtos}})

    print("\nAtualização bem sucedida!")

#####  FAVORITOS  #####

### CREATE
def create_favoritos(cpf):
    mycolUser = db.usuario
    mycolProd = db.produtos

    usuario = mycolUser.find_one({"cpf": cpf})
    if not usuario:
        print("Usuário não existe :(")
        return

    favoritos = usuario.get("favoritos", [])

    key = ''
    while key.upper() != 'N':
        try:
            id = int(input("Produto favorito (ID): "))
        except:
            print("ID inválido :(")
            continue

        produto = mycolProd.find_one({"id": id})
        if not produto:
            print("Produto não existe!")
            continue

        # Evita produtos duplicados
        if any(p["id"] == id for p in favoritos):
            print("Produto já está nos favoritos!")
        else:
            favoritos.append({
                "id": produto.get("id"),
                "nomeProduto": produto.get("nomeProduto"),
                "preco": produto.get("preco")
            })
            print("Produto adicionado aos favoritos!")

        key = input("Adicionar mais produtos? (N para sair) ")

    mycolUser.update_one(
        {"cpf": cpf},
        {"$set": {"favoritos": favoritos}}
    )

    print("\nLista de favoritos atualizada com sucesso! :D\n")

### READ
def read_favoritos(cpf):
    mycolUser = db.usuario

    if not cpf:
        usuarios = mycolUser.find().sort("nome")
    else:
        usuarios = mycolUser.find({"cpf": cpf})

    for usuario in usuarios:
        print(f"\nUsuário: {usuario.get('nome')}")
        print(f"CPF: {usuario.get('cpf')}")

        favoritos = usuario.get("favoritos", [])

        if not favoritos:
            print("Nenhum favorito cadastrado :/")
        else:
            print("FAVORITOS")
            for p in favoritos:
                print(f"ID: {p.get('id')}")
                print(f"Nome: {p.get('nomeProduto')}")
                print(f"Preço: {p.get('preco')}")

### DELETE
def delete_favorito(cpf):
    mycolUser = db.usuario

    resultado = mycolUser.update_one(
        {"cpf": cpf},
        {"$set": {"favoritos": []}}
    )

    if resultado.matched_count:
        print("\nLista de favoritos apagada com sucesso! :O\n")
    else:
        print("\nUsuário não encontrado :/\n")
 
### UPDATE
def update_favoritos(cpf):
    mycolUser = db.usuario

    usuario = mycolUser.find_one({"cpf": cpf})
    if not usuario:
        print("\nUsuário não encontrado!\n")
        return

    favoritos = usuario.get("favoritos", [])

    opc = ''
    while opc.upper() != 'N':
        print("\n1 - Adicionar Produto")
        print("2 - Remover Produto")
        print("N - Sair")

        opc = input("Selecione uma opção: ")

        if opc == '1':
            try:
                produto_id = int(input("ID do produto: "))
            except:
                print("ID inválido!")
                continue

            prod = db.produtos.find_one({"id": produto_id})
            if not prod:
                print("Produto não existe!")
            elif any(p["id"] == produto_id for p in favoritos):
                print("Produto já está nos favoritos!")
            else:
                favoritos.append({
                    "id": prod.get("id"),
                    "nomeProduto": prod.get("nomeProduto"),
                    "preco": prod.get("preco")
                })
                print("Produto adicionado!")

        elif opc == '2':
            if not favoritos:
                print("Lista vazia :/")
                continue

            print("\nProdutos na lista:")
            for i, p in enumerate(favoritos):
                print(f"{i} - {p.get('nomeProduto')}")

            try:
                indice = int(input("Selecione um produto: "))
                if 0 <= indice < len(favoritos):
                    removido = favoritos.pop(indice)
                    print(f"{removido.get('nomeProduto')} removido!")
                else:
                    print("Produto inválido!")
            except:
                print("Produto inválido!")

    mycolUser.update_one(
        {"cpf": cpf},
        {"$set": {"favoritos": favoritos}}
    )

    print("\nAtualização bem sucedida!")
  
key = ''
sub = ''
sub2 = ''
while (key.upper() != 'S'):
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    print("4-CRUD Compras")
    key = input("Digite a opção desejada? (S para sair) ")

    if (key == '1'):
        print("Menu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        print("5-Lista de Favoritos")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create usuario")
            create_usuario()
        elif (sub == '2'):
            cpf = input("Informe o CPF do usuário ou pressione ENTER para todos: ")
            read_usuario(cpf)
        elif (sub == '3'):
            cpf = input("Informe o CPF do usuário: ")
            update_usuario(cpf)
        elif (sub == '4'):
            print("delete usuario")
            cpf = input("Informe o CPF do usuário: ")
            delete_usuario(cpf)
        elif (sub == '5'):
            print("Lista de Favoritos")
            print("1-Adicionar Produto")
            print("2-Mostrar Favoritos")
            print("3-Atualizar Favoritos")
            print("4-Remover Produto")
            sub2 = input("Digite a opção desejada? (V para voltar) ")
            if (sub2 == '1'):
                cpf = input("Informe o CPF do usuário: ")
                create_favoritos(cpf)
            elif (sub2 == '2'):
                cpf = input("Informe o CPF do usuário ou pressione ENTER para todos: ")
                read_favoritos(cpf) 
            elif (sub2 == '3'):
                cpf = input("Informe o CPF do usuário: ")
                update_favoritos(cpf)
            elif (sub2 == '4'):
                cpf = input("Informe o CPF do usuário: ")
                delete_favorito(cpf)
            
    elif (key == '2'):
        print("Menu do Vendedor")        
        print("1-Create Vendedor")
        print("2-Read Vendedor")
        print("3-Update Vendedor")
        print("4-Delete Vendedor")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create vendedor")
            create_vendedor()
        elif (sub == '2'):
            cpf = input("Read vendedor, deseja algum nome especifico? (Pressione enter se quiser todos) ")
            read_vendedor(cpf) 
        elif (sub == '3'):
            cpf = input("Informe o CPF do usuário: ")
            update_vendedor(cpf)
        elif (sub == '4'):
            cpf = input("Informe o CPF do usuário: ")
            delete_vendedor(cpf)
    elif (key == '3'):
        print("Menu do Produto")
        print("1-Create Produto")
        print("2-Read Produto")
        print("3-Update Produto")
        print("4-Delete Produto")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create produto")
            create_produto()
        elif (sub == '2'):
            id = input("Informe o ID do produto ou pressione ENTER para todos: ")
            read_produto(id)
        elif (sub == '3'):
            id = input("Informe o ID do produto: ")
            update_produto(id)
        elif (sub == '4'):
            id = input("Informe o ID do produto: ")
            delete_produto(id)

    elif(key == '4'):
        print("Menu de Compras")
        print("1-Realizar Compra")
        print("2-Read Compras")
        print("3-Update Compras")
        print("4-Delete Compras")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
                cpf = input("Informe o CPF do usuário: ")
                create_compra(cpf)
        elif (sub == '2'):
                cpf = input("Informe o CPF do usuário ou pressione ENTER para todos: ")
                read_compras(cpf)
        elif (sub == '3'):
                cpf = input("Informe o CPF do usuário: ")
                update_compra(cpf)
        elif (sub == '4'):
                cpf = input("Informe o CPF do usuário: ")
                delete_compra(cpf)
print("Tchau Prof...")