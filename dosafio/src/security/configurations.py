from bottle import BaseResponse, request
import src.helpers.enum.system_variables as sv

WHITE_LIST = {
    "local": [],
    "dev": [],
    "hom": [],
    "prd": []
}


def config_response_headers(response: BaseResponse) -> BaseResponse:
    enable_cors(response)
    return response


def enable_cors(resp: BaseResponse) -> BaseResponse:
    origin = request.get_header('origin')
    resp.headers['Access-Control-Allow-Origin'] = origin if origin in WHITE_LIST[sv.ENVIRONMENT.lower()] else 'null'
    resp.headers['Access-Control-Allow-Headers'] = 'Accept, Accept-Type, Authorization, Content-Type, Origin'
    resp.headers['Access-Control-Allow-Headers'] += 'accept, accept-type, authorization, content-type, origin'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS, POST'
    resp.headers['Vary'] = 'Origin'
    return resp
