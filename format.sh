find . -type f -name "*.py" ! -path "./.git/*" ! -path "./utils/__pycache__/*" -exec black {} \;