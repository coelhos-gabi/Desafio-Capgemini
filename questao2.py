class Senha:
    def __init__(self, senha):
        self.senha = senha
        self.senha_sem_repeticao = list(sorted(set(self.senha)))
        self.caracteres = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '-']

    # Função para checagem tamanho >= 1
    def tamanho_maior_que_um(self):

        if len(self.senha) >= 1:
            return True
        else:
            return False

    # Função para checagem tamanho >= 6
    def tamanho_maior_que_seis(self):

        if len(self.senha) >= 6:
            return True
        else:
            return False
            
    def check_caracteres_senha(self):
        n = 4
        # Contém no mínimo 1 letra maiuscula
        for i in range(65,91):
            if chr(i) in self.senha_sem_repeticao:
                n -= 1
                break

        #Contém no minimo 1 letra em maiuscula
        for i in range(97, 123):
            if chr(i) in self.senha_sem_repeticao:
                n -= 1
                break
        
        # Contém numeros
        for i in range(48,58):
            if chr(i) in self.senha_sem_repeticao:
                n -= 1
                break     
        # Contem no minimo 1 caractere especial
        for elemento in self.caracteres:
            if elemento in self.senha_sem_repeticao:
                n -= 1
                break
        
        if n<0:
            n=0

        return n

def main():
    senha = input('Digite a senha: ').strip()
    verifica_senha = Senha(senha)
    if verifica_senha.tamanho_maior_que_um():
        if verifica_senha.tamanho_maior_que_seis():
            print(verifica_senha.check_caracteres_senha())
        else:
            print(6-len(senha))
    else:
        print(6-len(senha))


if __name__ == '__main__':
    main()
    