import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    array = np.array(list)
    mean = []
    variance = []
    standard_deviation = []
    max_values = []
    min_values = []
    sum_values = []
    
    matrix = array.reshape(3, 3)
    mean.append(matrix.mean(axis=0).tolist())
    mean.append(matrix.mean(axis=1).tolist())
    mean.append(matrix.mean().item())
    variance.append(matrix.var(axis=0).tolist())
    variance.append(matrix.var(axis=1).tolist())
    variance.append(matrix.var().item())
    standard_deviation.append(matrix.std(axis=0).tolist())
    standard_deviation.append(matrix.std(axis=1).tolist())
    standard_deviation.append(matrix.std().item())
    max_values.append(matrix.max(axis=0).tolist())
    max_values.append(matrix.max(axis=1).tolist())
    max_values.append(matrix.max().item())
    min_values.append(matrix.min(axis=0).tolist())
    min_values.append(matrix.min(axis=1).tolist())
    min_values.append(matrix.min().item())
    sum_values.append(matrix.sum(axis=0).tolist())
    sum_values.append(matrix.sum(axis=1).tolist())
    sum_values.append(matrix.sum().item())

    calculations = {"mean": mean, "variance": variance, "standard deviation": standard_deviation, "max": max_values, "min": min_values, "sum": sum_values}

    return calculations