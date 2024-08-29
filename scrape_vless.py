name: Scrape VLESS Info

on:
  schedule:
    - cron: "0 * * * *"  # 每小时运行一次
  workflow_dispatch: # 手动触发

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository content
      uses: actions/checkout@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}

    - name: Set up Python
      uses: actions/setup-python@v4

    - name: Install dependencies
      run: |
        pip install requests

    - name: Run scrape script
      run: |
        python scrape_vless.py

    - name: Commit and push changes
      run: |
        git config --local user.email "actions@github.com"
        git config --local user.name "GitHub Actions"
        git add v2rayN_subscription.txt
        git commit -m "Update v2rayN_subscription.txt"
        git push origin HEAD:main
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
