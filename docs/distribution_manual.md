# Distribution Manual

This document is for xLaDe maintainers and those who want to distribute their own projects along multiple repos.
This manual covers:

- Gitlab
- Codeberg
- Bitbucket
- Gitea

via Github as canonical.

Manual pushing can also be done through git locally as an alternative

## Procedure

First import the repository and create it. All of the above four git hosters allow importing repo. So, you can import. However, an empty repo is also fine since copying will be eventually done

Part A - Get the tokens

### Gitlab 

1. Go to Gitlab 
2. Go to repository
3. Settings (left)
4. Access tokens
5. Add new token
6. Fill the details and scope, permissions, etc
7. Copy it safely

Note: The address link may look like this 
`https://gitlab.com/<username>/<repo_name>/-/settings/access-tokens`

Example: "https://gitlab.com/lakshitsinghbishttm/xLaDe/-/settings/access_tokens"

### Codeberg

1. Go to Codeberg
2. Click on profile (top right)
3. Click on settings
4. Click on applications
5. Go to access tokens and create it
6. Fill the details and scope, permissions, etc
7. Copy it safely

Note: The address link may look like this
`https://codeberg.org/user/settings/applications`

### Bitbucket

1. Go to Bitbucket
2. Click on repository
3. Click on settings (left)
4. Click on three dots right side of repo name
5. Click on settings
6. Click on security
7. Click on access tokens
8. Fill the details and scope, permissions, etc
9. Copy it safely

Note: The address link may look like this
`https://bitbucket.org/<username>/<repo_name>/admin/access-tokens` 

Example: "https://bitbucket.org/lakshitsinghbishttm/xLaDe/admin/access-tokens"

### Gitea

1. Go to Gitea
2. Click on profile (top right)
3. Click on settings
4. Click on applications
5. Go to access tokens and create it
6. Fill the details and scope, permissions, etc
7. Copy it safely

Note: The address link may look like this
`https://gitea.com/user/settings/applications`

### Notes

1. Codeberg and Gitea work the same way here in access tokens.
2. Note the expiry of tokens so that you can replace in time.
3. This doc was created on June, 2026. I am not responsible if sites change the position in future.
4. Name the tokens something so that you can recall what it is in future.

---

Part B - Paste in GitHub

1. Go to Github
2. Go to repository
3. Click on settings
4. Go to secrets and variables
5. Click on actions
6. Click on New repository secret
7. Add all these tokens there and name it according to convenience
8. Write the token name of step7 in github workflow file

Done :)
Try a push and see auto sync.

---

### Zenodo

1. Go to zenodo
2. Click on three horizontal bars
3. Click on github
4. Click sync now
5. Create release on Github
6. Get the badge for every release automatically

### Onion Website

Manual
Each release


### Torrent

Manual 
Each release

1. Release the new version
2. Github creates tar.gz automatically
3. Download it
4. Go to bittorrent
5. Go to tools
6. Torrent creator
7. Select that file
8. Torrent created and then seed