output "cloudfront_domain" {
  value = aws_cloudfront_distribution.static_site_distribution.domain_name
  description = "Output the CloudFront Domain"
}

output "bucket_name" {
  value = aws_s3_bucket.static_site.bucket
  description = "Output the S3 Bucket Name"
}