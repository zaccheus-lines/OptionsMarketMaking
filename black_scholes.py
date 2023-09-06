from scipy import stats
import numpy as np

z_cdf = stats.norm(0, 1).cdf
z_pdf = stats.norm(0, 1).pdf

def d1 (S, K, T, r, sigma):
    numerator = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) 
    denominator = (sigma * np.sqrt(T))
    return numerator/denominator 


def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


def metrics(S, K, T, r, sigma):
    '''
    Calculate the fair price of a European call option.
    
    Param:
    ----------
    S : float
        The current value of the underlying stock.
    K : float
        The strike price of the option. 
    T : float
        Time to expiry in years.
    r : float
        The fixed interest rate.
    sigma : float
        The volatility of the underlying stock process.

    Returns:
    -------
    np.ndarray
        A 2 x 3 NumPy array:
        
        - The first row contains the fair price of the call option, call delta, and call vega.
        - The second row contains the fair price of the put option, put delta, and put vega.
        
        The structure of the returned array is as follows:
        [[call_price, call_delta, call_vega],
         [put_price, put_delta, put_vega]]
    '''
    
    call_price = S * z_cdf(d1(S, K, T, r, sigma)) - K * np.exp(-r * T) * z_cdf(d2(S, K, T, r, sigma))

    call_delta = call_delta = z_cdf(d1(S, K, T, r, sigma))

    call_vega = S * z_pdf(d1(S, K, T, r, sigma)) * np.sqrt(T)

    put_price = np.exp(-r * T) * K * z_cdf(-d2(S, K, T, r, sigma)) - S * z_cdf(-d1(S, K, T, r, sigma))

    put_delta = call_delta -1

    put_vega = call_vega

    return np.array([[call_price, call_delta, call_vega], [put_price, put_delta, put_vega]], dtype=float)
