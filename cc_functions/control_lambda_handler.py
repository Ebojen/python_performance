"""Sample Event
{
      "resource": "/",
      "path": "/",
      "httpMethod": "GET",
      "requestContext": {
          "resourcePath": "/",
          "httpMethod": "GET",
          "path": "/Prod/",
          ...
      },
      "queryStringParameters": null,
      "multiValueQueryStringParameters": null,
      "pathParameters": null,
      "stageVariables": null,
      "body": null,
      "isBase64Encoded": false
  }
"""

def lambda_handler(event, _context):
    resource: str = event["resource"]
    if resource.startswith("customers"):
        pass
    if resource.startswith("orders"):
        pass
