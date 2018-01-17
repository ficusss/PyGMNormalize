import numpy as np
from sys import stderr
from scipy.stats import rankdata
from utils import percentile

#===============================================================================

def total_count_normalization(matrix):
    """
    Total count normalization
    
    Parameters
    ----------
    matrix : array_like
        Matrix to normalize.
        
    Returns
    -------
    array_like
        Normalized matrix.
    """
    return matrix / matrix.sum(axis=0)

#===============================================================================

def percentile_normalization(matrix, p):
    """
    Percentile normalization
    
    Parameters
    ----------
    matrix : array_like
        Matrix to normalize.
    p : float in range of [0,100]
        Percentile to compute, which must be between 0 and 100 inclusive.
        
    Returns
    -------
    array_like
        Normalized matrix.
    """
    return matrix / percentile(matrix, p)

#===============================================================================

def quartile_normalization(matrix, q):
    """
    Quartile normalization
    
    Parameters
    ----------
    matrix : array_like
        Matrix to normalize.
    q : string from {"lower", "median", "upper"} or quartile number (1, 2 or 3)
        The names of quartiles to compute in accordance:
        "lower" = 1,
        "median" = 2,
        "upper" = 3.
        
    Returns
    -------
    array_like
        Normalized matrix.
    """
    d = {"upper": 75, "lower": 25, "median": 50, 3: 75, 1: 25, 2: 50}
    assert q in d, 'Unexpected quartile for normalization: "' + str(q) + '"'
    return percentile_normalization(matrix, d[q])

#===============================================================================

def tmm_normalization(matr, index_ref=None, trim_fold_change=0.3, trim_abs_expr=0.05):
    """
    Trimmed mean of M-values normalization
    
    Parameters
    ----------
    matrix : array_like
        Matrix to normalize.
    index_ref:
        Index of reference column.
    trim_fold_change:
        Percent of trimmed for folder change.
    trim_abs_expr:
        Percent of trimmed for absolute expression.
        
    Returns
    -------
    array_like
        Normalized matrix.
    """
    matrix = np.array(matr)                           # better speed of calculating
    np.seterr(divide='ignore', invalid='ignore')      # for divide on zeros in log2
    
    # Calculation log2(tmm_factor)
    def log2_tmm(index_vec):
        # select the necessary vectors
        curr_vec = matrix[:, index_vec]
        ref_vec = matrix[:, index_ref]
        
        # total number molecules in cells
        total_curr_vec = np.sum(curr_vec)
        total_ref_vec = np.sum(ref_vec)
        
        # select significant genes
        check_inf = (~np.isinf(matr_a[:, index_vec])) & (~np.isinf(matr_m[:, index_vec]))
        ranks = rankdata(matr_a[:, index_vec][check_inf], method='ordinal')
        bool_a = (ranks > len(ranks) * trim_abs_expr) & (ranks < len(ranks) * (1 - trim_abs_expr))
        ranks = rankdata(matr_m[:, index_vec][check_inf], method='ordinal')
        bool_m = (ranks > len(ranks) * trim_fold_change) & (ranks < len(ranks) * (1 - trim_fold_change))
        curr_vec = curr_vec[check_inf]
        ref_vec = ref_vec[check_inf]
        bool_curr_vec = curr_vec > 0
        bool_ref = ref_vec > 0
        bool_result = bool_curr_vec & bool_ref & bool_a & bool_m
        
        # ñalculation of required values
        w_vec = 1 / ((total_curr_vec - curr_vec[bool_result]) / (total_curr_vec * curr_vec[bool_result]) + 
                     (total_ref_vec - ref_vec[bool_result]) / (total_ref_vec * ref_vec[bool_result]))
        m_vec = np.log2(curr_vec[bool_result] / total_curr_vec) - np.log2(ref_vec[bool_result] / total_ref_vec)
        
        # calculation log2(tmm_factor)
        w_sum = np.sum(w_vec)
        if np.isclose(w_sum, 0) or np.isinf(w_sum):
            print("Unexpected sum of weights for vector {}: '{}'".format(index_vec, w_sum), file=stderr)
            return 0
        
        return np.sum(w_vec * m_vec) / w_sum
        
    # find index of reference column
    f75 = percentile(matrix, 75)
    if index_ref is None:
        index_ref = np.argmin(abs(f75 - np.mean(f75)))
    elif isinstance(numeric_matrix, pd.DataFrame) and isinstance(index_ref, int):
        index_ref = matr.columns.values[index_ref]    
    
    # find matrix A and M described expression levels of genes
    matr_norm = matrix / np.sum(matrix, axis=0)
    matr_a = np.log2(matr_norm * matr_norm[:, index_ref].reshape(matr_norm.shape[0], 1)) / 2
    matr_m = np.log2(matr_norm / matr_norm[:, index_ref].reshape(matr_norm.shape[0], 1))
    
    # calculation tmm_factor and normalization of input data
    tmm_factor = 2 ** np.array([log2_tmm(i) for i in range(matrix.shape[1])])
    return matr / tmm_factor

#===============================================================================
