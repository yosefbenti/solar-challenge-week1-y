# app/utils.py

from scipy.stats import f_oneway, kruskal

def run_anova(*groups):
    """
    Run one-way ANOVA test on multiple groups of data.
    
    Parameters:
    *groups: variable number of arrays/lists containing numerical data
    
    Returns:
    f_statistic: float
    p_value: float
    """
    result = f_oneway(*groups)
    return result.statistic, result.pvalue

def run_kruskal(*groups):
    """
    Run Kruskal-Wallis H-test (non-parametric ANOVA alternative).
    
    Parameters:
    *groups: variable number of arrays/lists containing numerical data
    
    Returns:
    h_statistic: float
    p_value: float
    """
    result = kruskal(*groups)
    return result.statistic, result.pvalue
