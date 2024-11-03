import pandas as pd
import numpy as np

# Đọc dữ liệu từ file results.csv
df = pd.read_csv('results.csv', delimiter=';')

# Danh sách các chỉ số cần tính toán
attributes = [
    'Min', 'Gls', 'Ast', 'PK', 'PKatt', 'Sh', 'SoT', 'CrdY', 'CrdR', 
    'Touches', 'Tkl', 'Int', 'Blocks', 'xG', 'npxG', 'xAG', 'SCA', 
    'GCA', 'Cmp', 'Att', 'Cmp%', 'PrgP', 'Carries', 'PrgC', 'Succ'
]

# Chuyển các cột số sang kiểu dữ liệu số (nếu cần)
for attr in attributes:
    df[attr] = pd.to_numeric(df[attr], errors='coerce')

# 1. Tính trung vị, trung bình và độ lệch chuẩn cho từng chỉ số trên toàn giải
overall_stats = {
    'Team': 'all',
    'Median': df[attributes].median(),
    'Mean': df[attributes].mean(),
    'Std': df[attributes].std()
}

# 2. Tính trung vị, trung bình và độ lệch chuẩn cho từng chỉ số của từng đội
team_stats = []
for team in df['Squad'].unique():
    team_df = df[df['Squad'] == team]
    team_stat = {
        'Team': team,
        'Median': team_df[attributes].median(),
        'Mean': team_df[attributes].mean(),
        'Std': team_df[attributes].std()
    }
    team_stats.append(team_stat)

# 3. Chuyển đổi kết quả thành DataFrame để ghi vào file CSV
# Tạo DataFrame từ các thống kê toàn giải và từng đội
summary_df = pd.DataFrame([overall_stats] + team_stats)

# Tách các giá trị trung vị, trung bình và độ lệch chuẩn ra thành các cột riêng
summary_df = pd.concat([summary_df.drop(['Median', 'Mean', 'Std'], axis=1), 
                        summary_df['Median'].apply(pd.Series).add_prefix('Median_'),
                        summary_df['Mean'].apply(pd.Series).add_prefix('Mean_'),
                        summary_df['Std'].apply(pd.Series).add_prefix('Std_')], axis=1)

# 4. Ghi kết quả ra file CSV
summary_df.to_csv('results2.csv', index=False)

print("Kết quả đã được ghi vào file results2.csv")
