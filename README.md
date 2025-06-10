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

4. **Upload to S3**:
   ```bash
   cd ..
   pip3 install boto3
   python3 upload_to_s3.py
   ```
   - Ensure `upload_to_s3.py` is configured with your S3 bucket name and region.
   - This uploads the frontend to AWS S3, and your website will be ready via the CloudFront URL!

### Troubleshooting
- **NPM errors**: Ensure dependencies are installed (`npm install`).
- **Terraform errors**: Check AWS credentials and `terraform plan` output.
- **S3 upload errors**: Verify AWS CLI and script configuration (e.g., bucket name, region).

