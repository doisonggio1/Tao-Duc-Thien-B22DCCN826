import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('results.csv', delimiter=';')  # delimiter=';' vì file sử dụng dấu chấm phẩy làm dấu phân cách

# Chọn các cột cần phân tích
columns_to_analyze = ['Min', 'Gls', 'Ast', 'Sh', 'xG', 'SCA']

# Vẽ histogram cho mỗi cột
plt.figure(figsize=(14, 10))
for i, col in enumerate(columns_to_analyze, 1):
    plt.subplot(2, 3, i)
    plt.hist(data[col].dropna(), bins=10, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
