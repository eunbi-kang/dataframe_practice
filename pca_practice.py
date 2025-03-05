import seaborn as sns
import numpy as np
from numpy.linalg import inv, eig


## ✅마할라노비스 거리 구하기 (4): 고유값, 고유벡터 구하기
if __name__ == "__main__":
    iris = sns.load_dataset('iris')
    iris_data = iris[["sepal_length", "sepal_width", 'petal_length', "petal_width"]]

    # Step1. 평균 구하기
    iris_mean = iris_data.mean(axis=0)
    # Step2. 공분산 구하기
    iris_cov = (iris_data - iris_mean).T @ (iris_data - iris_mean)
    # Step3. 고유값(Eigenvalues), 고유벡터(eigenvectors) 구하기
    eigenvalues, eigenvectors = np.linalg.eig(iris_cov)
    print(eigenvalues)
    print(eigenvectors)


