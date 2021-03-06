from flask import Flask, request
from models.processo import Process
from models.regiao import Regiao
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return 'Running!'


# PROCESSOS
p = Process()


@app.route('/processos', methods=['POST'])
def new_process():
    return str(p.new_process(request))


@app.route('/processos/pedido', methods=['POST'])
def new_order():
    return str(p.new_order(request))


@app.route('/processos/pedido/<order_id>', methods=["POST"])
def update_order(order_id):
    return str(p.update_order(request, order_id))


@app.route('/processos/pedidos/tipos')
def get_order_types():
    return p.json(p.get_order_types())


@app.route('/processos/<num_processo>')
def get_process(num_processo):
    return p.json(p.get_process(num_processo))


@app.route('/processos/pagina/<int:num>')
def get_processes_by_page(num):
    return p.get_processes(num)


# REGIÕES
r = Regiao()


@app.route('/regioes/estados/siglas')
def estados_siglas():
    return r.get_estados_siglas()


@app.route('/regioes/municipios/<uf>')
def municipios_by_uf(uf):
    return r.get_municipios_by_uf(uf)


if __name__ == "__main__":
    app.run()
