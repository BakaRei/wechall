__author__ = 'rei'
#coding:utf-8
#solution for  Coding->Programming 1
import httplib


def get_str():

    host = "www.wechall.net"
    login_cookie = "WC=8465216-14554-sU0s3gVFn6N9894S"  # wechall login cookie
    request_url = "http://www.wechall.net/challenge/training/programming1/index.php?action=request"
    header_data = {"Host": "www.wechall.net", "Cookie": login_cookie}

    conn = httplib.HTTPConnection(host=host)
    conn.request(method="GET", url=request_url, headers=header_data)

    print "connect to %s" % request_url

    response = conn.getresponse()
    result = response.read()
    print "code is: %s" % result

    request_url = "http://www.wechall.net/challenge/training/programming1/index.php?answer=%s" % result
    conn.request(method="GET", url=request_url, headers=header_data)

    print "connect to %s" % request_url

    response = conn.getresponse()
    result = response.read()
    conn.close()

    print result

if __name__ == "__main__":
    get_str()