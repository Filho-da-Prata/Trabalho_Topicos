import sqlite3
from tkinter import messagebox
"""
    CREATE TABLE "Usuarios" (
	"ID_usuario"	INTEGER NOT NULL UNIQUE,
	"NOME_usuario"	TEXT NOT NULL,
	"EMAIL_usuario"	TEXT NOT NULL,
	"SENHA_usuario"	TEXT NOT NULL,
	"TIPO_usuario"	TEXT NOT NULL,
	PRIMARY KEY("ID_usuario" AUTOINCREMENT)
    );
"""

def conectar():
    conn = sqlite3.connect("BD.db")
    cursor = conn.cursor()
    return conn,cursor

# inserindo dados na tabela
def Registrar_Usuario(login,email,senha,tipo):
    """
    LOGIN_usuario,EMAIL_usuario,SENHA_usuario,TIPO_usuario
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Usuarios (LOGIN_usuario,EMAIL_usuario,SENHA_usuario,TIPO_usuario)
        VALUES (?,?,?,?)
    """, (login,email,senha,tipo))
    #
    conn.commit()
    conn.close()

    #return id

def Registrar_Pessoa(nome,rua,num,bairro,cidade,tel,email,cpf,situacao):
    """
    NOME_pessoa,END_rua,END_num,END_bairro,END_cidade,TELEFONE_pessoa,EMAIL_pessoa,CPF_pessoa,SITUACAO_CAD_pessoa
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Cad_Pessoa (NOME_pessoa,END_rua,END_num,END_bairro,END_cidade,TELEFONE_pessoa,EMAIL_pessoa,CPF_pessoa,SITUACAO_CAD_pessoa)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (nome,rua,num,bairro,cidade,tel,email,cpf,situacao))
    
    conn.commit()
    conn.close()

def Registrar_Pet(nome,raca,genero,idade,status,foto=''):
    """
    NOME_pet,RACA_pet,GENERO_pet,IDADE_pet,STATUS_pet,FOTO_pet
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Pet (NOME_pet,RACA_pet,GENERO_pet,IDADE_pet,STATUS_pet,FOTO_pet)
        VALUES (?,?,?,?,?,?)
    """, (nome,raca,genero,idade,status,foto))
    
    conn.commit()
    conn.close()

def Registrar_Lar_Temp(status,capacidade,utilizacao,endereco,cod_pessoa):
    """
    STATUS_lar,CAPACIDADE_lar,UTILIZACAO_lar,ENDERECO_lar,fk_Cad_pessoa_COD_pessoa
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Lar_temporario (STATUS_lar,CAPACIDADE_lar,UTILIZACAO_lar,ENDERECO_lar,fk_Cad_pessoa_COD_pessoa)
        VALUES (?,?,?,?,?)
    """, (status,capacidade,utilizacao,endereco,cod_pessoa))
    
    conn.commit()
    conn.close()

def Registrar_Clinica(nome,cnpj,tel,endereco):
    """
    NOME_clini,CNPJ_clini,TELEFONE_clini,END_clini
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Clinica_vet (NOME_clini,CNPJ_clini,TELEFONE_clini,END_clini)
        VALUES (?,?,?,?)
    """, (nome,cnpj,tel,endereco))
    
    conn.commit()
    conn.close()
    
def Registrar_Adocao(data,cod_pet,cod_pessoa):
    """
    DATA_adocao,FK_Pet_COD_pet,FK_Cad_pessoa_COD_pessoa
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO ADOTA_ADOCAO (DATA_adocao,FK_Pet_COD_pet,FK_Cad_pessoa_COD_pessoa)
        VALUES (?,?,?)
    """, (data,cod_pet,cod_pessoa))
    
    conn.commit()
    conn.close()

def Registrar_Hospedagem(periodo,cod_pet,cod_lar):
    """
    PERIODO_hosp,fk_Pet_COD_pet,fk_Lar_temporario_COD_larTemporario
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Hospedagem_CONTEM (PERIODO_hosp,fk_Pet_COD_pet,fk_Lar_temporario_COD_larTemporario)
        VALUES (?,?,?,?,?,?,?)
    """, (periodo,cod_pet,cod_lar))
    
    conn.commit()
    conn.close()

def Registrar_Atendimento(historico,valor,cod_clini,cod_pet):
    """
    HISTORICO_proced, VALOR_proced, fk_Clinica_vet_COD_clini, fk_Pet_COD_pet
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO Procedimento_ATENDER (HISTORICO_proced, VALOR_proced, fk_Clinica_vet_COD_clini, fk_Pet_COD_pet)
        VALUES (?,?,?,?)
    """, (historico,valor,cod_clini,cod_pet))
    
    conn.commit()
    conn.close()

def Verificar_Login(email,senha):
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Usuarios 
            WHERE (EMAIL_usuario = ? AND SENHA_usuario = ?)
        """,(email, senha))
    VerificaLogin = cursor.fetchone()
    conn.close()
    
    return VerificaLogin
    
    '''
    try: 
        if login in VerificaLogin and senha in VerificaLogin:
            messagebox.showinfo(title="Login Info", message="Seja Bem Vindo!")
    except:
        messagebox.showerror(title="Login Info",message="Este usuário não está cadastrado!")
    '''

def Verificar_Admin(login,senha):
    conn,cursor = conectar()
    cursor.execute(""" 
            SELECT * FROM Usuarios 
            WHERE (LOGIN_usuario = ? AND SENHA_usuario = ? AND TIPO_usuario = 'Administrador')
        """,(login,senha))
    VerificaAdmin = cursor.fetchone()
    conn.close()
    
    return VerificaAdmin