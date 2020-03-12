# -*- coding: utf-8 -*-
# 設定ファイルを読み込む
import os
from setup.setup import *
# FTPモジュールを読み込む
from ftplib import FTP

class ftp:

    # 対象のホストにアクセスしてログイン
    def connect(self):
        self.ftp = FTP(host, username, password)
        return self

    #(1)クライアントのアップロード対象のファイル・ディレクトリを全て取得
    def getAllFilesAndDirectries(self):
        self.getAll = os.walk(basepath)
        return self

    #取得したものがディレクトリである
    def isDirectry(self, directryPath):
        return os.path.isdir(directryPath)   


# ======================

print ftp().connect().ftp # OK 
print ftp().getAllFilesAndDirectries().getAll # OK 
print ftp().isDirectry('hogehoge/') # directry does not exits 
print ftp().isDirectry('hogtext.txt') # file exits(not directry)
print ftp().isDirectry(basepath) # directry exits





























# ======================

            #サーバーにディレクトリを作成
        #未処理のファイル・ディレクトリが存在する
    #(2)クライアントのアップロード対象のファイル・ディレクトリを全て取得
        #取得したものがファイルである
            #サーバーにファイルをアップロード
        #未処理のファイル・ディレクトリが存在する
#FTP接続を終了
