# -*- coding:utf8 -*-
__author__ = 'hartnett'
from celery import Celery
#from arachni import arachni_console

from config import BACKEND_URL, BROKER_URL, db_info
from helper import Reporter, PassiveReport, TaskStatus
import subprocess


app = Celery('task', backend=BACKEND_URL, broker=BROKER_URL)

# scanning url task
# --------------------------------------------------------------------
@app.task
def scan_all(task_id, task_url,domain,method,request_data,user_agent,cookies):
    print 'scan_all'


@app.task
def scan_web(task_id, task_url,domain,method,request_data,user_agent,cookies):
    print 'scan_web'

@app.task
def sqli_dispath(taskid,request):
        # 命令执行环境参数配置
        #run_env = '{"LD_LIBRARY_PATH": "/home/liet/code/git/doom"}'

        if taskid == None:
                cmdline = 'python sqli_check.py %s' % (request)
        else:
                cmdline = 'python sqli_check.py %s' % (request)
        permission_proc = subprocess.Popen(cmdline,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        process_output = permission_proc.stdout.readlines()        
        return process_output