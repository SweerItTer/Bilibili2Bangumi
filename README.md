# Bilibili2Bangumi - 将B站追番列表迁移到Bangumi

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
[![GitHub license](https://img.shields.io/github/license/SweerItTer/Bilibili2Bangumi)](https://github.com/SweerItTer/Bilibili2Bangumi/blob/main/LICENSE)

一个用于将Bilibili追番列表迁移到Bangumi.tv的Python脚本工具。自动获取B站用户的追番列表，并准备数据用于同步到Bangumi平台。

## 功能特性

- 使用官方Bilibili API，数据准确可靠
- 长期维护的开源第三方库[bilibili-api](https://github.com/nemo2011/bilibili-api)
- 获取指定B站用户所有追番条目
- 支持分页获取，处理大量追番数据
- 将追番数据保存为结构化的JSON文件

## 快速开始

### 安装依赖

```bash
pip3 install bilibili-api-python
pip3 install aiohttp
pip3 install httpx
pip3 install "curl_cffi"
```

### 配置用户ID

编辑脚本文件，将用户ID替换为你的B站用户ID：

```python
# 在脚本中找到这行并修改数字为你的B站用户ID
u = user.User(361883361)  # 将361883361替换为你的用户ID
```

你可以在B站用户主页URL中找到用户ID，例如：  
`https://space.bilibili.com/361883361/` 中的 `361883361`

### 运行脚本

```bash
python3 bilibili_to_bangumi.py
```

脚本运行后，会在当前目录生成 `bilibili_bangumi.json` 文件，包含所有追番数据。

## 输出示例

```json
[
  {
    "name": "剧场版 咒术回战 0",
    "media_id": 22006270,
    "season_id": 48001,
    "cover": "https://i0.hdslb.com/bfs/bangumi/image/0082a5c243151ef989439578e745785268c58e7d.png"
  },
  {
    "name": "地。-关于地球的运动-",
    "media_id": 22953531,
    "season_id": 48688,
    "cover": "https://i0.hdslb.com/bfs/bangumi/image/9224dea1cf31c2d014d7ccee4b7a22f5ff1b9dd7.png"
  },
]
```

## 文件说明

- `bilibili_to_bangumi.py` - 主脚本文件，用于获取B站追番数据
- `bilibili_bangumi.json` - 脚本生成的追番数据文件
- `bangumi_sync.py` - (即将推出) 将数据同步到Bangumi的脚本

## 同步到Bangumi

> **注意**：完整的Bangumi同步功能正在开发中，请关注项目更新！

当前版本只完成B站数据抓取部分。接下来我们将实现：

1. 使用Bangumi API进行身份验证
2. 将抓取的数据与Bangumi条目匹配
3. 将追番列表添加到Bangumi账户

## 贡献指南

欢迎贡献代码或提出建议！请遵循以下步骤：

1. Fork 本仓库
2. 创建新分支 (`git checkout -b feature/your-feature`)
3. 提交更改 (`git commit -am 'Add some feature'`)
4. 推送到分支 (`git push origin feature/your-feature`)
5. 创建Pull Request

## 注意事项

1. B站API可能有请求频率限制
2. 如果遇到连接问题，请检查网络环境或稍后重试
3. 目前仅支持公开追番列表，私密列表需要用户登录
4. 确保使用最新版的 `bilibili-api` 库

## 相关资源

- [Bilibili-API 文档](https://nemo2011.github.io/bilibili-api/)
- [Bangumi API 文档](https://bangumi.github.io/api/)

## 许可证

本项目采用 [GPL-3.0 许可证](LICENSE)