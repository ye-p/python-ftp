# -*- coding: utf-8 -*-
import os
import pdb
# ftpモジュールを読み込む
from ftplib import FTP
from setup.setup import *

class FtpUpload:

    # 対象のホストにログイン
    ftp = FTP(host, username, password)
    print ftp

    # サーバー上のカレントディレクトリの一覧を取得

    # 取得したものがディレクトリである
    # サーバーにディレクトリを作成
    # 未処理のファイル・ディレクトリが存在する
    # サーバー上のカレントディレクトリの一覧を取得
    # 取得したものがファイルである
    # サーバーにファイルをアップロード
    # 未処理のファイル・ディレクトリが存在する
    # FTPサーバとの切断
    def quit(self):
        self.ftp.quit

# 関数をメソッドチェーンで呼び出し
ftp = FtpUpload()
# FTPサーバとの切断
ftp.quit()
