################################################################################
# Funções para imagens
################################################################################

from PIL import Image


def converte_imagem_pb_em_vetor_binario():
    imagem_pb_binaria = []

    imagem = Image.open(r"/images/smile.jpg")
    imagem = imagem.convert("1")
    for y in range(imagem.size[1]):
        for x in range(imagem.size[0]):

            this_pix = imagem.getpixel((x, y))
            if (this_pix > 0):
                imagem_pb_binaria.append(1)
            else:
                imagem_pb_binaria.append(0)
    return imagem_pb_binaria


def converte_vetor_binario_em_imagem_pb(imagem_pb):
    imagem_antiga = Image.open(r"/images/smile.jpg")

    imagem_nova = Image.new('1', imagem_antiga.size)

    pix_num = 0
    for y in range(imagem_nova.size[1]):
        for x in range(imagem_nova.size[0]):
            this_pix = imagem_pb[pix_num]
            if this_pix == 1:
                imagem_nova.putpixel((x, y), 1)
            elif this_pix == 0:
                imagem_nova.putpixel((x, y), 0)

            pix_num += 1

    imagem_nova.save("nova_imagem.jpeg")