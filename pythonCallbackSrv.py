import falcon
import json


class DefaultResource(object):

    def on_get(self, req, resp):
        """ / endpoint """
        resp.status = falcon.HTTP_200
        resp.body = ('\n Hello \n')


class simpleCallBack(object):

    def echo(self, fromNumber, msg):
        body = "User Callback [%s, %s]" % (fromNumber, msg)
        dictJson = dict()
        dictJson['from'] = fromNumber
        dictJson['msg'] = body
        result = json.JSONEncoder().encode(dictJson)
        return result

    #llamada post
    def on_post(self, req, resp):
        tmp = req.stream.read().decode('utf-8')  #decodificar utf8
        data = None
        try:
            data = json.loads(tmp)  #cargar json
        except Exception, ex:
            print ex.message

        telFrom = ''
        msg = ''
        valsOk = False
        try:
            telFrom = data['from']  # desde que numero
            msg = data['msg']  # mensaje
            valsOk = True
        except Exception, ex:
            valsOk = False
            print "Error: ", ex.message

        resp.status = falcon.HTTP_200
        result = "{}"
        if valsOk:
            result = self.echo(telFrom, msg)

        resp.body = (result)


wsgi_app = api  = falcon.API()
default = DefaultResource()
callBack = simpleCallBack()
#definir endPoints
api.add_route('/', default)
api.add_route('/whats', callBack)


