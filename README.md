# Sparrow62 v2 Keyboard KMK Firmware

Sparrow62 v2 の Firmware コード

keymap.py を書き換えて、自在に[キーマップ ./keymap.py](./keymap.py)を変更して楽しんで下さい。

左右分割キーボードを1個の Raspberry PI Pico と MCP23017 で実現するためのトリックが [./code.py](./code.py) に入っています。

## Install

### Circuit Python

Raspberry Pi PICO 用の Circuit Python のファームウェアをダウンロードして、インストールします。

https://circuitpython.org/board/raspberry_pi_pico/

インストールには、PICO 上のボタンを押しながら USB を接続すると、RP2 という USB メモリとして認識するため、その中に uf2 のファイムウェアのファイルを起きます。

### KMK Firmware と必要ファイルのインストール

必要な 2 つのライブラリが、submodule としてこのリポジトリに含まれています。

- MCP23017 のライブラリ: https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx
- KMK Firmware: https://github.com/KMKfw/kmk_firmware

libs 内にない場合、以下のコマンドを実行してチェックアウトします。

```
git submodule update -i
```

Circuit Python がブートされると、CIRCUITPY という USB メモリとして認識するため、以下の 2 つのディレクトリを libs/ 内に置きます。

- libs/libs/Adafruit_CircuitPython_MCP230xx/adafruit_mcp230xx
- libs/kmk_firmware/kmk

### Sparrow62 用のキーマップと、初期ファイルの設置

以下の 2 つのファイルを、CIRCUITPY のルートディレクトリに置きます。

- boot.py
- code.py
- keymap.py

自動で再ロードされるため、キーボードとしてすぐ利用できます。
