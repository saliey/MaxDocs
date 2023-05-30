


# windows 默认配置

不配置的话每次都要在 mingw64 中手动配置

在 `.bash_profile` 添加 
```
# Start SSH agent and add SSH key
eval $(ssh-agent)
ssh-add ~/.ssh/win_key
```

# 启动代理

eval "$(ssh-agent)"

# 添加 ssh key

ssh-add -l

ssh-add ~/.ssh/id_rsa

# 项目拉取

**要通过 git 拉取；通过 https 拉取的项目无法提交。**
git clone git@github.com:saliey/MaxDocs.git

# 项目配置

git config --local credential.helper store
git config --local credential.https://github.com.saliey ghp_xxx

# 项目提交

git push

# 说明

1. ghp_xxx 是 github 下 `Settings / Developer settings / Personal access tokens` 生成的 token 
2. 还需要在 `SSH keys` 的 `New SSH Key` 添加公钥信息，直接拷进去
3. 公钥的生成方法 `ssh-keygen -t ed25519 -C "your_email@example.com"` ，文件为 `.pub` 结尾
4. 在 linux 下 pri_key 权限可能太高，改为 `chmod 600 ~/.ssh/id_rsa`



