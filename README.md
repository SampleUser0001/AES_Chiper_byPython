# AES_Cipher_byPython
AES暗号化をPythonで実装する。

- [AES_Cipher_byPython](#aes_cipher_bypython)
  - [コマンド](#コマンド)
    - [実行：暗号化](#実行暗号化)
    - [実行：復号](#実行復号)
    - [exe化](#exe化)
  - [備考](#備考)
  - [参考](#参考)

## コマンド

```
python -m pip install pycryptodome
```

### 実行：暗号化

コマンドプロンプトで実行する。
```
python encrypter.py
```

### 実行：復号

暗号化の実装待ち。
```

```

### exe化

Windowsで叩く。
```
pyinstaller chiper.py --clean --onefile --key <暗号化パスワード>
```

app\dist配下にexeができる。

## 備考

Docker化はあきらめる。

## 参考

- [Qiita:pythonでAES暗号化/複合化](https://qiita.com/penta2019/items/a500630608960752a914)
