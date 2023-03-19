class Inimigo():
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vivo = True
        self.vida_max = vida
        self.vida = vida
        self.dano = dano
    
    
    # GETS
    def get_stats(self):
        return [self.nome, self.vivo, self.vida_max, self.vida, self.dano]

    def get_nome(self):
        return self.nome

    def get_vivo(self):
        return self.vivo

    def get_vida_max(self):
        return self.vida_max
        
    def get_vida(self):
        return self.vida
    
    def get_dano(self):
        return self.dano
    

    # SETS
    def set_vida_max(self, nova_vida_max):
        self.vida_max = nova_vida_max
    
    def set_vida(self, nova_vida):
        self.vida = nova_vida
        if self.vida <= 0:
            self.vivo = False
        return self.vivo

    def set_dano(self, novo_dano):
        self.dano = novo_dano