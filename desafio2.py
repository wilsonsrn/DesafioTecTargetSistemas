# DESAFIO TÉCNICO 2
"""2) Escreva um programa que verifique, em uma string, a existência da letra 'a',
 seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

 """
import unicodedata

def count_letter_a(s):
  text = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("utf-8")
  return text.lower().count('a')

s = input("Digite uma string para verificar a existência da letra 'a': ")

if count_letter_a(s) == 0:
  print("Não existem letras 'a' na string.")

if count_letter_a(s) > 0:
  print(f"A string '{s}' existem {count_letter_a(s)} letras 'a'.")