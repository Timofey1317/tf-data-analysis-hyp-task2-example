import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 1028099632 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p_value = ks_2samp(x, y)
    alpha = 0.02
