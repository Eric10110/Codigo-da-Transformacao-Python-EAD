class Carro:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def exibir_info(self):
            return f"Marca: {self.marca}, Modelo: {self.modelo}"
        
class CarroEletrico(Carro):
    def __init__( self, modelo, marca, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base}, Autonomia da Bateria: {self.autonomia_bateria} km"
    
meu_Carro = CarroEletrico("BYD","Dolphin",600) 
print(meu_Carro.exibir_info())