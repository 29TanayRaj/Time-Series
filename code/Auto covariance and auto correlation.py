import numpy as np

def auto_covariance(series, t, s):
    '''
    Compute the auto-covariance of a time series.

    Parameters:
    series: List or numpy array representing the time series.
    t: Index for the first time stamp.
    s: Index for the second time stamp.

    Returns:
    Auto-covariance value.
    '''
    lag = abs(t - s)
    series_t = np.array(series[:len(series) - lag])
    series_s = np.array(series[lag:])

    n = len(series_t)

    mu_1 = np.mean(series_t)
    mu_2 = np.mean(series_s)

    result = np.sum((series_t - mu_1) * (series_s - mu_2)) / n

    return result


def auto_correlation(series, t, s):
    '''
    Compute the auto-correlation of a time series.

    Parameters:
    series: List or numpy array representing the time series.
    t: Index for the first time stamp.
    s: Index for the second time stamp.

    Returns:
    Auto-correlation value.
    '''
    lag = abs(t - s)
    series_t = np.array(series[:len(series) - lag])
    series_s = np.array(series[lag:])

    n = len(series_t)

    mu_1 = np.mean(series_t)
    mu_2 = np.mean(series_s)

    sigma_1 = np.std(series_t)
    sigma_2 = np.std(series_s)

    result = np.sum((series_t - mu_1) * (series_s - mu_2)) / n
    result = result / (sigma_1 * sigma_2)

    return result