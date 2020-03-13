# -*- coding: utf-8 -*-
# モジュールを読み込む
import os
# FTPモジュールを読み込む
from ftplib import FTP
# 設定ファイルを読み込む
from setup.setup import *

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

    #サーバーにディレクトリを作成
    def makeDirectry(self, directryName):
        self.ftp = FTP(host, username, password)
        return self.ftp.mkd(directryName)

    #未処理のファイル・ディレクトリが存在する
    def unUploadFilesOrDirectries(self, func):
        #self.getAll = os.walk(basepath)
        print basepath
        return self



# ================================
#   Function call
# ================================

print ftp().connect().ftp # OK 
print ftp().getAllFilesAndDirectries().getAll # OK 
print ftp().isDirectry('hogehoge/') # directry does not exits → OK
print ftp().isDirectry('hogtext.txt') # file exits(not directry) → OK
print ftp().isDirectry('./upload/') # directry exits → OK
#print ftp().makeDirectry('dir') # OK
print ftp().unUploadFilesOrDirectries(ftp().isDirectry(basepath)) # NG 
#print ftp().unUploadFilesOrDirectries() # NG 

# ================================
#   Comment to make functions
# ================================

            # (1)の次ループへ
    #(2)クライアントのアップロード対象のファイル・ディレクトリを全て取得
        #取得したものがファイルである
            #サーバーにファイルをアップロード
        #未処理のファイル・ディレクトリが存在する
            # (2)の次ループへ
#FTP接続を終了

