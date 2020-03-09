# -*- coding: utf-8 -*-
import os
import pdb
# ftpモジュールを読み込む
from ftplib import FTP
from setup.setup import *

class FtpUpload:

    # 他の関数でも使いたいものをクラス変数化
    ftp = FTP(host,username,password) # 対象のホストにアクセスしてログイン
    files = os.listdir(basepath)
 
    # サーバー上のカレントディレクトリの一覧を取得
    def nowDir(self):
        print self.ftp.dir()

    # 対象のファイル・ディレクトリがなければ作成
    def uploadDir(self):
        for f in self.files:
            file = f
            #print file
            def isDir(file):
                print os.path.isdir(basepath + '/{}'.format(file))

                return isDir(file)
                def mkd(self):
                    self.ftp.mkd(f)
                    self.ftp.cwd(f)
                    print self.ftp.dir()
                    # ディレクトリ配下のファイル・ディレクトリもアップロード
                    #uploadDir(basepath + '/{}'.format(f))
#            elif os.path.isfile(basepath + '/{}'.format(f)):
#        #        fh = open(f, 'rb')
#        #        self.ftp.storbinary('STOR %s' % f, fh)
#        #        fh.close()
#        self.ftp.dir()
        
    # 対象のディレクトリに移動
    # ファイルを転送する

    # FTPサーバとの切断
    def quit(self):
        self.ftp.quit


# メソッドチェーンで呼び出す
ftp = FtpUpload()

# カレントディレクトリの一覧を表示
#ftp.nowDir()

# 対象のディレクトリがなければ作成
# 1. 対象のディレクトリを確認
#ftp.isDir()
# 2. 対象のディレクトリを作成(アップロード)
ftp.uploadDir()

# FTPサーバとの切断
ftp.quit()

