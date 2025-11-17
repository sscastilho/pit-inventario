from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_secreta_projeto'  # Necessário para usar sessões (login)

# --- Conexão com Banco de Dados ---
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # Permite acessar colunas pelo nome
    return conn

# --- Rotas (O Caminho do Usuário) ---

# 1. Rota Inicial: Tela de Login
@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Verificação simples (Para teste rápido)
        # No mundo real, verificaríamos no banco de dados tb_usuario
        if email == "admin@email.com" and senha == "1234":
            session['usuario_logado'] = email
            return redirect(url_for('dashboard'))
        else:
            erro = "Login ou senha incorretos!"

    return render_template('login.html', erro=erro)

# 2. Rota do Dashboard: Lista os Itens
@app.route('/dashboard')
def dashboard():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    # Busca os itens e junta com o nome da categoria
    itens = conn.execute('SELECT i.*, c.nome as nome_categoria FROM tb_item i JOIN tb_categoria c ON i.id_categoria = c.id_categoria').fetchall()
    conn.close()
    return render_template('dashboard.html', itens=itens)

# 3. Rota para Adicionar Novo Item
@app.route('/novo_item', methods=('GET', 'POST'))
def novo_item():
    if 'usuario_logado' not in session: return redirect(url_for('login'))

    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        categoria_id = request.form['categoria']
        qtd = request.form['quantidade']

        conn.execute('INSERT INTO tb_item (nome, id_categoria, quantidade_atual) VALUES (?, ?, ?)',
                     (nome, categoria_id, qtd))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))

    categorias = conn.execute('SELECT * FROM tb_categoria').fetchall()
    conn.close()
    return render_template('novo_item.html', categorias=categorias)

# 4. Rota para Movimentar Estoque (Entrada/Saída)
@app.route('/movimentacao/<int:id_item>', methods=('GET', 'POST'))
def movimentacao(id_item):
    if 'usuario_logado' not in session: return redirect(url_for('login'))

    conn = get_db_connection()
    item = conn.execute('SELECT * FROM tb_item WHERE id_item = ?', (id_item,)).fetchone()

    if request.method == 'POST':
        tipo = request.form['tipo'] # 'Entrada' ou 'Saída'
        qtd = int(request.form['quantidade'])

        # Atualiza a quantidade no item
        nova_qtd = item['quantidade_atual'] + qtd if tipo == 'Entrada' else item['quantidade_atual'] - qtd

        conn.execute('UPDATE tb_item SET quantidade_atual = ? WHERE id_item = ?', (nova_qtd, id_item))

        # Registra no histórico (tb_movimentacao)
        # Obs: Usando ID de usuário 1 fixo para simplificar o exemplo
        conn.execute('INSERT INTO tb_movimentacao (data_hora, tipo, quantidade, id_item, id_usuario) VALUES (datetime("now"), ?, ?, ?, 1)',
                     (tipo, qtd, id_item))

        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))

    conn.close()
    return render_template('movimentacao.html', item=item)

# 5. Rota de Logout
@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
