# 네이버 만나이 계산기
      
### USE
- https://ojooon.store

### Ref
- https://docs.python.org/ko/3.10/library/datetime.html

### Dev
```bash
$ pyenv global
3.10.12

$ python -m venv venv
$ source venv/bin/activate
$ uvicorn api.index:app --reload
# $ deactivate
```

### Contributing
- scenario #1
```bash
# setting ssh
$ git clone <URL>
$ git branch <VER>/<NAME>
$ git checkout <VER>/<NAME>
$ git push
# make PR
# do someting
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# release & tag
```

- scenario #2
```bash
$ git branch -r
$ git checkout -t origin/<VER>/<NAME>
# do something
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# release & tag

```
