from cv2 import cv2
#import numpy as np


def bboxes(inp):
    video = inp
    result_video = video.copy()
    #video_final = inp

    #img2gray = cv2.cvtColor(inp, cv2.COLOR_BGR2GRAY)
    #ret, mask = cv2.threshold(img2gray,180, 255, cv2.THRESH_BINARY)
    #image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    # ret, new_img = cv2.threshold(video_final, 180, 255, cv2.THRESH_BINARY)  #para texto preto, cv.THRESH_BINARY_INV
    # para texto preto, cv.THRESH_BINARY_INV
    ret, new_img = cv2.threshold(video, 180, 255, cv2.THRESH_BINARY)
    # new_img = cv2.threshold(video_final, 180, 255, cv2.THRESH_BINARY)  #para texto preto, cv.THRESH_BINARY_INV
    newimg = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

    # remover ruído da imagem
    # para manipular a orientação da diluição, x grande significa dilatar mais horizontalmente, y significa dilatar mais verticalmente
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(newimg, kernel, iterations=3)  # dilatar
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # obter contornos

    for contour in contours:
        # obter contorno delimitador de retângulo
        [x, y, w, h] = cv2.boundingRect(contour)

        #[x, y, w, h] = 334, 0, 100, 20

        # remover pequenos falsos positivos que não são texto
        if w < 80 and h < 80:
            continue
        if h/w > 9.0 or w/h > 9.0:
            continue

        # retângulo ao redor do contorno da imagem original
        cv2.rectangle(video, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cropped = video[y: y + h, x: x + w]

    cropped = cv2.GaussianBlur(cropped, (23, 23), 30)
    result_video[y:y+cropped.shape[0], x:x+cropped.shape[1]] = cropped
    #result_video[y:y+h, x:x+w] = cropped


    cv2.imshow('Saida', result_video)
    out.write(result_video)


# localização do arquivo de origem
srcfile = 'videoentrada.mp4'
cap = cv2.VideoCapture(srcfile)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('saida.avi', fourcc, 30, (480, 360))

while(cap.isOpened()):
    ret, inp = cap.read()
    bboxes(inp)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
