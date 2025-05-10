from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# --------- DADOS FICTÍCIOS DE PROJETOS ---------
projetos = [
    # Não finalizados (criando)
    {"id": 1, "nome": "Projeto Alfa", "data": datetime(2025, 5, 13), "status": "criando"},
    {"id": 2, "nome": "Projeto Beta", "data": datetime(2025, 5, 12), "status": "criando"},
    {"id": 3, "nome": "Projeto Gama", "data": datetime(2025, 5, 11), "status": "criando"},
    {"id": 4, "nome": "Projeto Delta", "data": datetime(2025, 5, 10), "status": "criando"},
    {"id": 5, "nome": "Projeto Épsilon", "data": datetime(2025, 5, 9), "status": "criando"},
    # Recentes (aguardando/revisão)
    {"id": 6, "nome": "Projeto Zeta", "data": datetime(2025, 5, 8), "status": "aguardando"},
    {"id": 7, "nome": "Projeto Eta", "data": datetime(2025, 5, 7), "status": "revisão"},
    {"id": 8, "nome": "Projeto Teta", "data": datetime(2025, 5, 6), "status": "aguardando"},
    {"id": 9, "nome": "Projeto Iota", "data": datetime(2025, 5, 5), "status": "revisão"},
    {"id": 10, "nome": "Projeto Kappa", "data": datetime(2025, 5, 4), "status": "aguardando"},
    # Em andamento
    {"id": 11, "nome": "Projeto Lambda", "data": datetime(2025, 5, 3), "status": "em andamento"},
    {"id": 12, "nome": "Projeto Mi", "data": datetime(2025, 5, 2), "status": "em andamento"},
    {"id": 13, "nome": "Projeto Ni", "data": datetime(2025, 5, 1), "status": "em andamento"},
    {"id": 14, "nome": "Projeto Xi", "data": datetime(2025, 4, 30), "status": "em andamento"},
    {"id": 15, "nome": "Projeto Ômicron", "data": datetime(2025, 4, 29), "status": "em andamento"},
]

# --------- DADOS FICTÍCIOS DOS ORÇAMENTOS ---------
orcamentos = [
    {
        "id": 1,
        "projeto": "Reforma Predial",
        "data": "10/05/2025",
        "cidade_uf": "São Paulo/SP",
        "base": "ABNT",
        "cliente": "Construtora Alpha"
    },
    {
        "id": 2,
        "projeto": "Instalação Elétrica",
        "data": "09/05/2025",
        "cidade_uf": "Rio de Janeiro/RJ",
        "base": "ISO",
        "cliente": "Engenharia Beta"
    }
]

# Listas para filtros de orçamentos
clientes = ["Construtora Alpha", "Engenharia Beta"]
estados = ["SP", "RJ"]
cidades = ["São Paulo", "Rio de Janeiro"]
anos = ["2025", "2024"]

# --------- ROTAS ---------

@app.route('/')
def inicio():
    agora = datetime.now()
    mes_atual = agora.month
    ano_atual = agora.year

    projetos_mes = [p for p in projetos if p['data'].month == mes_atual and p['data'].year == ano_atual]
    projetos_ano = [p for p in projetos if p['data'].year == ano_atual]
    projetos_total = len(projetos)

    # Projetos não finalizados (criando)
    projetos_nao_finalizados = sorted(
        [p for p in projetos if p['status'] == "criando"],
        key=lambda x: x['data'],
        reverse=True
    )[:5]

    # Projetos recentes (aguardando ou revisão)
    projetos_recentes = sorted(
        [p for p in projetos if p['status'] in ["aguardando", "revisão"]],
        key=lambda x: x['data'],
        reverse=True
    )[:5]

    # Projetos em andamento
    projetos_andamento = sorted(
        [p for p in projetos if p['status'] == "em andamento"],
        key=lambda x: x['data'],
        reverse=True
    )[:5]

    return render_template(
        'inicio.html',
        titulo='Início',
        projetos_mes=len(projetos_mes),
        projetos_ano=len(projetos_ano),
        projetos_total=projetos_total,
        projetos_nao_finalizados=projetos_nao_finalizados,
        projetos_recentes=projetos_recentes,
        projetos_andamento=projetos_andamento,
        now=agora
    )

@app.route('/orcamentos')
def orcamentos_redirect():
    # Redireciona para a lista de orçamentos
    return render_template(
        'lista_orcamentos.html',
        titulo='Orçamentos',
        orcamentos=orcamentos,
        clientes=clientes,
        estados=estados,
        cidades=cidades,
        anos=anos
    )

@app.route('/orcamentos/lista')
def lista_orcamentos():
    return render_template(
        'lista_orcamentos.html',
        titulo='Orçamentos',
        orcamentos=orcamentos,
        clientes=clientes,
        estados=estados,
        cidades=cidades,
        anos=anos
    )

@app.route('/insumos')
def insumos():
    return render_template('insumos.html', titulo='Insumos')

@app.route('/composicoes')
def composicoes():
    return render_template('composicoes.html', titulo='Composições')

@app.route('/planejamentos')
def planejamentos():
    return render_template('planejamentos.html', titulo='Planejamentos')

@app.route('/cadastros')
def cadastros():
    return render_template('cadastros.html', titulo='Cadastros')

@app.route('/administracao')
def administracao():
    return render_template('administracao.html', titulo='Administração')

if __name__ == '__main__':
    app.run(debug=True)
