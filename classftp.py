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

# class化
class ftpUpload():

    # サーバー上のカレントディレクトリの一覧を取得
    print(os.getcwd())
    myPath = basepath

# FTPサーバとの切断
ftp.quit()

