import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath("C:/dev/plot/Python-Plot"))
from style import apply_style

a = np.array([1,2,3])
word = "haru1"

print("Hello Haru!!")

print(a)

if word == "haru":
    print("word is haru")

for i in range(1,10+1,1):
    print("値は",i,"です。")

# numpyで読み込み
# data = np.loadtxt("Python-Plot/data/data.csv",delimiter=",",skiprows=1)
# data = np.genfromtxt("Python-Plot/data/data.csv", delimiter=",", dtype=None, encoding="utf-8", names=True)
# print(data)

# Pandasで読み込み
df = pd.read_csv("Python-Plot/data/data.csv")
print(df.head)

plt.plot(df['ID'],df['colum1'],marker='o')
# スタイル適用
apply_style(xlabel='ID', ylabel='colum1', title='ID vs colum1')

plt.show()

folder = "Python-Plot/graphs"

# 保存
# filepath = os.path.join(folder, "id_vs_colum1.png")
# plt.savefig(filepath,dpi=300)
# plt.close() # 画面に表示せずに閉じる

