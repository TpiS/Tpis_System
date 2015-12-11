# -*- coding: utf-8 -*-
from bottle import route, run, HTTPResponse, request, Bottle, response, static_file, auth_basic, template
import simplejson as json
import json
import datetime
from StringIO import StringIO
import classifier_csv as c
import pymongo
import urllib2


app = Bottle()
@app.route('/receiver2', method="POST")
def receiver():
    content_type = request.get_header('Content-Type')
    if content_type  == 'audio/wav' or content_type == "text/plain":
#        print request.body.read()
        pass
    else:
        return "Bad Content-Type"

    id = request.get_header('X-Voice-ID')
    #speaker = "panda"
    print "ID=>"+str(id)
    dir = "/home/sugaya/public_html/wav/"
    tdatetime = datetime.datetime.now()
    tstr = tdatetime.strftime('%Y%m%d%H%M%S')



    if content_type  == 'audio/wav': #音源が与えられた場合
        target_path = "/".join([dir+"20151013223903.wav"])
        print target_path
        """
        with open(target_path, mode = 'w') as fh:
            fh.write(str(request.body.read()))
        """
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
    content_type = request.get_header('Content-Type')
    print content_type
    dir = "/home/sw/wav/"
    tdatetime = datetime.datetime.now()
    tstr = tdatetime.strftime('%Y%m%d%H%M%S')
    target_path = dir+tstr+".wav"
    with open(target_path, mode = 'w') as fh:
        fh.write(str(request.body.read()))
        r = HTTPResponse(status=200, body="OK")
        r.set_header('Content-Type', 'text/plain')
        return r
    print "saved "+target_path+" !!"



@app.route('/subfomation', method=["OPTIONS","POST"])
def subfomation():
    print("subfomation")
    
    if request.is_ajax:
        """
        print(JSON.stringify(request.json))
        """

        json_data = json.loads(JSON.stringify(JSONdata))
        print json_data

    con = pymongo.MongoClient()
    coll = con.test1.user

    docs = [{"_id" : 5, "foo" : "Bye"}, {"_id" : 6, "Blah" : "Blue"}]

    for doc in docs:
        coll.save(doc)

run(app,host='0.0.0.0', port=9990, debug=True, reloader=True)
