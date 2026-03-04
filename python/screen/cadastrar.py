from modules.mysql import MySQL
from modules.aluno import Aluno
 
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)
from PySide6.QtCore import Qt
 
 
class Cadastrar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()
 
        self.campos = {}
 
        self.configurar_janela()
        self.criar_componentes()
        self.aplicar_estilo()
 
    def configurar_janela(self):
        self.janela.setWindowTitle("Sistema Acadêmico - Cadastro de Aluno")
 
        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.4)
        altura = int(screen.height() * 0.65)
 
        self.janela.resize(largura, altura)
        self.janela.setMinimumSize(420, 550)
        self.janela.setLayout(self.layout)
 
    def criar_componentes(self):
 
        # 🔹 TÍTULO PRINCIPAL
        titulo = QLabel("Cadastro de Aluno")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setObjectName("titulo")
        self.layout.addWidget(titulo)
 
        componentes = {
            "nome": "Nome completo:",
            "email": "Email:",
            "cpf": "CPF:",
            "telefone": "Telefone:",
            "endereco": "Endereço:"
        }
 
        for chave, valor in componentes.items():
            label = QLabel(valor)
            campo = QLineEdit()
 
            self.layout.addWidget(label)
            self.layout.addWidget(campo)
 
            self.campos[chave] = campo
 
        botao_cadastro = QPushButton("Cadastrar Aluno")
        self.layout.addWidget(botao_cadastro)
 
        botao_cadastro.clicked.connect(self.cadastrar)
 
    def aplicar_estilo(self):
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #0A192F;
                color: #CCD6F6;
                font-size: 14px;
            }
 
            QLabel {
                color: #8892B0;
                margin-top: 8px;
            }
 
            QLabel#titulo {
                color: #4DA6FF;
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 15px;
            }
 
            QLineEdit {
                background-color: #112240;
                border: 1px solid #233554;
                border-radius: 6px;
                padding: 8px;
                color: #CCD6F6;
            }
 
            QLineEdit:focus {
                border: 1px solid #4DA6FF;
            }
 
            QPushButton {
                background-color: #1E90FF;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
                margin-top: 18px;
            }
 
            QPushButton:hover {
                background-color: #187BDC;
            }
 
            QPushButton:pressed {
                background-color: #0F5FBF;
            }
        """)
 
    def validar_campos(self):
        dados = {chave: campo.text().strip() for chave, campo in self.campos.items()}
 
        for chave, valor in dados.items():
            if not valor:
                return False, f"O campo '{chave}' não pode estar vazio."
 
        if not dados["cpf"].isdigit() or len(dados["cpf"]) != 11:
            return False, "CPF deve conter exatamente 11 números."
 
        return True, dados
 
    def cadastrar(self):
 
        valido, resultado = self.validar_campos()
 
        if not valido:
            QMessageBox.warning(
                self.janela,
                "Validação",
                resultado
            )
            return
 
        aluno = Aluno(
            resultado["nome"],
            resultado["email"],
            resultado["cpf"],
            resultado["telefone"],
            resultado["endereco"],
        )
 
        try:
            self.banco.connect()
            aluno.cadastrar(self.banco)
 
            QMessageBox.information(
                self.janela,
                "Sucesso",
                "Aluno cadastrado com sucesso!"
            )
            self.limpar_campos()
 
        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao cadastrar: {e}"
            )
 
        finally:
            self.banco.disconnect()
 
    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()