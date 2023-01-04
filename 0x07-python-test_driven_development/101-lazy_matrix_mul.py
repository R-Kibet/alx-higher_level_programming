#!/usr/bin/python3
""" Funct multiplies 2 matrix """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Funct  multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        multiplication
    """

    return (np.matmul(m_a, m_b))
