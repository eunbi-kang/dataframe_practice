import seaborn as sns
from pandas.core.common import random_state
import numpy as np

if __name__ == "__main__":
    # 데이터셋 로드
    iris = sns.load_dataset('iris')

    # 컬럼 정보 및 species 종류 확인
    print(iris.keys())
    print(iris['species'].unique())

    # 각 품종을 필터링하고 명확한 복사본 생성
    setosa = iris[iris['species'] == "setosa"].copy()
    setosa["species"] = 0

    versicolor = iris[iris['species'] == "versicolor"].copy()
    versicolor["species"] = 1

    virginica = iris[iris['species'] == "virginica"].copy()
    virginica["species"] = 2

    ## ✅마할라노비스 거리 구하기 (1): 평균 구하기 - mean()
    setosa_data = setosa[["sepal_length", "sepal_width", 'petal_length', "petal_width"]]
    setosa_sample2 = setosa_data.sample(n=2, random_state=42) # 샘플데이터2개, random_state: 시드값
    setosa_remaing = setosa_data.drop(setosa_sample2.index) # 50 - 42(random_state)
    setosa_mean = setosa_data.mean(axis=0)

    virginica_data = virginica[["sepal_length", "sepal_width", 'petal_length', "petal_width"]]
    virginica_sample2 = virginica_data.sample(n=2, random_state=42)  # virginica_data 샘플데이터 2개 뽑음
    virginica_remaing = virginica_data.drop(virginica_sample2.index)
    virginica_mean = virginica_data.mean(axis=0)

    versicolor_data = versicolor[["sepal_length", "sepal_width", 'petal_length', "petal_width"]]
    versicolor_sample2 = versicolor_data.sample(n=2, random_state=42)  # virsicolor_data 샘플데이터 2개 뽑음
    versicolor_remaing = versicolor_data.drop(versicolor_sample2.index)
    versicolor_mean = versicolor_data.mean(axis=0)




    print('setosa:', setosa_mean.values)
    print('virsicolor:', versicolor_mean.values)
    print('virginica:', virginica_mean.values)

    ## ✅마할라노비스 거리 구하기 (2): 공분산 행렬 구하기
    # @: 곱하기, T: 역(reverse)
    setosa_cov = ((setosa_data - setosa_mean).T@(setosa_data-setosa_mean)).values
    versicolor_cov = ((versicolor_data - versicolor_mean).T @ (versicolor_data - versicolor_mean)).values
    virginica_cov = ((virginica_data - virginica_mean).T @ (virginica_data - virginica_mean)).values

    ## ✅마할라노비스 거리 구하기 (3): 공분산 행렬의 역행렬 구하기
    # 역행렬 값 클수록 : 원본행렬 값들이 작거나, 행렬이 특이점에 가깝다는 의미
    setosa_cov_inv = np.linalg.inv(setosa_cov)
    versicolor_cov_inv = np.linalg.inv(versicolor_cov)
    virginica_cov_inv = np.linalg.inv(virginica_cov)

    d0 = (setosa_sample2.values[0] - setosa_mean.values).T @ setosa_cov_inv @ (setosa_sample2.values[0] - setosa_mean.values)
    print("setosa: ", d0)
    d1 = (versicolor_sample2.values[0] - versicolor_mean.values).T @ versicolor_cov_inv @ (
                versicolor_sample2.values[0] - versicolor_mean.values)
    print("versicolor: ", d1)
    d2 = (virginica_sample2.values[0] - virginica_mean.values).T @ virginica_cov_inv @ (
                virginica_sample2.values[0] - virginica_mean.values)
    print("virginica: ", d2)