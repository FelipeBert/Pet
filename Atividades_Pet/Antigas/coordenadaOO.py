import math

class Ponto():

    def __init__(self, xPassado, yPassado): #metodo que é primeiro iniciado em toda classe
        self.x = xPassado
        self.y = yPassado

    def distancia(self, pOutro): #sempre passar self como argumento
        dist = math.sqrt( (pOutro.x - self.x)**2 + (pOutro.y - self.y)**2 )
        return dist

class Circuferencia():

    def __init__(self, ponto, raio):
        self.centro = ponto
        self.r = raio
    
    def pertence(self, nPonto):
        if self.centro.distancia(nPonto) <= self.r: #self.centro seria o mesmo que p.
            return True
        else:
            return False

p = Ponto(1, 1)
p2 = Ponto(2, 2)
c = Circuferencia(p, 1)
retorno = c.pertence(p2)
print(retorno)