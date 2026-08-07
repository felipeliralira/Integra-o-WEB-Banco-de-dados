from flask import Flask, render_template, redirect, url_for,request
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
bd_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1',
    'ssl_disabled': True
}

@app.route('/')
def indexRota():
    try:
        conexaoIndex = mysql.connector.connect(**bd_config)
        curso_index = conexaoIndex.cursor(dictionary=True)

        curso_index.execute("SELECT * FROM tb_cliente")
        #Variável que armazena os dados
        lista_clientes = curso_index.fetchall()

        curso_index.close()
        conexaoIndex.close()

        return render_template('index.html', clientes=lista_clientes)


    except mysql.connector.Error as err:
        return f"Erro ao carregar a lista: {err}"

@app.route('/cadastrar', methods=['POST'])
def criarCadastro():
    try:
        # Recebe os dados do formulário
        cpf = request.form['cpf']
        primeiro_nome = request.form['primeiro_nome']
        sobrenome = request.form['sobrenome']
        idade = request.form['idade']

        # Conecta ao banco de dados
        conexao = mysql.connector.connect(**bd_config)
        curso = conexao.cursor()

        # Instrução SQL
        query = "INSERT INTO tb_cliente (CPF, PRIMEIRO_NOME, SOBRENOME, IDADE) VALUES (%s, %s, %s, %s)"

        # Executa a inserção dos dados
        curso.execute(query, (cpf, primeiro_nome, sobrenome, idade))

        # CORREÇÃO AQUI: O commit deve ser feito na CONEXÃO, não no curso
        conexao.commit()  

        # Fecha o cursor e a conexão
        curso.close()
        conexao.close()

        return f"<h3> Cliente {primeiro_nome} gravado com sucesso!</h3><a href='/'> Voltar</a>"
        
    except mysql.connector.Error as err:
        return f"Erro ao conectar ao banco de dados: {err}"
    
@app.route('/excluir/<cpf>')
def excluir(cpf):
    try:
        conexao = mysql.connector.connect(**bd_config)
        curso = conexao.cursor()

        curso.execute("DELETE FROM tb_cliente WHERE CPF = %s", (cpf))
        conexao.commit()
        curso.close()
        conexao.close()

        return redirect(url_for('index'))
    except mysql.connector.Error as err:
        return f"Erro ao carregar a lista: {err}"

if __name__ == '__main__':
    app.run(debug=True)