# API

Koe 通过 HTTP API 实现客户端与服务端的通信。

你可以基于这些 API 构建一个新的 Koe 客户端。

## Authorization

Koe 采用单用户模式，所以对于请求的验证非常简单，验证的密钥即为后端生成的 API Key 。

在每个 HTTP 请求中加入 `Authorization` 请求头：
```
Authorization: Apikey [YOUR_API_KEY_HERE]
```

## Docs

大部分 Koe API 采用的是 GraphQL 标准构建。

### GraphQL

`POST /api/graphql`

### File

Koe 目前使用 RESTFul API 处理文件请求。

#### 从 FileID 获取文件

`GET /api/v1/file/id/[id]`

当成功获取到文件时返回文件内容，获取失败时返回状态码 `404` 与错误信息。

#### 从 Hash 获取文件

`GET /api/v1/file/hash/[hash]`

返回同上。