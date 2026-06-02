#Import do framework Flask
#Render_template para ler/renderizar o html
#Request para pegar os dados do formulário

from flask import Flask, render_template, request
#biblioteca para conectar ao banco de dados MySQL
import mysql.connector

#Cria conexão com o banco de dados
bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}

