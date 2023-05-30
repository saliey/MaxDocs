

# 启动代理

eval "$(ssh-agent)"

# 添加 ssh key

ssh-add -l

ssh-add ~/.ssh/id_rsa

# 项目拉取

git clone git@github.com:saliey/MaxDocs.git

# 项目配置

git config --local credential.helper store

git config --local credential.https://github.com.saliey ghp_xxx

# 项目提交

git push



