# CommentAnalysis_Git
Public repository of comment analysis  (for streamlit app.)

## アプリの機能
これはYouTubeの配信動画におけるコメントの量を可視化するアプリケーションです。

URL: https://sugiz0261-commentanalysis-git-st-youtube-commentflow-9hjooh.streamlit.app/

フィルタ機能を用いることで、特定のコメント量を可視化することもできます。

## 使い方
1. 動画のURLをコピーします(`https://www.youtuve.com/watch?v=xxxxxxxx`で表示されるものです。`xxxxxxxx`には動画IDが入ります。)。
2. サイドバーのURL入力欄にコピーしたものを貼り付けます。
3. 検索方法で「全検索」を指定して実行すると、動画のコメント量が時系列順に表示されます。表示形式は`hh:mm`です。
4. 検索方法で「フィルタ検索」を指定すると、単語入力欄ガ出現します。ここにはカンマ区切りで単語を入力してください(例：`単語1,単語2`)。
   単語を入力した状態で実行すると、その単語が含まれるコメントの量と時間が表示されます。