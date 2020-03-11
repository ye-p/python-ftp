# -*- coding: utf-8 -*-
import os
import pdb
# ftpモジュールを読み込む
from ftplib import FTP
from setup.setup import *

class FtpUpload:

    # 対象のホストにログイン
    # サーバー上のカレントディレクトリの一覧を取得
    # 取得したものがディレクトリである
    # サーバーにディレクトリを作成
    # 未処理のファイル・ディレクトリが存在する
    # サーバー上のカレントディレクトリの一覧を取得
    # 取得したものがファイルである
    # サーバーにファイルをアップロード
    # 未処理のファイル・ディレクトリが存在する
    # FTPサーバとの切断

