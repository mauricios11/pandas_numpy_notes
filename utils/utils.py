import numpy as np

def func(array):
    mean = np.mean(array)
    return mean

def data_json():
    #listas
    a_values1 = ['A0', 'A1', 'A2', 'A3']
    b_values1 = ['B0', 'B1', 'B2', 'B3']
    c_values1 = ['C0', 'C1', 'C2', 'C3']
    d_values1 = ['D0', 'D1', 'D2', 'D3']

    a_values2 = ['A4', 'A5', 'A6', 'A7']
    b_values2 = ['B4', 'B5', 'B6', 'B7']
    c_values2 = ['C4', 'C5', 'C6', 'C7']
    d_values2 = ['D4', 'D5', 'D6', 'D7']
    #listas de listas
    values_1 = [a_values1, b_values1, c_values1, d_values1]
    values_2 = [a_values2, b_values2, c_values2, d_values2]
    
    keys = ['A', 'B', 'C', 'D']
    #dicts
    dict_1 = dict(zip(keys, values_1))
    dict_2 = {keys : values_2 for keys , values_2 in zip(keys , values_2)}
    
    # listas 2
    e_values11 = ['k0', 'k1', 'k2', 'k3']
    f_values11 = ['A0', 'A1', 'A2', 'A3']
    g_values11 = ['B0', 'B1', 'B2', 'B3']
        
    e_values22 = ['k0', 'k1', 'k2', 'k3']
    f_values22 = ['C0', 'C1', 'C2', 'C3']
    g_values22 = ['D0', 'D1', 'D2', 'D3']
        
    keys_11 = ['key', 'A', 'B']
    keys_22 = ['key', 'C', 'D']
    
        
    # lista de listas 2
    values_11 = [e_values11, f_values11, g_values11]
    values_22 = [e_values22, f_values22, g_values22]
    #keys_4 = [keys_2, keys_2]

    #dicts2
    dict_3 = dict(zip(keys_11, values_11))
    dict_4 = {keys: values for keys, values in zip(keys_22, values_22)}
    
    #lista de listas 3
    keys_33 = ['key_2', 'C', 'D']
    
    #dicts3
    dict_5 = dict(zip(keys_33, values_22))
    
    #lista de listas 4
    values_44 = [a_values1, b_values1]
    values_55 = [c_values1, d_values1]
    
    keys_44 = ['A', 'B']
    keys_55 = ['C', 'D']
    
    #dicts4
    dict_6 = dict(zip(keys_44, values_44))
    dict_7 = {keys : values for keys, values in zip(keys_55, values_55)}
    
    hola = "hola :D"  
    return dict_1, dict_2, dict_3, dict_4, dict_5, dict_6, dict_7