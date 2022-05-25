import pytest


def imprimir_oi(nome):
    print(f'Oi, {nome}')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'

def subtrair(numero_a, numero_b):
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


if __name__ == '__main__':
    imprimir_oi('Luciana')

    # Chamar a definição somar e mostrar o resultado
    resultado = somar(7, -6)
    print(f'A soma: {resultado}')

    # Chamar a definição subtrair e mostrar o resultado
    resultado = subtrair(25, 8)
    print(f'A subtração: {resultado}')


def teste_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7

    # 2 - Exucuta
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

def teste_subtrair():
    # 1 - Prepara / Configura
    # 1.1 - Dados de Entrada / Valores do Teste
    numero_a = 15
    numero_b = 10

    # 1.2 - Resultados Esperados
    resultado_esperado = 5

    # 2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida / Checa
    assert resultado_obtido == resultado_esperado


def teste_multiplicar():
    # 1 - Configura
    numero_a = 3
    numero_b = 4

    # 1.2 - Resultados Esperados
    resultado_esperado = 12

    # 2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida / Checa
    assert resultado_obtido == resultado_esperado

def teste_dividir():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 3

    # 1.2 - Resultados Esperados
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

 TDD = Test Driven Development
#        Desenvolvimento Direcionado por Teste
#
# - Criar todos os testes de unidade no começo
# - Executar todos os testes pelo menos 1 vez por dia
#
# Imagine que você no 1º dia (nada pronto)
# Você executa todos os testes - o que acontece?
# Dia 01 - Falhou 100 - Passou 000
# Dia 02 - Falhou 095 - Passou 005
# Dia 03 - Falhou 090 - Passou 010
# Dia 04 - Falhou 088 - Passou 012
# Dia 05 - Falhou 081 - Passou 019
# Dia 06 - Falhou 075 - Passou 025
# Informação sobre o progresso
# Insistir mais um dia      1 + 1 = 2?
# Pedir ajuda               1 + 2 = 3
# Devolver e pegar outra    1 + 1 = 2!
# Tudo certo!               1 + 2 = 4
# TDD: Teste é uma medida de progresso

# CI: Continuous Integration
# IC: Integração Continua

# (Build) --> Suite de Testes ------> (Build)
#              Automatizada   Passou
# Ambiente                            Então, move >> Ambiente
# de Desenvolvimento                                 de Teste

# CD: Continuous Delivery
# EC: Entrega Continua

# (Build) --> Suite --> (Build) -----> (Build)
#   Dev      de Teste    Teste  Muitos Produção
#                               Testes
