#isso é uma variável
nome  =  "Camila"
#7 indices 
#variedade de dados menos digitação
#estrutura composta
#indices ==0 e o valores

# lista = [1,3.28,-6,5,5, "casa", 2.8, True]
# lista.append(2)
# print(lista)


#-------------------------
# lista2 = [25,3,566,545,5678, 25]
# lista2.remove(25)
# print(lista2)

# del lista2[0]
# print(lista2)

# lista4 =  len(lista2)
# print(lista4)

#-----------------------------------

# lista5 = [1,3,45,89,78,123,45,78,56]
# for i in lista5:
#   print(i)




# **Exercício 1:** Crie uma lista chamada `numeros` que contenha os números inteiros de 1 a 5 e imprima-a na tela.
#identação  =  organização do código 
print("exercicio 1")
numeros = [1,2,3,4,5]
for i in numeros: 
     print(i) 
  


# **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
print("exercicio 2")
print(numeros[2])







# **Exercício 3:** Adicione o número 6 à lista `numeros` e imprima a lista atualizada.
print("exercicio 3")
numeros.append(6)
print(numeros)



# **Exercício 4:** Remova o número 3 da lista `numeros` e imprima a lista resultante.
print("exercicio 4")
numeros.remove(3)
print(numeros)

# **Exercício 5:** Crie uma lista chamada `frutas` contendo três nomes de frutas diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.
print("exercicio 5")
frutas  = ["maçã", "banana", 'laranja']
print(frutas, numeros )



# **Exercício 6:** Use um loop `for` para percorrer e imprimir todos os elementos da lista `frutas`.
print("exercicio 6")
for i in frutas: 
   print(i)

# **Exercício 7:** Verifique se o número 5 está presente na lista `numeros` e imprima uma mensagem informando se ele está na lista ou não.


if  5 in numeros: 
    print('Esta aqui')
else: 
    print('Não tem')











