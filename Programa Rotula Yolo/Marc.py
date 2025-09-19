
class Marc:
    def __init__(self, p1, p2, color):
        # img é uma imagem
        # p1 e p2 sao as coordenadas de 2 pontos opostos do marcador
        
        self.x1, self.y1 = p1
        self.x2, self.y2 = p2
        self.color = color

    def get_p1(self):
        return [self.x1, self.y1]
    
    def get_p2(self):
        return [self.x2, self.y2]
    
    def get_color(self):
        return self.color
    
    def set_p1(self, p1):
        self.x1, self.y1 = p1

    def set_p2(self, p2):
        self.x2, self.y2 = p2
        print(f'valores atualizados para {self.x2}, {self.y2}')