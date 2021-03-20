# 音频转码

Koe 支持自动音频转码，详见 `src/job/file_transcoder.py` 。

对音频转码能够减小网络传输负担，但是增加了存储空间占用。

若符合转码条件，则会自动转码为以下格式的文件：
- 24bit 441000Hz 128kbps MP3
- 24bit 441000Hz 192kbps MP3
- 24bit 441000Hz 320kbps MP3
