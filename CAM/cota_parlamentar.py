#!/bin/python

import wget

AnoInicial = 2009
AnoAtual = datetime.date.year

PathArquivos = "../arquivos/CAM/"

wget.download("http://www.camara.gov.br/cotas/AnoAtual.zip",PathArquivos + "AnoAtual.zip")

for ano in range(AnoInicial, AnoAtual):
    url = "http://www.camara.gov.br/cotas/Ano-" + ano + ".xml.zip"
    wget.download(url,PathArquivos + "Ano-" + ano + ".xml.zip")
