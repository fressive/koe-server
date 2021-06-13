from fastapi.responses import JSONResponse, Response, StreamingResponse

def response_ok(data = {}, message = "OK"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=200)

def response_error(data = {}, message = "Unknown Error"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=400)

def response_not_found(data = {}, message = "Not Found"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=404)

def response_file(content, extension = None, media_type = None, content_length = -1):
    return StreamingResponse(content=content, media_type=media_type, headers={
        "Content-Length": str(content_length),
        "Content-Extension": extension,
    })

def response_file_headers(extension = None, media_type = None, content_length = -1):
    return Response(media_type=media_type, headers={
        "Content-Length": str(content_length),
        "Content-Extension": extension,
    })

def response_custom(data = {}, status_code = 400, message = "Error"):
    return JSONResponse(content={ "message" : message, "data": data }, status_code=status_code)