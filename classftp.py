# -*- coding: utf-8 -*-
import os
import pdb
from ftplib import FTP
from setup.setup import *

class FtpUpload():

    # 対象のホストにアクセスしてログイン
    ftp = FTP(
        host,
        username,
        password
    )
    files = os.listdir(basepath)
    uploadPath = basepath + '/{}'.format(files)

    def echoPath(self):
        print basepath

    def nowDir(self):
        print self.ftp.dir()

    def isFile(self):
        if os.path.isfile(self.uploadPath):
            fh = open(self.files, 'rb')
            ftp.storbinary('STOR %s' % self.files, fh)
            fh.close()

    def isDir(self):
        if os.path.isdir(self.uploadPath):
            self.ftp.mkd(self.files)
            self.ftp.cwd(self.files)

    def FTPUpload(uploadFile,uploadDir):
        os.chdir(basepath)
        for f in self.files:
            print f
            return uploadFile(f)
            return UploadDir(f)

            #    ディレクトリ配下のファイル・ディレクトリもアップロード
            #    uploadInFTP(self.uploadPath)

    # FTPサーバとの切断
    def quit(self):
        self.ftp.quit

    #print uploadInFTP(getFiles)

ftpUpload = FtpUpload()
#ftpUpload.echoPath()
ftpUpload.isFile()
ftpUpload.isDir()
ftpUpload.FTPUpload(isFile,isDir)
#ftpUpload.nowDir()
ftpUpload.quit()

