class Pessoa():
    def __init__(self, nome, idade,peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False
    def falar(self):
        print (f" {self.nome} comecou a falar ")
    def comer(self,comida):
        if self.comendo==true:
            print("nao pode comer, pois ja esta comendo")
     print (f" comecou a comer {comida}")
    def dormir (self):
        print (f" comecou a dormir ")