class Car:
    def __init__(self, color, brand, price, model, country, typeCar):
        self.color = color
        self.brand = brand
        self.price = price
        self.model = model
        self.country = country
        self.typeCar = typeCar

    def cadastro(self):
        print("Cor:", self.color)
        print("Marca:", self.brand)
        print("Preço:", self.price)
        print("Modelo:", self.model)
        print("País de fabricação:", self.country)
        print("Tipo do carro:", self.typeCar)

    def servico(self):
        print("\n\nNOSSOS SERVIÇOS")
        print("\n\033[92m>> Promoção! Qualquer serviço por R$ 80,00! <<\033[0m\033[96m")
        return "\n[ 1 ] - Encher Pneu \n[ 2 ] - Trocar Pneu \n[ 3 ] - Trocar Peças \n[ 4 ] - Consertos \n[ 5 ] - Reparos Gerais\n"

    def encherPneu(self):
        return "\nEnchendo o pneu... Finalizado!\n"

    def trocarPneu(self):
        return "\nTrocando o pneu... Finalizado!\n"

    def trocarPecas(self):
        return "\nFazendo a troca de peças... Finalizado!\n"

    def consertos(self):
        return "\nFazendo o concerto do carro... Finalizado!\n"

    def reparos(self):
        return "\nRealizando o reparo do carro... Finalizado!\n"

    def conserto(self):
        if (conserto == 1):
            return carro.encherPneu()
        elif (conserto == 2):
            return carro.trocarPneu()
        elif (conserto == 3):
            return carro.trocarPecas()
        elif (conserto == 4):
            return carro.consertos()
        elif (conserto == 5):
            return carro.reparos()
        else:
            return "\nOpção não identificada...  :( \n"

print(f'\033[1;95m{"-"*80}\n\n{"SEJAM BEM-VINDOS A OFICINA RUBY!!".center(80, " ")}\n\n{"-"*80}\033[0m')
print("\nREALIZE O CADASTRO DO SEU CARRO: \n")

cor = input("Cor: ")
marca = input("Marca: ")
preco = input("Preço: ")
modelo = input("Modelo: ")
pais = input("País de fabricação: ")
tipo = input("Tipo do seu carro: ")
carro = Car(cor, marca, preco, modelo, pais, tipo)

print(carro.servico())
conserto = int(input("\033[0mDIGITE O NÚMERO DO SERVIÇO: "))
print(carro.conserto())
print("\nVOLTE SEMPRE! :) ")
