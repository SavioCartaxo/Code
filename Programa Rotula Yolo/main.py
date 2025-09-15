import cv2 as cv


# Função que vai responder aos eventos do mouse
def mouse_handler(event, x, y, flags, param):
    
    if event == cv.EVENT_LBUTTONDOWN:   # clique botão esquerdo
        print(f"Botão esquerdo pressionado em ({x}, {y})")
    elif event == cv.EVENT_MOUSEMOVE:   # movimento do mouse
        print(f"Mouse movendo em ({x}, {y})")
    elif event == cv.EVENT_LBUTTONUP:   # soltar botão esquerdo
        print(f"Botão esquerdo solto em ({x}, {y})")



# Cria uma janela
cv.namedWindow("MinhaJanela")

# Liga a função à janela
cv.setMouseCallback("MinhaJanela", mouse_handler)

# Exibe uma imagem em loop
imagem = cv.imread("/home/saviocartaxo/Downloads/batch_5/449804939_04899316011152_01052025_998469762260095_CUPOM_VINCULADO_.jpg")
while True:
    cv.imshow("MinhaJanela", imagem)
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()
