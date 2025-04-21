# CreateEmptyQuickClaimProject.ps1

# Create main folder
New-Item -ItemType Directory -Path quickclaim_login_project -Force | Out-Null

# Create subfolders
New-Item -ItemType Directory -Path quickclaim_login_project\static -Force | Out-Null
New-Item -ItemType Directory -Path quickclaim_login_project\static\images -Force | Out-Null
New-Item -ItemType Directory -Path quickclaim_login_project\static\css -Force | Out-Null
New-Item -ItemType Directory -Path quickclaim_login_project\templates -Force | Out-Null

# Create empty files
New-Item -ItemType File -Path quickclaim_login_project\app.py -Force | Out-Null
New-Item -ItemType File -Path quickclaim_login_project\requirements.txt -Force | Out-Null
New-Item -ItemType File -Path quickclaim_login_project\static\images\logo.png -Force | Out-Null
New-Item -ItemType File -Path quickclaim_login_project\static\css\style.css -Force | Out-Null
New-Item -ItemType File -Path quickclaim_login_project\templates\index.html -Force | Out-Null

Write-Host "Empty project structure created."
