# -*- coding: utf-8 -*-
def jogo_premiado(a,b):
  if (a+b == 7 or a+b == 11):
    return 'Premiado!'
  return nova_jogada(a,b)

def nova_jogada(a,b):
  soma = a + b
  if (soma == 12):
    return 'Premiado!'
  return 'Tente novamente :('

import random
a = random.randint(1,11)
b = random.randint(1,11)
jogo_premiado(a,b)
