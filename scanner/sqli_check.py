#!/usr/bin/env python
# encoding: utf-8
# mail: root@1137.me

import json
import sys
import base64
import os
from time import sleep
import re


from  req  import Req




global_sqlmap = "python D:\\sqlmap\\sqlmap.py"

global_options = " --batch  --smart "

global_notify = "--alert='python "+sys.path[0]+"/"+sys.argv[0]+" notify "

global_flag = "sqli_vul"



def sqliCheck(request, platform = None):
    reqObj = Req(request)
    if reqObj.method != "GET" and reqObj.method !=   "POST":
         return "Not Vul"
     #后缀删除
    ext = getExtByUri(reqObj.uri)
    if ext in ["gif","js","jpg","css","png","ico"]:        
        return "Not Vul"
     #无参数 filter
    if reqObj.method != "POST" and len(reqObj.url.split('=')) == 1:
        return "Not Vul"

  

    reqFile = req2file(reqObj.hash,request)
    notify = global_notify + reqFile + "\'"
    cmd = global_sqlmap+ " -r "+reqFile + global_options + notify
    outPut = os.popen(cmd)
    url=reqObj.url
    return     outPut.read(),url


def getExtByUri(uri):
    ext =  uri.split('?')[0].split('.')
    if len(ext) > 1 :
        return ext[-1]
    return None


def req2file(code, request):
    fileName =  "./"+code+".tmp"
    fh = file(fileName, "wb")
    fh.write(request)
    fh.close()
    return fileName





if __name__ == "__main__":

    if len(sys.argv) == 2:
        argv1 = base64.b64decode(sys.argv[1])  
        return_data,url=sqliCheck(argv1)
        if not (return_data.find("back-end DBMS:")==-1):
            result=re.findall("back-end DBMS:(.+)",return_data)
            print "SQLi Vul,DBMS is:",result,"url is ",url
        else:
            print "NOT VUL,url is ",url
    elif len(sys.argv) == 3:        
        fh = open(sys.argv[2],'rb')
        try:
            data = fh.read( )
        finally:
            fh.close( )
        reqObj = Req(data)
        target = reqObj.host
        vul_type = global_flag
        vul_detail ="SQLi Vul:\n"+data
        
        #print "VUL" if permissionCheck(reqStr) else "SAFE"

        sys.exit(0)
    else:
        print ("usage: %s base64(request)" % sys.argv[0])
        sys.exit(-1)
