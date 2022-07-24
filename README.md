# Neo's Monaco Editor

Ruby CGI・Node.js CGI を組み合わせて動作するオレオレ Monaco Editor。

__[Enter The Demo Site](https://neos21.github.io/neos-monaco-note)__ … CGI による永続化ではなく LocalStorage を使用したバージョン


## 特徴

- Monaco Editor 部分
    - イタリック体を使用しない Monokai テーマ
    - Noto Sans Mono CJK JP を Web Fonts で読み込み使用
    - スペースなどの不可視文字を可視化
    - 未保存の変更がある場合はマーカを表示する他、タブを閉じる際に確認のプロンプトを表示 (iOS はプロンプト表示には非対応)
- CGI 版
    - Markdown シンタックスにのみ対応
    - 簡易パスワード認証によるアクセス制御 (パスワード認証が通らない場合はエディタ自体が表示されない)
    - 簡易パスワード認証による Markdown ファイルの読み込み・保存
- LocalStorage 版
    - データ永続化方法を CGI ではなく LocalStorage にしたモノ
    - Markdown、HTML、CSS (SCSS)、JavaScript (TypeScript)、Bash (Shell Script) の言語切替に対応


## セットアップ手順

- Apache サーバで Ruby CGI・Node.js CGI が動作するように設定しておく
- `$ npm install` で Monaco Editor の資材を `./node_modules/` に配置する
- `$ bash ./copy-monaco-editor-assets.bash` を実行して Monaco Editor の AMD で動作する各種資材 (`./node_modules/monaco-editor/min/` 配下) を `./min/` にコピーし、同時に `min.zip` を作成する
- Apache サーバにて次のようにファイルを配置する

```
/var/www/html/neos-monaco-note/ … Apache サーバの公開ディレクトリ
├ index.html      … LocalStorage 版 HTML (CGI 類は不要で `min/` のみあれば良い)
├ nmn.rb          … エントリポイントかつパスワード認証を行う Ruby CGI
├ nmn-load.js.cgi … 読込 API として動作する Node.js CGI
├ nmn-save.js.cgi … 保存 API として動作する Node.js CGI
└ min/            … 前述の min.zip を展開したモノ
   └ vs/...

/PATH/TO/private/    … Apache サーバの非公開ディレクトリ
├ credential.txt    … クレデンシャル文字列を記した1行のテキストファイル
└ neos-monaco-note/
   ├ nmn.html       … `index.rb` より認証成功時に読み込まれる HTML
   └ note.md        … ノートの内容が保存されるファイル・存在しなければ新規作成する
```

- `nmn.rb`・`nmn-load.js.cgi`・`nmn-save.js.cgi` の3ファイルについて、実行権を付与し、ファイル内のパス情報を調整する
- 必要に応じて、`nmn.html` 内の API コール URL を調整する
- `http://example.com/neos-monaco-note/nmn.rb?credential=【クレデンシャル文字列】` でアクセスし `nmn.html` が表示されたら、画面右上のテキストボックスに同じクレデンシャル文字列を入力し、「Load」「Save」ボタンが動作するか確認する


## Links

- [Neo's World](https://neos21.net/)
- [GitHub - neos-monaco-note](https://github.com/Neos21/neos-monaco-note)
- [GitHub Pages - neos-monaco-note : Neo's Monaco Note](https://neos21.github.io/neos-monaco-note)
