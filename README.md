# Sparrow62 v2 Keyboard KMK Firmware

Sparrow62 v2 の Firmware コード

keymap.py を書き換えて、自在に[キーマップ ./keymap.py](./keymap.py)を変更して楽しんで下さい。

左右分割キーボードを 1 個の Raspberry PI Pico と MCP23017 で実現するためのトリックが [./code.py](./code.py) に入っています。

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

また、RGB LED を点灯する NeoPixel モジュールをインストールします。
以下のリリースから、 adafruit-circuitpython-bundle-7.x-mpy-20220326.zip をダウンロードし、ZIP 中の lib/neopixel.mpy を、CIRCUITPY 内の libs/ 内に置きます。

https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

### Sparrow62 v2 用のキーマップと、初期ファイルの設置

以下の 2 つのファイルを、CIRCUITPY のルートディレクトリに置きます。

- boot.py
- code.py
- keymap.py

boot.py には、自動リロードをオフにする設定が入っています（ソースコードが置き換わる前に、リロードされるとエラーになるため）。

### 2 回目移行のアップグレード

このリポジトリには、MacOS、Linux で使用できるアップロードコマンドが Python のタスクランナー Invoke で実装されています。

invoke、detect がインストールされている場合（もしくは poetry install を行った場合）、以下のコマンドでアップロードを実行できます。

```
# invoke, detect がインストールされている
inv -e upload

# poetry を使う場合
poetry run inv -e upload
```

詳しい実装は [./tasks.py](./tasks.py) をみてみてください。

## Circuit Python の Serial Console の開き方

Circuit Python の出力は、USB シリアルコンソールに出力されます。エラー時のエラーメッセージもこちらに表示されます。

接続の仕方はこちらを確認ください。

https://zenn.dev/link/comments/cc8372b5b0c7d4

## LED の色

初期起動時には LED の色は白色に光ります。
その後、発色を抑えるなどをおこなってください。

## エラーの時

この code.py には、モジュールの読み込みでエラーが発生した場合、自動的に 10 秒で再起動する処理が入っています。
慌てずに、kmk などライブラリを CIRCUITPY 内の lib/ に入れてください。

キーマップを開発している時、Python のコードのため、実行するまでエラーが含まれているかどうかがわかりません。
この code.py ではキーマップの読み込みでエラーになった場合、LED を赤色に変えて、さらに backup_keymap.py を読み込んで実行するようになっています。
ぜひ、動作する状態のキーマップを backup_keymap.py として保存しておいてください。

## Pro Micro のリセットボタンの機能がほしい

実装できます。

## その他のテクニックや、トラブルシューティング

Zenn にまとめています。

https://zenn.dev/74th/scraps/c59fb553c9309f
