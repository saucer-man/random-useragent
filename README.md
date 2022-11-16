##  random-useragent

This is a package to generate random user-agent. support simulating windows, linux, mac, android and simulating multiple browser clients.

## how to install

```bash
python3 -m pip install r-useragent
```

##  how to use

reference examples folder

```
from random_useragent import UserAgent

u = UserAgent()

# generate android user-agent
print(u.android())  # random
print(u.android(app="app"))
print(u.android(app="webview"))
print(u.android(app="uc"))
print(u.android(app="baidu"))
print(u.android(app="qq"))
print(u.android(app="wechat"))

# generate windows user-agent from chrome,firefox,edge...
print(u.windows())  # random
print(u.windows(app="chrome"))
print(u.windows(app="firefox"))
print(u.windows(app="edge"))

# generate linux user-agent
print(u.linux())
print(u.linux(app="chrome"))
print(u.linux(app="firefox"))


# generate mac user-agent
print(u.mac())
print(u.mac(app="chrome"))
print(u.mac(app="firefox"))
print(u.mac(app="safiri"))

# and if you want, you can just generate random ua
print(u.random())

# or designated platform
print(u.pc())
```
