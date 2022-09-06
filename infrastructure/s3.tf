resource "aws_s3_bucket" "myDatalake" {
  bucket = "${var.base_bucket_name}-${var.env}-${var.account_num}"
  acl    = "private"
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    IES   = "IGTI"
    CURSO = "EDC"
  }
}