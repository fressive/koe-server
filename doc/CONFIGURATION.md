# 配置

koe-server 的配置分为**启动配置**与**运行配置**。

启动配置为硬编码形式，不可在运行时更改。  
运行配置存储在数据库中，可以在运行时更改。

## 启动配置

启动配置存放在 `src/config.py` 中。

### DATABASE_URL

**str**

用于连接 MongoDB 的 URL 。

## 运行配置

### file_provider

**str**

数据（如图像、音频等）保存方案。  

可选参数：
- [默认] local_storage 本地存储
- gridfs_storage 数据库（GridFS）存储

### data_save_path

**str**

数据（如图像、音频等）在本地保存的位置。仅当 `file_provider` 设置为 `local_storage` 时生效。

**默认值：**`./data`

### audio_transcoding_size_limit

**number**

音频文件转码大小阈值（单位：B)，即文件大小达到设定的值后才对音频进行转码。

当值为 `-1` 时禁用转码功能，当值为 `0` 时对所有音频进行转码。

**默认值：**`10485760（10MB）`


