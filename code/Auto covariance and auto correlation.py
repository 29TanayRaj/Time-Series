import numpy as np

def auto_covariance(series, lag):
    '''
    Compute the auto-covariance of a time series.

    Parameters:
    series: List or numpy array representing the time series.
    lag: Time Lag.

    Returns:
    Auto-covariance value.
    '''

    series_t = np.array(series[:len(series) - lag])
    series_s = np.array(series[lag:])

    n = len(series_t)

    mu_1 = np.mean(series_t)
    mu_2 = np.mean(series_s)

    result = np.sum((series_t - mu_1) * (series_s - mu_2)) / n

    return result


def auto_correlation(series, lag):
    '''
    Compute the auto-correlation of a time series.

    Parameters:
    series: List or numpy array representing the time series.
    lag: Time Lag.

    Returns:
    Auto-correlation value.
    '''
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
