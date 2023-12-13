resource "github_repository" "terraform-first-repo" {
  name        = "first-terraform-project"
  description = "My first-terraform-project to create this repo using teraform auomation"
  visibility = "public"
  auto_init = true
}