import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# 1. 데이터 로드
iris_sklearn = load_iris()
X = iris_sklearn.data  # 특성 데이터
y = iris_sklearn.target  # 클래스 (species)

# 2. 데이터 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. PCA 적용 (주성분 2개)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 4. 결과를 DataFrame으로 변환
pca_df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
pca_df["species"] = iris_sklearn.target_names[y]  # 문자열 라벨로 변환

# 5. 시각화 (PCA 2차원 변환 후 산점도)
plt.figure(figsize=(8, 6))
sns.scatterplot(x="PC1", y="PC2", hue="species", data=pca_df, palette="viridis")
plt.title("PCA Scatter Plot (2 Principal Components)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Species")
plt.show()