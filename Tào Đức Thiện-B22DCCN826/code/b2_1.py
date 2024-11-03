    
import pandas as pd
import numpy as np

    # Đọc dữ liệu từ file results.csv
df = pd.read_csv('results.csv', delimiter=';')

    # Kiểm tra tên các cột
print("Columns in DataFrame:", df.columns)

    # Danh sách các chỉ số cần tính toán
attributes = [
        'Min', 'Gls', 'Ast', 'PK', 'PKatt', 'Sh', 'SoT', 'CrdY', 'CrdR', 
        'Touches', 'Tkl', 'Int', 'Blocks', 'xG', 'npxG', 'xAG', 'SCA', 
        'GCA', 'Cmp', 'Att', 'Cmp%', 'PrgP', 'Carries', 'PrgC', 'Succ'
    ]

    # Đổi 'Player Name' thành tên cột thực sự chứa tên cầu thủ nếu cần
player_name_column = 'Player Name'  # Đảm bảo cột này chứa tên cầu thủ

    # Chuyển các cột số sang kiểu dữ liệu số (nếu cần)
for attr in attributes:
        df[attr] = pd.to_numeric(df[attr], errors='coerce')

    # 1. Tìm top 3 cầu thủ cao nhất và thấp nhất ở mỗi chỉ số
top_bottom_players = {}
for attr in attributes:
        if attr in df.columns and df[attr].dtype in [np.float64, np.int64]:  # Kiểm tra cột có kiểu số
            # Kiểm tra cột 'Age' có tồn tại không trước khi chọn cột
            columns_to_display = ['Squad', 'Opponent', player_name_column, attr]
            if 'Age' in df.columns:
                columns_to_display.insert(3, 'Age')  # Thêm cột Age nếu có
            top_3 = df.nlargest(3, attr)[columns_to_display]
            bottom_3 = df.nsmallest(3, attr)[columns_to_display]
            top_bottom_players[attr] = {'top_3': top_3, 'bottom_3': bottom_3}

    # In kết quả top 3 cao nhất và thấp nhất của mỗi chỉ số
for attr, data in top_bottom_players.items():
        print(f"Top 3 players for {attr}:\n", data['top_3'])
        print(f"Bottom 3 players for {attr}:\n", data['bottom_3'])
