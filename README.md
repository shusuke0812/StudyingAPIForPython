FastAPIを使ったAPIの作成練習
====

## 環境
- MacOS Catalina version 10.15.4
- python version 3.8.1
- pip version 20.1  

## サンプルコード概要
- 

## 実行方法  
- conda環境に入る
```bash
$ conda activate fastapi_todo
```
- conda環境を抜ける
```bash
$ conda deactivate
```
## ルール
- ダブルクォーテーションとシングルクオーテーションの使い分け  
ダブル： エクケープ文字がある場合、docstring（[PEP 257](https://www.python.org/dev/peps/pep-0257/)）、コードブロックの無効化  
シングル：上記以外

## Memo
- FastAPIの特徴：動作が早い、非同期処理ができる
- redoc（swaggerUI）を使えばブラウザ１つでリクエスト、レスポンスのデバッグができる  
						   
## 参考文献   
- [はんなりPython FastAPIハンズオン 資料１](https://scrapbox.io/PythonOsaka/FastAPI_%E3%81%A7RESTful_Web%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E5%AE%9F%E8%A3%85_Part1)
- [はんなりPython FastAPIハンズオン 資料２](https://scrapbox.io/PythonOsaka/FastAPI_%E3%81%A7RESTful_Web%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E5%AE%9F%E8%A3%85_Part2)					
- [はんなりPython FastAPIハンズオン 資料３](https://scrapbox.io/PythonOsaka/FastAPI%E3%81%A7Web%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%92%E4%BF%9D%E8%AD%B7%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B)
- [はんなりPython FastAPIハンズオン 資料４](https://scrapbox.io/PythonOsaka/FastAPI%E3%81%A8SQLAlchemy_%E3%81%AB%E3%82%88%E3%82%8BWeb%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E5%AE%9F%E8%A3%85)
