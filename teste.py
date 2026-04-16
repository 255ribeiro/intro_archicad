from git import Repo
import toml

# Load the repository (current directory)
repo = Repo('.')

# Get the origin remote URL
remote_url = repo.remotes.origin.url  # e.g., git@github.com:user/repo.git or https://github.com/user/repo.git

# Normalize to HTTPS if SSH
if remote_url.startswith('git@'):
    remote_url = remote_url.replace('git@', 'https://').replace(':', '/')

# Ensure it ends with .git for consistency (optional)
if not remote_url.endswith('.git'):
    remote_url += '.git'

# Derive site_url (e.g., strip .git and use GitHub Pages or custom domain)
site_url = remote_url[:-4]  # Remove .git
# Example: for GitHub Pages: site_url = site_url.replace('https://github.com/', 'https://user.github.io/')

# Read zensical.toml
with open('zensical.toml', 'r') as f:
    config = toml.load(f)

# Update fields
config['project']['repo_url'] = remote_url
config['project']['site_url'] = site_url  # Adjust logic as needed

# Write back
with open('zensical.toml', 'w') as f:
    toml.dump(config, f)

print("zensical.toml updated with remote URLs.")