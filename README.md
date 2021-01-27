# IOTWebServer
## インストール & 実行

```bash
# https://github.com/dododoSA/IOTWebServer をFork

git clone フォークした自分のリポジトリ

cd IOTWebServer

pip install Flask

python server.py
```

http://127.0.0.1:8000/ にアクセス


## パラメータについて
```javascript
// templates/piano.html

////////////////////////////メインの実行
function piano() {
	const canvas = document.getElementById('sample');
    const board = document.getElementById('board');
    
    // 【音階の周波数】

	//                     ド　　　レ　　　ミ　　　ファ　ソ　　　ラ　　　シ　　　ド　　　レ　　ミ　　　ファ　　ソ　　　ラ　　シ　
	const onkaiListW = [130.8, 146.8, 164.8, 174.6, 196.0, 220.0, 246.9, 261.6, 293.7, 329.6, 349.2, 392.0, 440.0, 493.9];
	//                   ド＃　レ＃　　ファ＃　ソ＃　　ラ＃　　ド＃　レ＃　　ファ＃　ソ＃　　ラ＃
    const onkaiListB = [138.6, 155.6, 185.0, 297.7, 233.1, 277.2, 311.1, 370.0, 415.3, 466.2];

    // --------- 略 ---------


    // 【音階の周波数の送信間隔】


	// 一定の間隔で周波数のデータを送信
	const interval = 1000;
	setInterval(() => {
		axios.post("/freq", {
			freq: freq
		})
		.then(res => {
			console.log(res.data)
		})
		.catch(err => {
			console.log(err)
		})
	}, interval)

}
```


## hackmd
https://hackmd.io/KklKp2gdS_GjFV2DHMsE3w