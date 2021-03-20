# koe-server

使用 FastAPI 构建的服务器，大部分请求遵循 GraphQL 设计。

## 安装

### 需求

- MongoDB

### 手动安装

```
$ git clone https://github.com/fressive/koe-server.git
$ cd koe-server/src
$ pip3 install -r requirements.txt
```

#### 运行

```
$ uvicorn main:app --host 0.0.0.0
```

## 文档

- [API](doc/API.md)
- [配置](doc/CONFIGURATION.md)
- [转码](doc/TRANSCODING.md)
