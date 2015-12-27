# -*- coding: utf-8 -*-
from bottle import route, run, HTTPResponse, request, Bottle, response, static_file, auth_basic, template
import simplejson as json
import json
import datetime
from StringIO import StringIO
import classifier as c
import classifier_csv as cc
import pymongo
import urllib2
import copy
from bson.objectid import ObjectId
from bson import json_util

app = Bottle()
@app.route('/receiver', method="POST")
def receiver():
    content_type = request.get_header('Content-Type')
    if content_type  == 'audio/pcm' or content_type == "text/plain":
        #print request.body.read()
        pass
    else:
        return "Bad Content-Type"

    id = request.get_header('X-Voice-ID')
    speaker = "panda"
    print "ID=>"+str(id)
    dir = "/home/sw/dataset/"
    tdatetime = datetime.datetime.now()
    tstr = tdatetime.strftime('%Y%m%d%H%M%S')
    if content_type  == 'audio/pcm': #音源が与えられた場合
        target_path = "/".join([dir, "wav", speaker+tstr+str(id)+".pcm"])
        with open(target_path, mode = 'w') as fh:
            fh.write(str(request.body.read()))

        #活性度推定
        result = c.classify_by_file(target_path)
        body = json.dumps(result)
        r = HTTPResponse(status=200, body=body)
        r.set_header('Content-Type', 'application/json')
        return r
    elif content_type  == 'text/plain': #音声認識結果が与えられた場合
        target_path = "/".join([dir, "text", speaker+tstr+str(id)+".rcg"])
        with open(target_path, mode = 'w') as fh:
            fh.write(str(request.body.read()))
    return "OK\r\n"


@app.route('/saveWavPage', method="GET")
def saveWavPage():
    return static_file("index.html",root="/home/sugaya/public_html/Tpis_System")



@app.route('/saveWav', method=["OPTIONS","POST"])
def saveWav():
    #録音音声をSEND
    content_type = request.get_header('Content-Type')
    subjectid = request.get_header("subject-id")
    print content_type
    print subjectid
    dir = "/home/sw/wav/"
    tdatetime = datetime.datetime.now()
    tstr = tdatetime.strftime('%Y%m%d%H%M%S')
    target_path = dir+tstr+".wav"
    with open(target_path, mode = 'w') as fh:
        fh.write(str(request.body.read()))
        r = HTTPResponse(status=200, body="OK")
        r.set_header('Content-Type', 'text/plain')        
    print "saved "+target_path+" !!"
    
    #活性度推定
    feature_list, classification_result = cc.classify_by_file(target_path)
    result = {"feature_list": feature_list, "result": classification_result, "subject-id": subjectid}
    
    body = json.dumps(result)
    rr = HTTPResponse(status=200, body=body)
    rr.set_header('Content-Type', 'application/json')
    print result
    
    #MongoDBに特徴量・推定結果挿入
    result_for_mongo = copy.copy(result)
    con = pymongo.MongoClient()
    coll = con.test1.user
    post_id = coll.insert(result_for_mongo)
    print(post_id)

    #MongoDBから挿入したドキュメントを取得                                                                                   
    user_data = coll.find_one({"_id":ObjectId(post_id)})
    print user_data
    
    #ブラウザにjsonデータを返答
    return json.dumps(user_data, sort_keys=True, default=json_util.default)


@app.route('/subfomation', method=["OPTIONS","POST"])
def subfomation():
    print("subfomation")
    #JSONデータ取得
    json_data = json.loads(str(request.body.read()))
    print json_data
    #MongoDBに被験者番号・正誤判定挿入
    con = pymongo.MongoClient()
    coll = con.test1.user
    coll.insert_one(json_data)
    """
    for doc in coll.find():
        print(doc)
    """
run(app,host='0.0.0.0', port=5298, debug=True, reloader=True)
