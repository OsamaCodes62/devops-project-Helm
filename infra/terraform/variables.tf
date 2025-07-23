variable "aws_region" {
  description = "AWS region to deploy EKS cluster"
  type        = string
  default     = "ap-south-1" # change to your preferred region
}

variable "project_name" {
  description = "Project name prefix for resources"
  type        = string
  default     = "dubizzle-sample"
}
