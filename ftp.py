# -*- coding: utf-8 -*-
import os
import pdb
from ftplib import FTP
from setup.setup import *

# 対象のホストにアクセスしてログイン
ftp = FTP(
    host,
    username,
    password
)

# サーバー上のカレントディレクトリの一覧を取得
print(os.getcwd())
myPath = basepath

def uploadDir(path):
    files = os.listdir(path)
    os.chdir(path)

    for f in files:
        # 対象のファイル・ディレクトリがなければ作成
        if os.path.isfile(path + r'/{}'.format(f)):
            fh = open(f, 'rb')
            ftp.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(path + r'/{}'.format(f)):
            ftp.mkd(f)
            ftp.cwd(f)
            # ディレクトリ配下のファイル・ディレクトリもアップロード
            uploadDir(path + r'/{}'.format(f))
    ftp.cwd('..')
    ftp.dir()
    os.chdir('..')

uploadDir(myPath)

# FTPサーバとの切断
ftp.quit()

