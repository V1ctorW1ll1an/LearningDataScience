from collections import Counter
from typing import List


def mean(xs: List[float]) -> float:
    """
    Retorna a média aritmética de uma lista

    >>> mean([1, 2, 3])
    2.0
    """
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    """
    Se len(xs) for impar, a mediana sera o elemento do meio
    """

    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """
    Se len(xs) for par, ela sera a media dos dois elementos do meio
    """

    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # p. ex., comprimento 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: List[float]) -> float:
    """
    Encontra o valor do meio de v

    >>> median([1, 10, 2, 9, 5])
    5
    """

    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: List[float], p: float) -> float:
    """
    Retorna o valor pth-percentile em xs.

    Exemplos de teste:
    >>> quantile([1, 2, 3, 4, 5], 0.10) # 10th percentile
    1
    >>> quantile([1, 2, 3, 4, 5], 0.25) # 25th percentile
    2
    >>> quantile([1, 2, 3, 4, 5], 0.75) # 75th percentile
    4
    >>> quantile([1, 2, 3, 4, 5], 0.90) # 90th percentile
    5
    """

    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def mode(x: List[float]) -> List[float]:
    """
    Retorna uma lista, pois pode haver mais de uma moda

    >>> set(mode([1, 1, 1, 2, 3, 4]))
    {1}
    >>> set(mode([1,1,1,2,3,3,4,5,6,6,6]))
    {1, 6}
    """

    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


# Dispersão

"""
A dispersão expressa a media da distribuição dos dados. Aqui, em geral, os valores 
próximos de zero indicam que os dados nao estão espalhados e os valores maiores
(ou algo assim) indicam dados muito espalhados. Por exemplo, um medida simples
disso é a amplitude, a diferença entre o maior elemento e o menor:
"""


def data_range(xs: List[float]) -> float:
    """
    Amplitude

    >>> data_range([1, 2, 3, 4, 5, 6, 7, 8, 9])
    8
    """
    return max(xs) - min(xs)
