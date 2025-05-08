import numpy as np
import pandas as pd


def main():
    """
    マクローリン展開のシミュレーション
    
    1 / 1-x = sigma_{n=0}^infty x^n をシミュレートする
    """
    
    delta_list_10 = list()
    delta_list_100 = list()
    delta_list_1000 = list()
    delta_list_10000 = list()
    
    for x in np.linspace(-0.5, 0.5, 100):
        true_f = f(x)
        
        approx_y_10 = g(x, 10)
        approx_y_100 = g(x, 100)
        approx_y_1000 = g(x, 1000)
        approx_y_10000 = g(x, 10000)
        
        delta_10 = true_f - approx_y_10
        delta_100 = true_f - approx_y_100
        delta_1000 = true_f - approx_y_1000
        delta_10000 = true_f - approx_y_10000
    
        delta_list_10.append(delta_10)
        delta_list_100.append(delta_100)
        delta_list_1000.append(delta_1000)
        delta_list_10000.append(delta_10000)
    
    delta_df = pd.DataFrame({
        'delta_10': delta_list_10, 
        'delta_100': delta_list_100, 
        'delta_1000': delta_list_1000, 
        'delta_10000': delta_list_10000, 
    })
    
    print(delta_df)
    
    delta_df.reset_index(inplace=True)
    
    delta_melt_df = pd.melt(
        delta_df, 
        id_vars='index',        
    )
    print(delta_melt_df)
        
    return


def f(x: float) -> float:
    return 1 / (1 - x)

def g(x: float, n: int=100) -> float:    
    x_list = [x**i for i in np.arange(n)]    

    return np.sum(x_list)


if __name__ == '__main__':
    main()
