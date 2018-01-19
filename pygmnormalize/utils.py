import numpy as np

def percentile(matrix, p):
    """
    Estimation of percentile without zeros
    
    Parameters
    ----------
    matrix : array_like
        Matrix to calculate percentile.
    p : float in range of [0,100]
        Percentile to compute, must be between 0 and 100 inclusive.
        
    Returns
    -------
    float
        Ñalculated percentile.
    """
    return np.percentile(matrix[np.any(matrix > 0, axis=1)], p, axis=0)