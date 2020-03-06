# -*- coding: utf-8 -*-
import os
import pdb
from ftplib import FTP
from setup.setup import *

# class化
class FtpUpload():

    # 対象のホストにアクセスしてログイン
    ftp = FTP(
        host,
        username,
        password
    )
    myPath = basepath

    # サーバー上のカレントディレクトリの一覧を取得
    # print(os.getcwd())

    def echoPath(self):
        print self.myPath

    def nowDir(self):
        print self.ftp.dir()

    def uploadInFTP(self):
        files = os.listdir(self.myPath)
        os.chdir(self.myPath)

        for f in files:
            # 対象のファイル・ディレクトリがなければ作成
           if os.path.isfile(self.myPath + r'/{}'.format(f)):
               fh = open(f, 'rb')
               self.ftp.storbinary('STOR %s' % f, fh)
               fh.close()
           elif os.path.isdir(self.myPath + r'/{}'.format(f)):
               self.ftp.mkd(f)
               self.ftp.cwd(f)
               # ディレクトリ配下のファイル・ディレクトリもアップロード
               uploadInFTP(self.myPath + r'/{}'.format(f))
        self.ftp.cwd('..')
        self.ftp.dir()
        os.chdir('..')

        #uploadInFTP(self.myPath)

    # FTPサーバとの切断
    def quit(self):
        self.ftp.quit

ftpUpload = FtpUpload()
ftpUpload.echoPath()
ftpUpload.uploadInFTP()
ftpUpload.nowDir()
ftpUpload.quit()

