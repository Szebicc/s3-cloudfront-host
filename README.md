## Quick start

### Prerequisites

Ensure the following are installed on your system:

[![My Skills](https://skillicons.dev/icons?i=js,html,css,wasm)](https://skillicons.dev)


### Verify installations

   ```bash
   node -v
   npm -v
   ```
### Start the application 

    ```bash
    cd cloudfront\ s3\ hosting/static-host
    npm run build
    ```
   This will build the frontend.

    ```bash
    cd ../terraform
    terraform apply
    ```
    This will create the AWS resources.

    ```bash
    cd ..
    python3 upload_to_s3.py
    ```
    This will upload the frontend to the AWS and you will be ready to use the website.