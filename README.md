
# Static Website Hosting with CloudFront and S3

This project sets up a static website hosted on AWS S3 with a CloudFront distribution for fast, secure delivery.

## Quick Start

### Prerequisites

Ensure the following are installed on your system:

[![My Skills](https://skillicons.dev/icons?i=nodejs,npm,terraform,py,aws)](https://skillicons.dev)

- Node.js (v16 or later)
- npm (v8 or later)
- Terraform (v1.5 or later)
- Python 3 (v3.8 or later)
- AWS CLI (v2 or later)
- AWS account with configured credentials (e.g., run `aws configure` or set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`)

### Verify Installations

Check that all tools are installed correctly:

```bash
node -v
npm -v
terraform -v
python3 --version
aws --version
```

### Start the Application

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/Szebicc/s3-cloudfront-host.git
   cd <repository-root>
   ```

2. **Build the frontend**:
   ```bash
   cd cloudfront-s3-hosting/static-host
   npm install
   npm run build
   ```
   - This builds the static website files.

3. **Deploy AWS resources**:
   ```bash
   cd ../terraform
   terraform init
   terraform plan
   terraform apply
   ```
   - `terraform init`: Downloads providers and modules.
   - `terraform plan`: Previews AWS resources (e.g., S3 bucket, CloudFront distribution).
   - `terraform apply`: Creates resources; review the plan and confirm.

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

