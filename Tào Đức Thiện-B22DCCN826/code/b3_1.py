import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
data = pd.read_csv('results.csv', delimiter=';')

# Chọn các chỉ số cho phân cụm
features = ['Min', 'Gls', 'Ast', 'Sh', 'xG', 'SCA']

# Lấy dữ liệu các chỉ số
X = data[features].fillna(0)  # Điền giá trị 0 cho các ô trống nếu có

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Áp dụng thuật toán K-means với số cụm là 3 (bạn có thể thử với các giá trị khác)
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Xem các nhóm kết quả
print("Số lượng cầu thủ trong mỗi cụm:")
print(data['Cluster'].value_counts())

# Trực quan hóa các cụm với hai chỉ số chính để dễ hình dung
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='xG', y='Gls', hue='Cluster', palette='viridis', s=100)
plt.title('Phân cụm cầu thủ dựa trên K-means')
plt.xlabel('xG (Expected Goals)')
plt.ylabel('Gls (Goals)')
plt.legend(title='Cluster')
plt.show()
