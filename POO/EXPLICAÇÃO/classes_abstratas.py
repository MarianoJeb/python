from abc import abstractmethod, ABC



##CLASS ABSTRATAS NÃO PODEM SER INSTANCIADAS, SERVEM APENAS COMO MOLDE PARA SEREM USADAS E HEERDADAS!!!
class Vehicle(ABC):

    @abstractmethod
    def andar():
        pass


    abstractmethod
    def parar():
        pass

class Car(Vehicle):
    def andar():
        print('Você está dirigindo o carro!!')

    def parar():
        print('Você estacionou o carro!!')


