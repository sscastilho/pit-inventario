from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_secreta_projeto'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email == "admin@email.com" and senha == "1234":
            session['usuario_logado'] = email
            return redirect(url_for('dashboard'))
        else:
            erro = "Login ou senha incorretos!"
    return render_template('login.html', erro=erro)

@app.route('/dashboard')
def dashboard():
    if 'usuario_logado' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    itens = conn.execute('SELECT i.*, c.nome as nome_categoria FROM tb_item i JOIN tb_categoria c ON i.id_categoria = c.id_categoria').fetchall()
    conn.close()
    return render_template('dashboard.html', itens=itens)

@app.route('/novo_item', methods=('GET', 'POST'))
def novo_item():
    if 'usuario_logado' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        categoria_id = request.form['categoria']
        qtd = request.form['quantidade']
        conn.execute('INSERT INTO tb_item (nome, id_categoria, quantidade_atual) VALUES (?, ?, ?)', (nome, categoria_id, qtd))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    categorias = conn.execute('SELECT * FROM tb_categoria').fetchall()
    conn.close()
    return render_template('novo_item.html', categorias=categorias)

@app.route('/movimentacao/<int:id_item>', methods=('GET', 'POST'))
def movimentacao(id_item):
    if 'usuario_logado' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM tb_item WHERE id_item = ?', (id_item,)).fetchone()
    erro = None

    if request.method == 'POST':
        tipo = request.form['tipo']
        qtd = int(request.form['quantidade'])

        if tipo == 'Saída' and qtd > item['quantidade_atual']:
            erro = f"Erro: Estoque insuficiente! Você tem {item['quantidade_atual']} e tentou tirar {qtd}."
        else:
            nova_qtd = item['quantidade_atual'] + qtd if tipo == 'Entrada' else item['quantidade_atual'] - qtd
            conn.execute('UPDATE tb_item SET quantidade_atual = ? WHERE id_item = ?', (nova_qtd, id_item))
            conn.execute('INSERT INTO tb_movimentacao (data_hora, tipo, quantidade, id_item, id_usuario) VALUES (datetime("now"), ?, ?, ?, 1)', (tipo, qtd, id_item))
            conn.commit()
            conn.close()
            return redirect(url_for('dashboard'))
    conn.close()
    return render_template('movimentacao.html', item=item, erro=erro)

# --- ROTA DE EDITAR (NOVA) ---
@app.route('/editar/<int:id_item>', methods=('GET', 'POST'))
def editar_item(id_item):
    if 'usuario_logado' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM tb_item WHERE id_item = ?', (id_item,)).fetchone()

    if request.method == 'POST':
        nome = request.form['nome']
        categoria_id = request.form['categoria']
        # Nota: Não editamos a quantidade aqui para manter a integridade do histórico.
        # A quantidade só muda via "Movimentação".

        conn.execute('UPDATE tb_item SET nome = ?, id_categoria = ? WHERE id_item = ?', (nome, categoria_id, id_item))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))

    categorias = conn.execute('SELECT * FROM tb_categoria').fetchall()
    conn.close()
    return render_template('editar_item.html', item=item, categorias=categorias)

@app.route('/deletar/<int:id_item>')
def deletar(id_item):
    if 'usuario_logado' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    conn.execute('DELETE FROM tb_item WHERE id_item = ?', (id_item,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)