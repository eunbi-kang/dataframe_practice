##  🔥 4차원 데이터(sepal_length, sepal_width, petal_length, petal_width)를
##      1차원으로 압축(PCA 변환) 해보기
import seaborn as sns
import numpy as np
from distance_test import setosa_sample2, virginica_sample2, versicolor_sample2

if __name__ == "__main__":
    iris = sns.load_dataset('iris')    # seaborn을 사용하여 Iris 데이터셋 로드
    iris_data = iris[["sepal_length", "sepal_width", 'petal_length', "petal_width"]]

    ## ❗️Step1) 평균 구하기
    iris_mean = iris_data.mean(axis=0)

    ## ❗Step2) 공분산 구하기 => np.cov(iris_data.T)와 같은 결과
    iris_cov = (iris_data - iris_mean).T @ (iris_data - iris_mean)

    ## ❗Step3) 고유값(Eigenvalues), 고유벡터(eigenvectors) 구하기
    #   - 고유값 : 데이터를 설명하는 축의 중요도를 나타냄
    #           값이 클수록 데이터의 변동성이 크고, 중요한 정보가 포함된 방향
    #   - 고유벡터 : 데이터의 주요 방향
    #            PCA에서 주성분(Principal Components)이 됨
    eigenvalues, eigenvectors = np.linalg.eig(iris_cov)
    # print(eigenvalues)
    # print(eigenvectors)

    ## ❗Step4) 샘플데이터 첫 번째 주성분 방향으로 새로운 차원축소값 생성
    print(setosa_sample2 @ eigenvectors[0]) # setosa 내적(거리의 합)
    print(versicolor_sample2 @ eigenvectors[0]) # versicolor 내적
    print(virginica_sample2 @ eigenvectors[0]) # virginica 내적



