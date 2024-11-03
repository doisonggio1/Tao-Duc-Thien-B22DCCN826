import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import argparse

def radar_chart(player1, player2, attributes):
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv('results.csv', delimiter=';')

    # Lấy dữ liệu của hai cầu thủ
    player1_data = data[data['Player Name'] == player1]
    player2_data = data[data['Player Name'] == player2]

    # Kiểm tra nếu không tìm thấy cầu thủ
    if player1_data.empty or player2_data.empty:
        print("Không tìm thấy cầu thủ. Vui lòng kiểm tra lại tên.")
        return

    # Tính trung bình của các chỉ số được yêu cầu cho mỗi cầu thủ
    player1_stats = player1_data[attributes].mean().values
    player2_stats = player2_data[attributes].mean().values

    # Thiết lập các thông số cho biểu đồ radar
    num_attrs = len(attributes)
    angles = [n / float(num_attrs) * 2 * pi for n in range(num_attrs)]
    angles += angles[:1]  # Đóng vòng tròn

    # Thêm giá trị đầu tiên vào cuối để đóng vòng tròn cho mỗi cầu thủ
    player1_stats = np.append(player1_stats, player1_stats[0])
    player2_stats = np.append(player2_stats, player2_stats[0])

    # Vẽ biểu đồ radar
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    # Vẽ các đường và nhãn trên biểu đồ radar
    plt.xticks(angles[:-1], attributes, color='grey', size=12)
    ax.plot(angles, player1_stats, linewidth=2, linestyle='solid', label=player1)
    ax.fill(angles, player1_stats, 'b', alpha=0.25)

    ax.plot(angles, player2_stats, linewidth=2, linestyle='solid', label=player2)
    ax.fill(angles, player2_stats, 'r', alpha=0.25)

    plt.title(f'So sánh chỉ số: {player1} vs {player2}', size=15, color='navy', y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    # Hiển thị biểu đồ
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Vẽ biểu đồ radar so sánh hai cầu thủ.')
    parser.add_argument('--p1', type=str, required=True, help='Tên cầu thủ thứ nhất')
    parser.add_argument('--p2', type=str, required=True, help='Tên cầu thủ thứ hai')
    parser.add_argument('--Attribute', type=str, required=True, help='Danh sách các chỉ số, cách nhau bằng dấu phẩy')

    args = parser.parse_args()
    player1 = args.p1
    player2 = args.p2
    attributes = args.Attribute.split(',')

    radar_chart(player1, player2, attributes)

