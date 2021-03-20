from fastapi.responses import JSONResponse, Response

def response_ok(data = {}, message = "OK"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=200)

def response_error(data = {}, message = "Unknown Error"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=400)

def response_not_found(data = {}, message = "Not Found"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=404)

def response_file(content, media_type = None):
    return Response(content=content, media_type=media_type)

def response_custom(data = {}, status_code = 400, message = "Error"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=status_code)