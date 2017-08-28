import json
'''
http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html#api-gateway-simple-proxy-for-lambda-input-format
{
    "resource": "Resource path",
    "path": "Path parameter",
    "httpMethod": "Incoming request's method name"
    "headers": {Incoming request headers}
    "queryStringParameters": {query string parameters }
    "pathParameters":  {path parameters}
    "stageVariables": {Applicable stage variables}
    "requestContext": {Request context, including authorizer-returned key-value pairs}
    "body": "A JSON string of the request payload."
    "isBase64Encoded": "A boolean flag to indicate if the applicable request payload is Base64-encode"
}
'''

'''
{
    "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headerName": "headerValue", ... },
    "body": "..."
}

'''

def response_proxy(data):
  response = {}
  response["isBase64Encoded"] = False
  response["statusCode"] = data["statusCode"]
  response["headers"] = {}
  if "headers" in data:
    response["headers"] = data["headers"]
  response["body"] = json.dumps(data["body"])
  return response

def request_proxy(data):
  request = {}
  request = data
  request["body"]=json.loads(data["body"])
  return request

def handler(event, context):
	response = {}
	try:
		request = request_proxy(event)
		response["statusCode"]=200
		response["headers"]={}
		'''
		data["headers"]["Access-Control-Allow-Methods"]="POST,OPTIONS"
		data["headers"]["Access-Control-Allow-Headers"]="Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
		data["headers"]["Access-Control-Allow-Origin"]="*"
		'''		
		response["body"]={}
	except:
		response["statusCode"]=500
		response["body"]={}		
		
	return response_proxy(data)