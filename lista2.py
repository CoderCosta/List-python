começar = input('para adicionar um item ou criar uma lista digite <s> se não digite <n>')

if começar == 'n':
    print('encerrar')

    exit
    
else:
    
    lista = []
    resposta = input('ensira a sua tarefa   ')
    lista.append(resposta)
    
    

while resposta :
     resposta = input('ensira a sua tarefa   ')
     lista.append(resposta)
     if resposta == 'n':
         print(lista)
         break
     else:
         continue
     
     # este codigo tem uma variavel que contem a lista e
     #identifica a resposta do usuario como item da lista 
     #alem de ter a funcao de parar o codigo ao ser enviado um 'n'
     
     
     #proximo passo
     #fazer com que a primeira letra de cada item da lista seja maiusculo
     #fazer com que o ultimo item da lista nao apareca ao 'printar' a lista
     
    

