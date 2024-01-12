resource "github_repository" "terraform-public" {
  name        = "first-terraform-project"
  description = "My first-terraform-project to create this repo using teraform auomation for public"
  visibility = "public"
  auto_init = true
  //private = true

}

# resource "github_repository" "terraform-private" {
#   name        = "second-terraform-project"
#   description = "My second-terraform-project to create this repo using teraform auomation for private"
#   visibility = "private"
#   auto_init = true
#   //private = true

# }