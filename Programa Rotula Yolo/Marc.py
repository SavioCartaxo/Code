class Marc:
    def __init__(self, p1, p2, color):
        # img é uma imagem
        # p1 e p2 sao as coordenadas de 2 pontos opostos do marcador
        
        self.x1, self.y1 = p1
        self.x3, self.y3 = p1[0], p2[1]
        self.x4, self.y4 = p2[0], p1[1]
        self.x2, self.y2 = p2
        self.color = color

    def get_p1(self):
        return [self.x1, self.y1]
    
    def get_p2(self):
        return [self.x2, self.y2]
    
    def get_color(self):
        return self.color

    def set_p2(self, p2):
        self.x2, self.y2 = p2

    def clicou_na_vertice_de_um_marcador(self, ponto_que_clicou, margem):
        x = ponto_que_clicou[0]
        y = ponto_que_clicou[1]

        # Checage, de cada um dos 4 pontos
        if (self.x1 - margem < x < self.x1 + margem 
            and 
            self.y1 - margem < y < self.y1 + margem):
            return True
        
        if (self.x2 - margem < x < self.x2 + margem 
            and 
            self.y2 - margem < y < self.y2 + margem):
            return True
        
        if (self.x3 - margem < x < self.x3 + margem 
            and 
            self.y3 - margem < y < self.y3 + margem):
            return True
        
        if (self.x4 - margem < x < self.x4 + margem 
            and 
            self.y4 - margem < y < self.y4 + margem):
            return True
        
        return False
        


    def clicou_na_borda_do_marcador(self, ponto_que_clicou, margem):
        # ponto_que_clicou = [x, y] uma lista de coordenadas
        # margem = uma margem de pixels. posso clicar até X de distância(ex pixels) que o programa vai reconhecer como true

        x = ponto_que_clicou[0]
        y = ponto_que_clicou[1]

        # Se clicou no X que tem borda
        clicou_no_eixo_X = (
            # Aresta horizontal formada por p1 e p3
            (self.x1 - margem <= x <= self.x3 + margem
             or 
             self.x3 - margem <= x <= self.x1 + margem
            )

             or 

            # Aresta horizontal formada por p2 e p4
            (self.x4 - margem <= x <= self.x2 + margem
             or
             self.x2 - margem <= x <= self.x4 + margem
            )
        )


        clicou_no_eixo_Y = (
            (
            self.y1 - margem <= y <= self.y4 + margem
            or
            self.y4 - margem <= y <= self.y1 + margem
            )
            
            or
            
            (
            self.y2 - margem <= y <= self.y3 + margem
            or
            self.y3 - margem <= y <= self.y2 + margem
            )
        )

        return (clicou_no_eixo_X and clicou_no_eixo_Y)