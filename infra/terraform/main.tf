resource "aws_kms_key" "artifacts" {
  description         = "Chiffrement du bucket d'artefacts"
  enable_key_rotation = true
}

resource "aws_s3_bucket" "artifacts" {
  #checkov:skip=CKV_AWS_18:Journalisation d'acces hors perimetre de cette demonstration
  #checkov:skip=CKV_AWS_144:Replication inter-regions inutile pour cette demonstration
  #checkov:skip=CKV2_AWS_62:Notifications d'evenements inutiles pour cette demonstration
  bucket = var.bucket_name
}

resource "aws_s3_bucket_public_access_block" "artifacts" {
  bucket                  = aws_s3_bucket.artifacts.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.artifacts.arn
    }
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  rule {
    id     = "nettoyage"
    status = "Enabled"

    filter {}

    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }

    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}
