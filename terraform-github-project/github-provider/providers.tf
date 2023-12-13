#provider "aws" {} //example

// bas itna sa likte ich wo automatically ek repo create kardega github par : command : terraform apply --auto-approve
provider "github" {
    #version = "~> 5.0"
    token = "${var.github_token}"
}