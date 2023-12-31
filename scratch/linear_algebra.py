import math
from typing import Callable, List, Tuple

Vector = List[float]
Matrix = List[List[float]]


def add(v: Vector, w: Vector) -> Vector:
    """Soma os elementos correspondente"""
    assert len(v) == len(w), 'vetores devem ter o mesmo tamanho'
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """
    Subtrai dois vetores

    Exemplo:
    >>> subtract([4, 5, 6], [1, 2, 3])
    [3, 3, 3]
    """
    assert len(v) == len(w), 'vetores dem ter o mesmo tamanho'
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([4, 5, 6], [1, 2, 3]) == [3, 3, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """
    Soma todos os vetores correspondentes

    >>> vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]])
    [16, 20]
    """
    assert vectors, 'no vectors provided!'

    # verifique se os vetores sao do mesmo tamanho
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), 'tamanhos diferentes!'

    # o elemento de n˚ i do resultado é a soma de todo vetor[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """
    Multiplica cada elemento por c

    >>> scalar_multiply(2, [1, 2, 3])
    [2, 4, 6]
    """
    return [v_i * c for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """
    Computa a média dos elementos

    >>> vector_mean([[1, 2], [3, 4], [5, 6]])
    [3.0, 4.0]
    """
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    """
    Computa v_1 * w_1 + ... + v_n * w_n

    1 * 4 + 2 * 5 + 3 * 6
    >>> dot([1, 2, 3], [4, 5, 6])
    32
    """
    assert len(v) == len(w), 'os vetores devem ter o mesmo tamanho'

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """
    Retorna v_1 * v_1 + ... + v_n * v_n

    1 * 1 + 2 * 2 + 3 * 3
    >>> sum_of_squares([1, 2, 3])
    14
    """
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """
    Retorna a magnitude (ou comprimento) do vetor v

    >>> magnitude([3, 4])
    5.0
    """
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))


# Matrix


def shape(A: Matrix) -> Tuple[int, int]:
    """
    Retorna (n˚ de linhas de Am n˚ de colunas de A)

    >>> shape([[1, 2, 3], [4, 5, 6]])
    (2, 3)
    """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # numero de elementos da primeira linha
    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """
    Retorna a linha i de A (como um vetor)
    """
    return A[i]  # A[i] já está na linha i


def get_col(A: Matrix, j: int) -> Vector:
    """
    Retorna a coluna j de A (como um vetor)
    """
    return [
        A_i[j] for A_i in A  # elemento j da linha A_i
    ]     # para cada linha A_i


def make_matrix(
    num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]
) -> Matrix:
    """
    Retorna uma matriz num_rows x num_cols
    cuja entrada (i,j) é entry_fn(i,j)
    """

    return [
        [
            entry_fn(i, j) for j in range(num_cols)  # com i, crie uma lista
        ]  # [entry_fn(i,0), ...]
        for i in range(num_rows)
    ]         # crie uma lista para cada i


def identity_matrix(n: int) -> Matrix:
    """
    Retorna uma matriz identidade n x n

    >>> identity_matrix(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
