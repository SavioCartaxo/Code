import os
import cv2 as cv

from Marc import Marc

class Image:
    def __init__(self, img_adress):
        if not os.path.isfile(img_adress):
            raise RuntimeError("Endereço de imagem inválido.")
        
        self.img = cv.imread(img_adress)
        self.marc_list = []

    def marc_add(self, p1, p2, color):
        # Adiciona um marcador na imagem
        marcador = Marc(p1, p2, color)
        self.marc_list.append(marcador)

    def marc_remove(self):
        try:
            return self.marc_list.pop(-1)
        except:
            pass

    def desenha_marcador_enquanto_move_mouse(self, p2):
        self.marc_list[-1].set_p2(p2)

    def to_designe(self):
        img_cp = self.img.copy()
        
        for marc in self.marc_list:
            cv.rectangle(img_cp, marc.get_p1(), marc.get_p2(), marc.get_color(), 3)
        return img_cp

    def get_img(self):
        return self.img