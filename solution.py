import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

chat_id =  285100540 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    s = (len(x)-1) * np.var(x)
    scale1 = chi2.ppf(1 - alpha/2, len(x)-1)
    scale2 = chi2.ppf(alpha/2, len(x)-1)
    return np.sqrt(s/(11*scale1)), \
           np.sqrt(s/(11*scale2))
