resource "github_repository" "terraform-public" {
  name        = "first-terraform-project"
  description = "My first-terraform-project to create this repo using teraform auomation for public"
  visibility = "public"
  auto_init = true
  //private = true
  #   pages {
  #   source {
  #     branch = "master"
  #     path   = "D:\\Vscode-All scripts\\All_in_one\\Python"
  #   }
  # }

}


resource "github_repository" "terraform-private" {
  name        = "second-terraform-project"
  description = "My second-terraform-project to create this repo using teraform auomation for private"
  visibility = "private"
  auto_init = true
  //private = true

}


resource "github_repository_file" "sendingdata" {
  repository          = github_repository.terraform-public.name
  branch              = "main"
  file                = "test.txt"
  content             = "Hello world, This file and repository created using terraform and public url  "
  commit_message      = "Managed by Terraform"
  commit_author       = "Terraform User"
  commit_email        = "terraform@example.com"
  overwrite_on_create = true
}