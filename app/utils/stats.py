

from scipy.stats import f_oneway, kruskal

def run_anova(*groups):
    """Perform one-way ANOVA test."""
    result = f_oneway(*groups)
    return result.statistic, result.pvalue

def run_kruskal(*groups):
    """Perform Kruskal-Wallis H-test."""
    result = kruskal(*groups)
    return result.statistic, result.pvalue
