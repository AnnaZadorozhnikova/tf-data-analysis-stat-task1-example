import pandas as pd
import numpy as np
import math


chat_id = 393669278 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = np.array([math.log(i) for i in x-635]) 
    return x.mean() # Ваш ответ
