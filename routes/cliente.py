from flask import Blueprint
from flask import render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ Tela inicial que lista clientes"""
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente no banco de dados"""
    pass

@cliente_route.route('/new')
def form_cliente():
    """ Tela para criar novo cliente"""
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalhes do cliente """
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Formulario para editar o cliente """
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar informações do cliente """
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ Deletar informações do cliente """
    pass