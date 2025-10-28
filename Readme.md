# Pythonパッケージ基本資料

`cmd + shift + P`で`disable cusor tab`を選択することで、オートコンプリートをオフにする。

# 検証準備

こちらはクローンの前に実行しておく。
また、OneDrive上で行わず、ローカルPCのみで行う。
理由は、`venv`などを実行したいに無駄な共有が発生してしまい、サーバに負荷がかかるため。

## 作業用ローカルディレクトリの作成

仮想環境使うのであれば、以下にディレクトリを作成したのでここで行う。
```
cd C:\dev
```

## 仮想環境の作成
プロット用の仮想環境を作成する。
```
python3 -m venv plot
cd plot
```
ここでクローンを行う。

```
Scripts/python.exe --version
```

```
Scripts/pip.exe list
Package Version
------- -------
pip     25.0.1
```
```
Scripts/pip.exe install numpy

```