import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
data = pd.read_csv('results.csv', delimiter=';')

# Chọn các chỉ số cho phân tích
features = ['Min', 'Gls', 'Ast', 'Sh', 'xG', 'SCA']
X = data[features].fillna(0)  # Điền giá trị 0 cho các ô trống nếu có

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Áp dụng PCA để giảm số chiều xuống 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Áp dụng phân cụm K-means trên dữ liệu đã giảm chiều
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_pca)

# Thêm các cột PCA và Cluster vào DataFrame
data['PCA1'] = X_pca[:, 0]
data['PCA2'] = X_pca[:, 1]
data['Cluster'] = clusters

# Trực quan hóa các cụm trên mặt phẳng 2D
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='PCA1', y='PCA2', hue='Cluster', palette='viridis', s=100)
plt.title('Phân cụm cầu thủ với K-means trên không gian PCA')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend(title='Cluster')
plt.show()
    