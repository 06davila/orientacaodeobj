class Pessoa():
    def __init__(self, nome, idade,peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False
    def dormir(self):
       if self.dormindo == True:
           print(f" {self.nome} ja estar dormindo")
       elif self.falando==True:
           print (f" {self.nome} nao pode falar pq ta dormindo")
       elif self.comendo==True:
           print (f" {self.nome} nao pode comer pq ta falando")
       else:
           print (f" foi dormir")
       elif self.dormindo==True:
      def self.
       elif self.comendo=False
   else:
          print  (f" ele ja estar acordado")

