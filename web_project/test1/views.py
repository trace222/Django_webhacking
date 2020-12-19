from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound,Http404
from .models import Boardlist #Candidate, Poll, Choice, Boardlist
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.shortcuts import render, redirect
from .form import PostForm
from .models import Post
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
from selenium.webdriver.chrome.options import Options
import requests
import re

def index(request):

    return render(request,'test1/index.html') 

def board(request):
    boardlist=Boardlist.objects.all()
    context={'boardlist' : boardlist}
    return render(request,'test1/board.html',context) 

def writeboard(request):
    
    return render(request,'test1/writeboard.html') 
@csrf_exempt
def writemanage(request):
    names=request.POST['names']
    introductions=request.POST['introductions']
    boardlist = Boardlist(name = names, introduction=introductions)
    boardlist.save()
    return HttpResponseRedirect("board")
@csrf_exempt
def deleteboard(request):
    names=request.POST['deletename']
    deleteunit=Boardlist.objects.get(name=names)
    deleteunit.delete()
    return HttpResponseRedirect("board")
    

# def results(request, user):
#     f = open(path,'a')
#     f.write(data)
#     f.close()

#     return render(request, 'test1/results.html', context)

def result(request):

    error_sql_list=open('./test1/file_folder/sql_folder/sql_injection_list.txt','r')
    blind_sql_list=open('./test1/file_folder/sql_folder/blind_sql_list.txt','r')
    timed_sql_list=open('./test1/file_folder/sql_folder/timed_sql_list.txt','r')
    directory_listing_list=open('./test1/file_folder/directory_listing/directory_listing_result.txt','r')
    error_page_list=open('./test1/file_folder/error_page/error_page_result.txt','r')
    file_download_list=open('./test1/file_folder/file_download/file_download_result.txt','r')
    file_upload_list=open('./test1/file_folder/file_upload/file_upload_result.txt','r')
    XSS_list=open('./test1/file_folder/XSS/XSS_result.txt','r')
    #blind_sqldatas=blind_sql_f.readlines()
    #for blind_sqldata in blind_sqldatas: 
    
    error_datalist=[]
    blind_datalist=[]
    timed_datalist=[]
    directory_datalist=[]
    errorpage_datalist=[]
    download_datalist=[]
    upload_datalist=[]
    XSS_datalist=[]

    i=0
    error_datalist.append("ErrorBased Injection")
    blind_datalist.append("BlindBased Injection")
    timed_datalist.append("TimedBased Injection")
    directory_datalist.append("Directory Listing")
    errorpage_datalist.append("Error Page")
    download_datalist.append("File Download")
    upload_datalist.append("File Upload")
    XSS_datalist.append("Cross-Site Script (XSS)")

    for data in error_sql_list:
        #data_1="/"+data_1
        data_1=(data.split(" ")[1])[:-1]
        error_datalist.append(data_1)
        i=i+1
    for data in blind_sql_list:
        #data_1="/"+data_1
        data_2=(data.split(" ")[1])[:-1]
        blind_datalist.append(data_2)
        i=i+1
    for data in timed_sql_list:
        #data_1="/"+data_1
        data_3=(data.split(" ")[1])[:-1]
        timed_datalist.append(data_3)
        i=i+1

    for data in directory_listing_list:
        #data_1="/"+data_1
        directory_datalist.append(data)
           
    for data in error_page_list:
        #data_1="/"+data_1
        errorpage_datalist.append(data)
        
    for data in file_download_list:
        #data_1="/"+data_1
        
        download_datalist.append(data)
        
    for data in file_upload_list:
        #data_1="/"+data_1
        data_3=(data.split(" ")[1])[:-1]
        upload_datalist.append(data_3)
        
    for data in XSS_list:
        #data_1="/"+data_1
        data_3=(data.split(" ")[1])[:-1]
        XSS_datalist.append(data_3)
        
    
    injetion_list=[]
    # injetion_list={'error_list':error_datalist,'blind_list':blind_datalist,'timed_list':timed_datalist}
    injetion_list.append(error_datalist)
    injetion_list.append(blind_datalist)
    injetion_list.append(timed_datalist)


    error_sql_list.close()
    blind_sql_list.close()
    timed_sql_list.close()
    directory_listing_list.close()
    error_page_list.close()
    file_download_list.close()
    file_upload_list.close()
    XSS_list.close()

    context={'sql_num':i,'injection_list':injetion_list,'directroy_num':len(directory_datalist),'directory_list':directory_datalist,'error_page_num':len(errorpage_datalist),'error_page_list':errorpage_datalist,'download_num':len(download_datalist),'download_list':download_datalist,'upload_num':len(upload_datalist),'upload_list':upload_datalist,'XSS_num':len(XSS_datalist),'XSS_list':XSS_datalist}
    return render(request,'test1/result.html',context) 

def solve(request):
    return render(request,'test1/solve.html') 
def UrlInput(request):
    return render(request,'test1/UrlInput.html') 
def login(request):
    return render(request,'test1/login.html') 
def crawling_result(request):
    
    i=0
    crawling_list=open('./test1/file_folder/list.txt','r')
    #blind_sqldatas=blind_sql_f.readlines()
    #for blind_sqldata in blind_sqldatas: 
    datalist=[]
    baseUrl=""
    for data in crawling_list:
        if i==0:
            baseUrl=data
            baseUrl=baseUrl[:-2]
        data_1=(data.split(baseUrl))[1]
        #data_1="/"+data_1
        datalist.append(data_1)
        i=i+1

        
    context={'crawling_list':datalist,'baseUrl':baseUrl}
    return render(request,'test1/crawling_result.html',context) 

################################################################
def write_file(path,data):
    f = open(path,'a')
    f.write(data)
    f.close()

def create_data_files(project_name):
    # queue=project_name+'queue.txt'
    # crawled="C:/django/folder/"+project_name+"(crawled.txt)"
    # if not os.path.isfile(queue):
    #     write_file(queue,base_url)
    crawled=project_name
    crawled2=crawled+"\n"
    if '&' in crawled or '%' in crawled:
        crawled3=re.split('[&%]',crawled)[0]
    else:
        crawled3=crawled+"\n"
    
    f = open("./test1/file_folder/list.txt",'r')
    # if not os.path.isfile(crawled):
    if not crawled3 in f.read():
        write_file("./test1/file_folder/list.txt",crawled2)
        f.close()
        return True
    else:
        f.close()
        return False
def get_subUrl(driver,baseUrl2,sub_url):
    driver.get(sub_url)
    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')

    try:
        alert = driver.switch_to_alert()
        alert.dismiss()
    except:
        pass
    for link in soup.select('a'):
        try:
            href=link.attrs['href']
            href,check_value=crawl_func(href,baseUrl2)
            if not check_value:
                continue

            get_subUrl(driver,baseUrl2,href)
        except:
            print("ERROR", href)


def crawl_func(href,baseUrl2):
        if "#" in href or "javascript:" in href:
 
            # #top
            # img src
            return href,False
        
        # if "?" in href:
        #     hrefs=href.split("?")
        #     href=hrefs[0]

        if "http://" in href or "https://" in href:
            if not (baseUrl2 in href) or (baseUrl2 in href):

                print("외부로 나감")
                return href,False
        else:
            if (href)[0:2]=="./":
                href=baseUrl2+(href)[1:]
            elif (href)[0]=="/":
                href=baseUrl2+(href)
            else:
                href=baseUrl2+"/"+(href)
            
        if not create_data_files(href):
            print("중복2")
            return href,False
        
        return href,True



###############################################################

def url_check(form,line,baseUrl2):
    try:
        if ("http://" in form.attrs['action']) or ("https://" in form.attrs['action']):
            action_url=form.attrs['action']
        else:
            if (form.attrs['action'])[0:2]=="./":
                action_url=baseUrl2+(form.attrs['action'])[1:]
            elif (form.attrs['action'])[0]=="/":
                action_url=baseUrl2+(form.attrs['action'])
            else:
                action_url=baseUrl2+"/"+(form.attrs['action'])

            # action_url=line+i.attrs['action']
        # elif i.attrs['action']=="":
        #     action_url=baseUrl2
        # else:
        #     action_url=baseUrl2+"/"+i.attrs['action']
    except:
        print("action이 없을경우")
        action_url=line

    return action_url


def timed_sql_vulnerable_check(form,action_url,method,arr,line):
    
    data = {}
    params = {}
    timed_sql_f=open('./test1/file_folder/sql_folder/timed_sql.txt','r')
    sqldatas=timed_sql_f.readlines()

    ##union sql은 그냥 여기 추가하면 되겄어
    for sqldata in sqldatas:

        ## url 의 대한 취약점, ㅂ퍼오버플로우 , sql 인젝션 없으면 리다이렉션 된다?
        start=time.time()
        if method=="POST":
            for data_1 in arr:
                # data[data_1]='valid'
                # data[data_1]="' or 1=1#"
                
                data[data_1]=sqldata
                break
                            
            res = requests.post(action_url, data=data)
        elif method=="GET":
            
            for params_1 in arr:
                params[params_1]=sqldata
                break     
            res = requests.get(action_url, params=params)
        else:
            print("post get 도 아닌데 여기왜들어왔니")
        end=time.time()-start

        if (end>0.1):          
            f = open('./test1/file_folder/sql_folder/timed_sql_list.txt','r')
                                
            try:
                aleady_data=form.attrs['action']+"), ("+','.join(arr)+")"
                if not aleady_data in f.read():
                    f.close()
                    f = open('./test1/file_folder/sql_folder/timed_sql_list.txt','a')
                    f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
            except:
                aleady_data="), ("+','.join(arr)+")"
                if not aleady_data in f.read():
                    f.close()
                    f = open('./test1/file_folder/sql_folder/timed_sql_list.txt','a')
                    f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
            f.close()
            break
        else:
            print("timed based 상태코드 : ",res.status_code)


    timed_sql_f.close()   

def blind_sql_vulnerable_check(form,action_url,method,line,arr,blind_arr):
    # 이거 되는지 확인 res.text가 soup의 인자로 들어갈수 있나,  일단 div태그만 이용해서 blind 테스트     
    # html = response.read().decode("utf-8")
    blind_data = {}
    blind_data2 = {}
    params = {}
    params2 = {}
    index=0
    blind_sql_f=open('./test1/file_folder/sql_folder/blind_sql.txt','r')
    blind_sqldatas=blind_sql_f.readlines()
    for blind_sqldata in blind_sqldatas: 
        index=0
        data1=blind_sqldata.split('||')[0]
        data2=blind_sqldata.split('||')[1]
        # print(data1,":",data2)
        if method=="POST":
            for data_1,value in zip(arr,blind_arr):
                
                #if value=="":
                #    continue
                if value=="blind_sql_name" or value=="":
                    # print("왜",data_1)
                    blind_data[data_1]=data1
                    blind_data2[data_1]=data2
                    # if data_1=="searchstring":
                    #     if line=="http://172.30.1.46/gmshop/board_list.php?boardIndex=6":
                    #         blind_data["search"]="name"
                    #         blind_data2["search"]="name"
                    #         index=1
                else:
                    blind_data[data_1]=value
                    blind_data2[data_1]=value

            # print("아녀",action_url)
            # print("아녀",blind_data)
            # print("아녀2",blind_data2)
            res = requests.post(action_url, data=blind_data)
            res2 = requests.post(action_url, data=blind_data2)
        elif method=="GET":
            
            for params_1,value in zip(arr,blind_arr):
                #if value=="":
                #    continue
                if value=="blind_sql_name"or value=="":
                    params[params_1]=data1  
                    params2[params_1]=data2 
                else:
                    params[params_1]=value
                    params2[params_1]=value
      
            res = requests.get(action_url, params=params)
            res2 = requests.get(action_url, params=params2)
        else:
            print("post get 도 아닌데 여기왜들어왔니")
        
        html_text=res.text
        html_text2=res2.text
        soup=BeautifulSoup(html_text,'html.parser')
        soup2=BeautifulSoup(html_text2,'html.parser')
        div_arr=soup.select('div')
        div_arr2=soup2.select('div')
        td_arr=soup.select('tr')
        td_arr2=soup2.select('tr')


        
        if (len(div_arr)!=len(div_arr2)) or (len(td_arr)!= len(td_arr2)):
                                
            f = open('./test1/file_folder/sql_folder/blind_sql_list.txt','r')
                                
            try:
                aleady_data=form.attrs['action']+"), ("+','.join(arr)+")"
                if not aleady_data in f.read():
                    f.close()
                    f = open('./test1/file_folder/sql_folder/blind_sql_list.txt','a')
                    f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
            except:
                aleady_data="), ("+','.join(arr)+")"
                if not aleady_data in f.read():
                    f.close()
                    f = open('./test1/file_folder/sql_folder/blind_sql_list.txt','a')
                    f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
            f.close()
            break
        else:
            print("블라인드 코드 : X")
            timed_sql_vulnerable_check(form,action_url,method,arr,line)


    blind_sql_f.close()

def sql_vulnerable_check(form,action_url,method,line,arr,blind_arr):
    data = {}
    params = {}
    check_num=0
    check_Errorbased=["mysql","warning:","maria","aurora","postgre","sqlserver","oracle","ms-sql","mssql","sqlite","SELECT statements"]
    #sql 버전
    sql_f=open('./test1/file_folder/sql_folder/sql_injection.txt','r')
    sqldatas=sql_f.readlines()

    ##union sql은 그냥 여기 추가하면 되겄어
    
    for sqldata in sqldatas:
        check_num=0
        ## url 의 대한 취약점, ㅂ퍼오버플로우 , sql 인젝션 없으면 리다이렉션 된다?
        if method=="POST":
            for data_1 in arr:
                # data[data_1]='valid'
                # data[data_1]="' or 1=1#"
                
                data[data_1]=sqldata
                            
            res = requests.post(action_url, data=data)
        elif method=="GET":
            
            for params_1 in arr:
                params[params_1]=sqldata          
            res = requests.get(action_url, params=params)
        else:
            print("post get 도 아닌데 여기왜들어왔니")

        # 에러 베이스 
        html_text=res.text
        
        for check_sentense in check_Errorbased:

            if check_sentense in (html_text.lower()):
                check_num=1

 
        if (res.status_code>=400 or check_num==1):
                                
            f = open('./test1/file_folder/sql_folder/sql_injection_list.txt','r')
                                
            try:
                aleady_data=form.attrs['action']+"), ("+','.join(arr)+")"
                if not aleady_data in f.read():
                    f.close()
                    f = open('./test1/file_folder/sql_folder/sql_injection_list.txt','a')
                    f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
            except:
                aleady_data="), ("+','.join(arr)+")"
                if not aleady_data in f.read():
                    f.close()
                    f = open('./test1/file_folder/sql_folder/sql_injection_list.txt','a')
                    f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
            f.close()
            break
        else:
            print("error based 상태코드 : ",res.status_code)
            blind_sql_vulnerable_check(form,action_url,method,line,arr,blind_arr)


    sql_f.close()   


def file_upload_check(form,action_url,method,line,arr,upload_arr,value_arr):
    # 이거 되는지 확인 res.text가 soup의 인자로 들어갈수 있나,  일단 div태그만 이용해서 blind 테스트     
    # html = response.read().decode("utf-8")
    upload_data = {}
    upload_error_check=0

    file_upload_f=open('./test1/file_folder/file_upload/file_upload_list.txt','r')
    upload_lists=file_upload_f.readlines()
    
    for upload_list in upload_lists: 
        index=0
        upload_error_check=0
        
        if method=="POST":
            for data_1,value in zip(arr,value_arr):
                if data_1 in upload_arr:
                    upload_data[data_1]=upload_list
                else:
                    upload_data[data_1]=value
            try:
                res = requests.post(action_url, data=upload_data)
                if res.status_code<400:
                    upload_error_check=1
                    break
                    print("kwon_2")
            except:
                print("kwon!")
                upload_error_check=1
        elif method=="GET":
            for params_1,value in zip(arr,value_arr):
                if params_1 in upload_arr:
                    upload_data[params_1]=upload_list
                else:
                    upload_data[params_1]=value
            try:
                res = requests.get(action_url, params=upload_data)
                if res.status_code<400:
                    print("kwon_3")
                    upload_error_check=1
                    break
            except:
                print("kwon!!")
                upload_error_check=1
        else:
            print("post get 도 아닌데 여기왜들어왔니")
        


    if upload_error_check==1:
        
        f = open('./test1/file_folder/file_upload/file_upload_result.txt','r')                 
        try:
            aleady_data=form.attrs['action']+"), ("+','.join(arr)+")"
            if not aleady_data in f.read():
                f.close()
                f = open('./test1/file_folder/file_upload/file_upload_result.txt','a')
                f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
        except:
            aleady_data="), ("+','.join(arr)+")"
            if not aleady_data in f.read():
                f.close()
                f = open('./test1/file_folder/file_upload/file_upload_result.txt','a')
                f.write(line+" ("+action_url+"), ("+','.join(arr)+")\n")
        f.close()

    file_upload_f.close()

def XSS_check(driver,action_url,name_arr,line):
    # 이거 되는지 확인 res.text가 soup의 인자로 들어갈수 있나,  일단 div태그만 이용해서 blind 테스트     
    # html = response.read().decode("utf-8")
    XSS_data = {}
    XSS_check=0

    for name_data in name_arr:
        f = open('./test1/file_folder/XSS/XSS_check_list.txt','r')                 
        aleady_data=action_url+", ("+name_data+")"
        if not aleady_data in f.read():
            f.close()
            f = open('./test1/file_folder/XSS/XSS_check_list.txt','a')
            f.write(action_url+", ("+name_data+")\n")
            f.close()

            file_XSS_f=open('./test1/file_folder/XSS/XSS_list.txt','r')
            XSS_lists=file_XSS_f.readlines()
            for XSS_list in XSS_lists:
                try:
                    elem=driver.find_element_by_name(name_data)
                    elem.send_keys(XSS_list)
                    elem.submit()
                except:
                    break
                try:
                    alert = driver.switch_to_alert()
                    alert.accept()
                    f2 = open('./test1/file_folder/XSS/XSS_result.txt','r')
                    aleady_data2=action_url+", ("+name_data+")"
                    if not aleady_data2 in f2.read():
                        f2.close()
                        f = open('./test1/file_folder/XSS/XSS_result.txt','a')
                        f.write(action_url+", ("+name_data+")\n")
                        f.close()
                except:
                    pass
            file_XSS_f.close()
        else:
            f.close()

            

def file_download_check(line,baseurl):
    
    download_url=""
    
    ##파일다운로드시 200인가?
    file_download_f=open('./test1/file_folder/file_download/file_download_list.txt','r')
    download_lists=file_download_f.readlines()
    for download_list in download_lists:
        i=0
        url_split=line.split('/')
        download_url=""
        while (i<len(url_split)-1):
            download_url=download_url+url_split[i]+'/'
            i=i+1
        download_url=download_url+download_list
        res = requests.get(download_url)
        if (res.status_code<300): #(res.status_code==403) 에러페이지 취약점
            f = open('./test1/file_folder/file_download/file_download_result.txt','a')
            f.write(download_url+"\n")
            f.close()
    file_download_f.close()

def error_page_check(line,baseurl):
    
    errorpage_url=""
    check_Errorpage=["mysql","warning:","maria","aurora","postgre","sqlserver","oracle","ms-sql","mssql","sqlite","SELECT statements","Apache","Ubuntu","mod_fastcgi","PHP","mod_ssl","OpenSSL","Port"]
    ##파일다운로드시 200인가?
    file_errorpage_f=open('./test1/file_folder/error_page/error_page_list.txt','rt',encoding='UTF8')
    errorpage_lists=file_errorpage_f.readlines()
    for errorpage_list in errorpage_lists:
        i=0
        url_split=line.split('/')
        errorpage_url=""
        while (i<len(url_split)-1):
            errorpage_url=errorpage_url+url_split[i]+'/'
            i=i+1
        errorpage_url=errorpage_url+errorpage_list
        res = requests.get(errorpage_url)
        if (res.status_code>400): #(res.status_code==403) 에러페이지 취약점

            html_text=res.text

            for check_sentense in check_Errorpage:
                if check_sentense in (html_text.lower()):
                    f2 = open('./test1/file_folder/error_page/error_page_result.txt','r')
                    aleady_data=errorpage_url
                    if not aleady_data in f2.read():
                        f2.close()
                        f = open('./test1/file_folder/error_page/error_page_result.txt','a')
                        f.write(errorpage_url+"\n")
                        f.close()
                        break


    file_errorpage_f.close()

def Directory_listing_check(line,baseurl):
    Directory_url=""
    check_Directory_listing=["Index of","parent directory","last modified"]

    ##파일다운로드시 200인가?
    file_Directory_f=open('./test1/file_folder/directory_listing/directory_listing_list.txt','r')
    Directory_lists=file_Directory_f.readlines()
    for Directory_list in Directory_lists:
        i=0
        url_split=line.split('/')
        Directory_url=""
        while (i<len(url_split)-1):
            Directory_url=Directory_url+url_split[i]+'/'
            i=i+1
        Directory_url2=Directory_url
        Directory_url=Directory_url+Directory_list[:-1]
        res = requests.get(Directory_url)
        
        if (res.status_code<300): #(res.status_code==403) 에러페이지 취약점

            html_text=res.text
            
            for check_sentense in check_Directory_listing:
                if check_sentense in (html_text.lower()):
                    f2 = open('./test1/file_folder/directory_listing/directory_listing_result.txt','r')
                    aleady_data=Directory_url
                    if not aleady_data in f2.read():
                        f2.close()
                        f = open('./test1/file_folder/directory_listing/directory_listing_result.txt','a')
                        f.write(Directory_url+"\n")
                        f.close()
                        break
        else:
            res2 = requests.get(Directory_url2)
            if (res2.status_code<300): #(res.status_code==403) 에러페이지 취약점

                html_text=res2.text
                for check_sentense in check_Directory_listing:
                    if check_sentense in (html_text.lower()):
                        f2 = open('./test1/file_folder/directory_listing/directory_listing_result.txt','r')
                        aleady_data=Directory_url2
                        if not aleady_data in f2.read():
                            f2.close()
                            f = open('./test1/file_folder/directory_listing/directory_listing_result.txt','a')
                            f.write(Directory_url2+"\n")
                            f.close()
                            break



    file_Directory_f.close()

def input_vulnerable_check(driver,line,baseUrl2,r1):
        for form in r1:
                
                arr=[]
                value_arr=[]
                upload_arr=[]
                name_arr=[]
                #blind_value_arr=[]
                    #submit reset 형식 에러처리
                for s in form.select('input'):
                    try:
                        arr.append(s.attrs['name'])
                        try:
                            if s.attrs['type']=='text':
                                value_arr.append("value_name")
                                name_arr.append(s.attrs['name'])
                            elif s.attrs['type']=='file':
                                upload_arr.append(s.attrs['name'])
                            else:
                                value_arr.append(s.attrs['value'])
                        except:
                            value_arr.append("")
                        


                        # print("n2 = ", s.attrs['name'])
                    except:
                        pass
                        # print("n2 = ", s.attrs['type'])
                for s in form.select('select'):
                    for s2 in s.select('option'):

                        try:
                            arr.append(s.attrs['name'])
                            value_arr.append(s2.attrs['value'])
                            break
                            # print("n2 = ", s.attrs['name'])
                        except:
                            pass
                            # print("n2 = ", s.attrs['type'])
                try:

                    # post방식 get방식 나눔
                    if form.attrs['method']=="post" or form.attrs['method']=="POST":
                        action_url=url_check(form,line,baseUrl2)
                        sql_vulnerable_check(form,action_url,"POST",line,arr,value_arr)
                        if(len(upload_arr)>0):
                            print("kwon!!")
                            file_upload_check(form,action_url,"POST",line,arr,upload_arr,value_arr)
                        
                    elif form.attrs['method']=="get" or form.attrs['method']=="GET":
                         # /result 경우나, ? 경우 "" 경우는 이걸로 퉁치는데 afreeca.co.kr 이런식으로 되있는경우가 있거나, result.php /없는경우 있으면 수정필요 
                        action_url=url_check(form,line,baseUrl2)
                        sql_vulnerable_check(form,action_url,"GET",line,arr,value_arr)
                        if(len(upload_arr)>0):
                            print("kwon!!")
                            file_upload_check(form,action_url,"GET",line,arr,upload_arr,value_arr)
                    else:
                        print("TRACE 취약점")
                    error_page_check(line,baseUrl2)
                    Directory_listing_check(line,baseUrl2)
                    file_download_check(line,baseUrl2)
                    XSS_check(driver,action_url,name_arr,line)
                except:
                    print("default 설정")

                    action_url=url_check(form,line,baseUrl2)
                    sql_vulnerable_check(form,action_url,"GET",line,arr,value_arr)  
                    file_upload_check(form,action_url,"GET",line,arr,upload_arr,value_arr)
                    error_page_check(line,baseUrl2)
                    Directory_listing_check(line,baseUrl2)
                    file_download_check(line,baseUrl2)
                    XSS_check(driver,action_url,name_arr,line)      
                # print("ERROR", i.attrs['type'])




@csrf_exempt
def vulnervle_main(request):
    #baseUrl2="http://172.30.1.46/gmshop"
    #baseUrl2="http://127.0.0.1:8000"
    baseUrl2 = request.POST.get('url_data','')##????????????????????????????????????????????이거 안될텐데
    options = Options()
    options.headless = True
    
    driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe",options=options)
    driver.get(baseUrl2)
    
    try:
        alert = driver.switch_to_alert()
        alert.dismiss()
    except:
        pass
    time.sleep(1)

    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    r=soup.select('a')
    create_data_files(baseUrl2+"/")

    img_r=soup.select('img')
    #-----------------------crawling
    for i in r:

        try:
            href=i.attrs['href']
            href,check_value=crawl_func(href,baseUrl2)
            if not check_value:
                continue
            get_subUrl(driver,baseUrl2,href)
        except:
            print("ERROR2", href)
    for i in img_r:

        try:
            href=i.attrs['src']
            href,check_value=crawl_func(href,baseUrl2)
            if not check_value:
                continue
            get_subUrl(driver,baseUrl2,href)
        except:
            print("ERROR2", href)
    f = open('./test1/file_folder/list.txt')
    lines=f.readlines()

    #-----------------------input check
    for line in lines:
        line=line[:-1]
        driver.get(line)
        while 1:
            try:
                # WebDriverWait(driver, 0.01).until(EC.alert_is_present(),
                #                        'Timed out waiting for PA creation ' +
                #                        'confirmation popup to appear.')
                alert = driver.switch_to_alert()
                alert.accept()
                
                #print('alert')
            except:
                break
        
        html=driver.page_source
        soup=BeautifulSoup(html,'lxml')
        

        # 여기가 폼- input 점검
        r1=soup.select('form')
        input_vulnerable_check(driver,line,baseUrl2,r1)
        file_download_check(line,baseUrl2)

    return render(request,'test1/index.html')
    # HttpResponseRedirect("/areas/{}/results".format(poll.area)) 

################################################################

