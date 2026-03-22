from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from database import conn, cursor, criar_tabelas
import config

criar_tabelas()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bem-vindo ao Bot de Prestadores!\n\n"
        "Digite o serviço que você precisa.\n"
        "Ex: eletricista, pedreiro, diarista, programador\n\n"
        "Se você é prestador digite /cadastrar"
    )

async def cadastrar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Envie os dados assim:\n"
        "Nome, Telefone, Cidade, Serviço, Descrição"
    )

async def mensagens(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    # CADASTRO
    if "," in texto:
        dados = texto.split(",")

        if len(dados) >= 5:
            nome = dados[0].strip()
            telefone = dados[1].strip()
            cidade = dados[2].strip()
            categoria = dados[3].strip()
            descricao = dados[4].strip()

            cursor.execute(
                "INSERT INTO prestadores (nome, telefone, cidade, categoria, descricao, plano) VALUES (?, ?, ?, ?, ?, ?)",
                (nome, telefone, cidade, categoria, descricao, "gratis")
            )
            conn.commit()

            await update.message.reply_text("Cadastro realizado com sucesso!")
            return

    # PESQUISA
    busca = texto.lower()
    cursor.execute(
        "SELECT nome, telefone, cidade, descricao FROM prestadores WHERE categoria LIKE ?",
        ('%'+busca+'%',)
    )
    resultados = cursor.fetchall()

    if resultados:
app.run_polling()
