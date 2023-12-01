from scipy import stats
import numpy as np
import blpapi as bb

_norm_cdf = stats.norm(0, 1).cdf
_norm_pdf = stats.norm(0, 1).pdf

def _d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))


def _d2(S, K, T, r, sigma):
    return _d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


def call_value(S, K, T, r, sigma):
    return S * _norm_cdf(_d1(S, K, T, r, sigma)) - K * np.exp(-r * T) * _norm_cdf(_d2(S, K, T, r, sigma))


def put_value(S, K, T, r, sigma):
    return np.exp(-r * T) * K * _norm_cdf(-_d2(S, K, T, r, sigma)) - S * _norm_cdf(-_d1(S, K, T, r, sigma))


def call_delta(S, K, T, r, sigma):
    return _norm_cdf(_d1(S, K, T, r, sigma))


def put_delta(S, K, T, r, sigma):
    return call_delta(S, K, T, r, sigma) - 1


def call_vega(S, K, T, r, sigma):
    return S * _norm_pdf(_d1(S, K, T, r, sigma)) * np.sqrt(T)


def put_vega(S, K, T, r, sigma):
    return call_vega(S, K, T, r, sigma)
