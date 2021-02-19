# Teste de Visão Computacional da V-Lab
## Desafio proposto: 

- Identificar o nome de uma pessoa, e anonimizar. A técnica para anonimização fica por sua conta, podendo ser blur, black-box, ou qualquer outra. Pense em criar algo escalável que funcione com qualquer nome, e em qualquer frame/local do vídeo.
Registrar todo o texto contido, no vídeo, assim como o tempo que o mesmo se encontra será considerado um plus, porém não obrigatório.

## Tecnologias utilizadas e necessárias para rodar o código:

- Python
- OpenCV
- NunPy

## Videos:

- Para ver os videos de saída baixe-os acima no repositório.

Existem dois videos de saída, o saida_reconhecimento.avi que mostra as áreas que o computador reconheceu como texto nos frames, e o saida.avi que é o video final do projeto com a anonimização do nome.

## Pesquisa e método de resolução:

Para a conclusão do desafio foi necessário muita pesquisa, sites como o Stack Overflow, GitHub, Youtube e blogs foram essenciais. De inicio foi necessário procurar as melhores bibliotecas de OCR (Optical Character Recognition), me deparei com muitos textos sobre Tesseract, porém nos projetos observados desta biblioteca eram ultilizadas imagens para reconhecimento de texto e não videos. Continuando na busca de modos para solucionar o problema foi encontrado no GitHub um repositório de reconhecimento de texto em video, este código serviu de modelo e estudo para a criação do projeto.
Primeiramente foi aplicado alguns códigos da biblioteca NunPy para reconhecer os textos no video, logo foi criado um recorte (cropped) na área que estava o nome identificado e para anonimizar o nome ultilizou se GaussianBlur do OpenCV.
