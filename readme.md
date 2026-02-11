# Projeto Universidade

Modelagem em Orientação à objetos das Entidades Alunos, Cursos e Turmas.

## Caso de Uso
```mermaid
flowchart LR
    Usuario([Secretaria])

    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Aluno))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de Classes
```mermaid

classDiagram
    class Aluno{
        - Nome
        - Email
        - CPF
        - Telefone
        - Endereço
        - Matrícula
        + cadastrar()
        + editar()
        + transferir()
    }
```
## Dependencias
- **VSCODE**: IDE(Interface de Desenvolvivemento)

- **Mermaid**: Linguagem para confecção de Diagramas em documntos MD (Mark Down)

- **Matherial Icon Theme**: Tema para as Colorir as pastas.

-  **Git Lens**: Interface gráfica para o versionamento .git integrada ao VSCode.

