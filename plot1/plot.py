import numpy as np
import matplotlib.pyplot as plt
import os
from style import apply_style


# データ作成
def func(t):
    return 2 * t

# 新しい関数：0〜10の範囲で0.1刻みのランダム値
def func2():
    values = np.arange(0, 10.1, 0.1)  # 0,0.1,0.2,...,10.0
    return np.random.choice(values)

x_values = range(0, 11)
y_values = [func2() for x in x_values]

print(list(x_values))

# 保存先フォルダ
folder = "Python-Plot/plot1/img"
os.makedirs(folder, exist_ok=True)

# ----------------------------
# 1. 点だけのバージョン
# ----------------------------
plt.figure(figsize=(6,6))
plt.scatter(x_values, y_values, color='#1f77b4', s=50, label='points')  # 点だけ
apply_style(xlabel='x', ylabel='y', title='Plot Data')

plt.xlim(0, 10)
plt.ylim(0, 10)

# 1刻みで目盛り設定
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 11, 1))

plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# 保存
plt.savefig(os.path.join(folder, "img_points.png"), dpi=300)
plt.close()  # 画面に表示せず閉じる

# ----------------------------
# 2. 線を引いたバージョン
# ----------------------------
plt.figure(figsize=(6,6))
plt.plot(x_values, y_values,
         marker='o',
         color='#1f77b4',
         linewidth=2,
         markersize=6,
         label='y = 2x')  # 線付き
apply_style(xlabel='x', ylabel='y', title='y = 2x')

plt.xlim(0, 10)
plt.ylim(0, 10)

# 1刻みで目盛り設定
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 11, 1))

plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# 保存
plt.savefig(os.path.join(folder, "img_line.png"), dpi=300)
plt.close()
