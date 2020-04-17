import urllib.request
import sys

try:
  urllib.request.urlretrieve("http://t1.gstatic.com/images?q=tbn:ANd9GcRBL_Z4t3zlPVfo4WLFmVy9CE2zBLph8hmwoexfOQn1kQOHoTDAu9dLCsI4", "pato.jpg")
  print("Imagem salva! =)")
except:
  erro = sys.exc_info()
  print("Ocorreu um erro:", erro)
