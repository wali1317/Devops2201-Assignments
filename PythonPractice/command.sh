aws lambda create-function \
    --function-name request_demo \
    --runtime python3.9 \
    --zip-file fileb://output.zip \
    --handler lambda_function.lambda_handler\
    --role arn:aws:iam::928284401303:role/lambdaDemoRole


aws lambda update-function-code \
    --function-name  request_demo \
    --zip-file fileb://PythonPractice.zip

