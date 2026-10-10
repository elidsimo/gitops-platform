variable "aws_region" {
  description = "Région AWS"
  type        = string
  default     = "eu-west-1"
}

variable "bucket_name" {
  description = "Nom du bucket S3 (unique mondialement)"
  type        = string
  default     = "gitops-platform-artifacts-demo"
}
