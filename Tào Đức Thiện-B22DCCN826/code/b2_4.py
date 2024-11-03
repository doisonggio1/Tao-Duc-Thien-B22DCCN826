import pandas as pd

# Đọc dữ liệu từ file CSV
data = pd.read_csv('results.csv', delimiter=';')

# Chọn các chỉ số cần phân tích
columns_to_analyze = ['Min', 'Gls', 'Ast', 'Sh', 'xG', 'SCA']

# Tính tổng điểm số của từng đội ở mỗi chỉ số
team_stats = data.groupby('Squad')[columns_to_analyze].sum()

# Tìm đội có giá trị cao nhất cho từng chỉ số
best_teams = team_stats.idxmax()

# In ra đội có điểm số cao nhất cho từng chỉ số
print("Đội có chỉ số cao nhất ở mỗi mục:")
print(best_teams)

# Đánh giá đội có phong độ tốt nhất dựa trên các chỉ số
best_team = best_teams.value_counts().idxmax()
print(f"\nĐội có phong độ tốt nhất giải đấu có thể là: {best_team}")
