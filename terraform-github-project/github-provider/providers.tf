#provider "aws" {} //example

// bas itna sa likte ich wo automatically ek repo create kardega github par : command : terraform apply --auto-approve

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
    #version = "~> 4.0"
    token = "${var.github_token}"
}