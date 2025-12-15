from scipy.stats import ttest_ind, pearsonr

def compare_smile_strength(smile1, smile2):
    skew1 = smile1[0] - smile1[-1]
    skew2 = smile2[0] - smile2[-1]
    return ttest_ind([skew1], [skew2])

def leverage_effect(price_series, vol_series):
    return pearsonr(price_series, vol_series)