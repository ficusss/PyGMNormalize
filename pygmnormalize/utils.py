import numpy as np

def percentile(matrix, p, saving_memory=False):
    """
    Estimation of percentile for each column without zero-rows.
    
    Parameters
    ----------
    matrix : array_like
        Matrix to calculate percentile.
    p : float in range of [0,100]
        Percentile to compute, must be between 0 and 100 inclusive.
    saving_memory : bool
        Parameter for activation of RAM saving mode. This may take longer.
        
    Returns
    -------
    array_like
        Calculated percentile for each column.
    """
    if saving_memory:
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)
        mask = [np.any(r > 0) for r in matrix] 
        return np.array([np.percentile(c[mask], p) for c in matrix.T])
    
    return np.percentile(matrix[np.any(matrix > 0, axis=1)], p, axis=0)
