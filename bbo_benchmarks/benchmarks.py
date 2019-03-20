import os
import sys
import numpy as np
import torch

import benchmarks.cec2013.cec13 as cec13_func
import benchmarks.cec2017.cec17 as cec17_func


def func_wrapper(func, func_id):

    def wrapped(x):
        origin_type = type(x)
        if origin_type is not list:
            origin_shape = x.shape
            dim = origin_shape[-1]
        
            if origin_type is torch.Tensor:
                x = x.cpu().numpy()
            x = x.reshape((-1, dim)).tolist()

        if func == "cec13":
            tmp = cec13_func.eval(x, func_id+1)
        elif func == "cec17":
            tmp = cec17_func.eval(x, func_id+1)
        else:
            raise Exception("No such benchmark!")
        
        if origin_type is np.ndarray:
            return np.array(tmp).reshape(origin_shape[:-1])
        elif origin_type is torch.Tensor:
            return torch.tensor(tmp).reshape(origin_shape[:-1])
        elif type(x) is list and type(x[0]) is list:
            return tmp
        else:
            return tmp[0]

    return wrapped

cec13 = [func_wrapper("cec13", func_id) for func_id in range(28)]
cec17 = [func_wrapper("cec17", func_id) for func_id in range(30)]

