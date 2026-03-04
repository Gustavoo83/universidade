from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)
from PySide6.QtCore import Qt

from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("Sistema Universidade - Dashboard")
        self.janela.resize(500, 350)
        self.janela.setLayout(self.layout)

        self.criar_componentes()
        self.aplicar_estilo()

        self.janela.show()

    def criar_componentes(self):

        # 🔹 TÍTULO
        titulo = QLabel("Sistema Universitário")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setObjectName("titulo")

        subtitulo = QLabel("Painel Administrativo")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setObjectName("subtitulo")

        self.layout.addWidget(titulo)
        self.layout.addWidget(subtitulo)

        # Espaço flexível superior (centralização vertical)
        self.layout.addStretch()

        # 🔹 BOTÃO LISTAR
        botao_listar = QPushButton("Listar Alunos")
        botao_listar.setFixedSize(450, 45)
        botao_listar.clicked.connect(self.abrir_listagem)
        self.layout.addWidget(botao_listar, alignment=Qt.AlignCenter)

        # 🔹 BOTÃO CADASTRAR
        botao_cadastrar = QPushButton("Cadastrar Aluno")
        botao_cadastrar.setFixedSize(450, 45)
        botao_cadastrar.clicked.connect(self.abrir_cadastro)
        self.layout.addWidget(botao_cadastrar, alignment=Qt.AlignCenter)

        # Espaço flexível inferior (centralização vertical)
        self.layout.addStretch()

    def aplicar_estilo(self):
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                color: #1F2937;
                font-size: 14px;
            }

            QLabel#titulo {
                font-size: 26px;
                font-weight: bold;
                color: #0B5ED7;
                margin-bottom: 5px;
            }

            QLabel#subtitulo {
                font-size: 14px;
                color: #6B7280;
                margin-bottom: 15px;
            }

            QPushButton {
                background-color: #FFFFFF;
                color: #1E90FF;
                border: 2px solid #1E90FF;
                border-radius: 12px;
                font-weight: bold;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #1E90FF;
                color: white;
            }

            QPushButton:pressed {
                background-color: #187BDC;
                border: 2px solid #187BDC;
                color: white;
            }
        """)

    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)
        self.tela_listagem.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app)
        self.tela_cadastro.janela.show()


if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())