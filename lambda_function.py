import json
tasks = []

def lambda_handler(event, context):
    path = event.get("resource")
    method = event.get("httpMethod")

    if path == "/health" and method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "API is healthy"})
        }

    if path == "/tasks" and method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps(tasks)
        }

    if path == "/tasks" and method == "POST":
        body = json.loads(event["body"])
        tasks.append(body)

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Task created"})
        }

    return {
        "statusCode": 404,
        "body": json.dumps({
            "path": path,
            "method": method,
            "message": "Not found"
        })
    }
