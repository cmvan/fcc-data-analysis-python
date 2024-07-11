import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    calculations = np.array(lst)
    calculations = calculations.reshape(3,3)
    calculations = {
        'mean': [calculations.mean(axis=0).tolist(), calculations.mean(axis=1).tolist(), calculations.mean()],
        'variance': [calculations.var(axis=0).tolist(), calculations.var(axis=1).tolist(), calculations.var()],
        'standard deviation': [calculations.std(axis=0).tolist(), calculations.std(axis=1).tolist(), calculations.std()],
        'max': [calculations.max(axis=0).tolist(), calculations.max(axis=1).tolist(), calculations.max()],
        'min': [calculations.min(axis=0).tolist(), calculations.min(axis=1).tolist(), calculations.min()],
        'sum': [calculations.sum(axis=0).tolist(), calculations.sum(axis=1).tolist(), calculations.sum()]
    }
    return calculations
