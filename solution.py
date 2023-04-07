import pandas as pd
import numpy as np


chat_id = 156090715 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x -= 115
    x = np.log(x)
    return x.mean() # Ваш ответ

