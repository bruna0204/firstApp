import requests
def exemplo_cep():
    CEP = "16702144"
    url = f"https://viacep.com.br/ws/{CEP}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados_cep = response.json()
        print(f"Logradouro: {dados_cep['logradouro']}")
        print(f"Bairro: {dados_cep['bairro']}")
        print(f"Estado: {dados_cep['estado']}")
    else:
        print(f"Erro: {response.status_code}")

def exemplo_get(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    get = requests.get(url)

    if get.status_code == 200:
        dados_get = get.json()
        print(f"title: {dados_get['title']}")
        print(f"conteudo: {dados_get['body']}\n")
    else:
        print(f"Erro: {get.status_code}")
#exeplo get

def exemplo_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    nova_postagem ={
        "title": "Novo titulo",
        "body": "Novo titulo",
        "user_Id": 1,
    }
    post = requests.post(url, json=nova_postagem)
    if post.status_code == 201:
        dados_post = post.json()
        print(f"title: {dados_post['title']}")
        print(f"conteudo: {dados_post['body']}\n")
    else:
        print(f"Erro: {post.status_code}")


def exemplo_put(id, id_usuario):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    nova_postagem = {
        "id": id,
        "title": "Novo titulo",
        "body": "Novo titulo",
        "userId": id_usuario
    }
    antes = requests.get(url)
    put = requests.put(url, json=nova_postagem)

    if put.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f"titulo_antigo: {dados_antes['title']}")
        else:
            print(f"Erro: {put.status_code}")
        dados_put = put.json()
        print(f"title: {dados_put['title']}")
        print(f"conteudo: {dados_put['body']}\n")
    else:
        print(f"Erro: {put.status_code}")

exemplo_put(40,1)