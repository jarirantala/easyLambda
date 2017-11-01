# ekalambda

## AWS account

- Create an account http://docs.aws.amazon.com/lambda/latest/dg/setting-up.html
- Create access key IAM -> Users -> *käyttäjänimi* -> Security credentials
    - Add keys to ~/.aws/credentials (http://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html)


```
[jari] <- Profile found in serverless.yml
aws_access_key_id = ACCESS_KEY
aws_secret_access_key = SECRET_ACCESS_KEY
```

## Serverless Framework

*The Serverless Framework is a CLI tool that allows users to build & deploy auto-scaling, pay-per-execution, event-driven functions.*

Usage:
- *npm install -g serverless* (https://www.npmjs.com/get-npm)
- *serverless deploy* to deploy the application

https://serverless.com