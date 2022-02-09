import gitlab
import private

gitlab_url = "https://gitlab.cs.ttu.ee/"
token = private.general
server_repo_id = private.server_repo_id
client_repo_id = private.client_repo_id

gl = gitlab.Gitlab(url=gitlab_url, private_token=token)

# server project
server_project = gl.projects.get(id=server_repo_id)
server_issues = server_project.issues.list()

# client project
client_project = gl.projects.get(id=client_repo_id)
client_issues = client_project.issues.list()

print(server_project.issues.list())
