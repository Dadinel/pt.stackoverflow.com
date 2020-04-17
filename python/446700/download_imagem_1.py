import requests

with open('pato.jpg', 'wb') as imagem:
  resposta = requests.get("http://t1.gstatic.com/images?q=tbn:ANd9GcRBL_Z4t3zlPVfo4WLFmVy9CE2zBLph8hmwoexfOQn1kQOHoTDAu9dLCsI4", stream=True)

  if not resposta.ok:
    print("Ocorreu um erro, status:" , resposta.status_code)
  else:
    for dado in resposta.iter_content(1024):
      if not dado:
          break

      imagem.write(dado)

    print("Imagem salva! =)")
