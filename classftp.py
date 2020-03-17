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

    # (1)クライアントのアップロード対象のファイル・ディレクトリを全て取得
    def getAllFilesAndDirectries(self):
        self.walk = os.walk(basepath)
        return self

    # 取得したものがディレクトリである
    def isDirectry(self, directryPath):
        return os.path.isdir(directryPath)   

    # サーバーにディレクトリを作成
    def makeDirectry(self, directryName):
        return self.ftp.mkd(directryName)

    # 未処理のファイル・ディレクトリが存在する
    def unUploadFilesOrDirectries(self, func):
        #self.getAll = os.walk(basepath)
        print basepath
        return self

    # (1)の次ループへ

    # (2)クライアントのアップロード対象のファイル・ディレクトリを全て取得

    # 取得したものがファイルである
    def isFile(self, filePath):
        return os.path.isfile(filePath)   

    # ファイルを開く 
    def openFile(self, filePath):
        self.fh = open(filePath, 'rb')
        return self

    # ファイルをアップロード
    def uploadFile(self, filePath):
        return self.ftp.storbinary('STOR %s' % filePath, self.fh)

    # ファイルを閉じる
    def closeFile(self):
        return self.fh.close()

    # 未処理のファイル・ディレクトリが存在する

    # (2)の次ループへ

    # FTP接続を終了
    def quitFtp(self):
        return self.ftp.quit()

    def main(self):
        self.connect().getAllFilesAndDirectries()
    
        for dirpath, dirname, filename in self.walk:
            if self.isDirectry(dirpath):
                self.makeDirectry(dirpath)
            for fName in filename:
                f = dirpath + '/{}'.format(fName)
                if self.isFile(f):
                    self.openFile(f)
                    self.uploadFile(f)
                    self.closeFile()

        self.quitFtp()
    
ftp = ftp()
ftp.main() 

# ================================
#   Function call
# ================================

# ftp = ftp()
# print ftp.connect().ftp # OK 
# print ftp.getAllFilesAndDirectries().walk # OK 
# print ftp.isDirectry('hogehoge/') # not found directry → OK
# print ftp.isDirectry(basepath + 'hogetext.txt') # file exits(not directry) → OK
# print ftp.isDirectry(basepath + 'dir') # directry exits → OK
# print ftp.makeDirectry('dir') # OK
# print ftp.unUploadFilesOrDirectries(ftp.isDirectry(basepath + 'dir')) # NG 

# print ftp.getAllFilesAndDirectries().walk # OK 
# print ftp.isFile('hogehoge/') # directry exits(not file) → OK
# print ftp.isFile(basepath + 'hogetext.txt') # not foubnd file → OK
# print ftp.isFile(basepath + 'dir.py') # file exits → OK
# print ftp.openFile('dir.py') # OK

# print ftp.uploadFile('dir.py') # NG

# print ftp.closeFile() # OK
# print ftp.quitFtp() # OK

