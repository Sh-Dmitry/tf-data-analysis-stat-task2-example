import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

chat_id =  285100540 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    scale1 = chi2.ppf(1 - alpha/2, 2*len(x))
    scale2 = chi2.ppf(alpha/2, 2*len(x))
    return np.sqrt(len(x)*np.mean(x**2)/(11*scale1)), \
           np.sqrt(len(x)*np.mean(x**2)/(11*scale2))
