# am_matrix_mult.py

"""
Implementação de multiplicação de matrizes, com explicabilidade
"""

# matriz 3x3
M1 = A = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# matriz 3x3
M2 = B = [
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r']
]


M1 = A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# matriz 3x3
M2 = B = [
    [10,11,12],
    [13,14,15],
    [16,17,18]
]


#-----------------------------------------------------------------------------------------------------------------------
def shape(
    p_M:list
):
    numero_de_linhas = len(p_M)

    linha_qualquer = primeira_linha = p_M[0]

    numero_de_colunas = len(
        linha_qualquer
    )

    return numero_de_linhas, numero_de_colunas # tuple (é uma forma de coleção)
# def shape

#-----------------------------------------------------------------------------------------------------------------------
"""
LA=0..#Linhas de A - 1
	CB=0..#Colunas de B - 1
		K=0..2 A[L,k] * B[k, C]
		
ordem de cálculo das células que compõem a matriz produto
(0,0) terá 3 produtos = A[0,0]*B[0,0] + A[0,1]*B[1,0] + A[0,2]*B[2,0]
(linha=0,col=1) terá 3 produtos = A[0,0]*B[0,1] + A[0,1]*B[1,1] + A[0,2]*B[2,1]
(0,2)
(1,0)
(1,1)
(1,2)
(2,0)
(2,1)
(2,2)
"""
def multiplicacao_de_matrizes(
    p_A, # matriz operando esquerdo
    p_B, # matriz operando direito
    p_b_fazer_contas:bool = False, # por defeito, o output é a explicação de como se fazem as contas; se se pretender as contas feitas, usar True
    # p_b_mostrar_endereco:bool = False
):
    nla, ncola = shape(p_A)
    nlb, ncolb = shape(p_B)

    # < <= > >= == !=
    b_posso_calcular:bool = ncola == nlb # True or False

    if (b_posso_calcular):
        # algoritmo de multiplicação de matrizes
        # um passeio entre os valores 0 e nla-1 (passear pelas linhas de A)
        matriz = ""
        for idx_linha in range(nla):

            linha = ""
            # um passeio entre os valores 0 e ncolb-1 (passear pelas colunas de B)
            for idx_coluna in range(ncolb):
                # computa o somatório que corresponde a cada célula da matriz produto
                # um passeio para computar a soma de fatores necessários, para obter as células da matriz produto
                celula_explicada:str = ""
                for k in range(ncola):
                    produto_apresentacional = f"{p_A[idx_linha][k]}*{p_B[k][idx_coluna]}"

                    # se for para fazer as contas, as contas substituem a explicação
                    if(p_b_fazer_contas):
                        try:
                            # contas todas feitas da célula
                            produto_apresentacional = str(eval(produto_apresentacional))
                        except Exception as e:
                            print(str(e))
                        # try-except
                     # if

                    b_ultimo_fator:bool = k==ncola-1
                    celula_explicada+=produto_apresentacional

                    if(not b_ultimo_fator):
                        celula_explicada+="  +  "
                    else: # sendo o último fator
                        if(p_b_fazer_contas):
                            celula_explicada=str(eval(celula_explicada))+"\t"

                        celula_explicada += "\t"
                    # if-else
                # for

                linha += celula_explicada

                b_ultima_coluna = idx_coluna==ncolb-1
                if(b_ultima_coluna):
                    linha+="\n"
                # if
            # for coluna
            matriz += linha
        # for linha
        return matriz
    # if
    else:
        return "Matrizes incompatíveis para multiplicação"
# multiplicacao_de_matrizes

#-----------------------------------------------------------------------------------------------------------------------
def dimensao_da_matriz(p):return shape(p)

print(A)

print("Dimensão/Shape da matriz: "+str(shape(A)))

print(B)

print("Dimensão/Shape da matriz: "+str(dimensao_da_matriz(B)))

# utilização de "named params"
explicacao_de_como_se_multiplicam_A_e_B = \
    multiplicacao_de_matrizes(
        p_A=A,
        p_B=B,
    )
print(
    explicacao_de_como_se_multiplicam_A_e_B
)

resultado = \
    multiplicacao_de_matrizes(
        p_A=A,
        p_B=B,
        p_b_fazer_contas=True,
    )

print(resultado)