provider "aws" {
  region = var.aws_region
}

#Centralizar o aqruivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-fernando-105396593195"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}