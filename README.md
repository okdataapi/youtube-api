# YouTube 数据接口（YouTube API）：视频搜索、视频详情、评论、字幕、频道

**YouTube 数据 API · YouTube 视频搜索 · YouTube 评论采集 · YouTube 字幕 · YouTube 频道视频。**

这个仓库是 [okdata](https://okdata.online/zh/?src=gh-youtube-api) 的YouTube接口示例：10 个接口在线可用，一个 API Key 调用，按次计费（$0.002 起），失败不扣费。不用登录平台账号，不用 Cookie，不开浏览器，所以也不存在账号被风控的问题。

[免费注册拿 Key（送 $0.1 试用额度）](https://okdata.online/zh/signup/?src=gh-youtube-api) · [全部接口文档](https://okdata.online/zh/apis/?src=gh-youtube-api) · [接入 AI（MCP）](https://okdata.online/zh/mcp/?src=gh-youtube-api)

## 接口清单

| 接口 | 说明 | 价格 | 路径 |
|---|---|---|---|
| [YouTube 视频搜索](https://okdata.online/zh/apis/youtube/videos/search/) | 按关键词搜视频，带播放量、时长和频道。 | $0.004 / 次 | `GET /v1/youtube/videos/search` |
| [YouTube 视频详情](https://okdata.online/zh/apis/youtube/videos/get/) | 按 ID 或链接取一个视频：标题、简介、播放、点赞和频道。 | $0.002 / 次 | `GET /v1/youtube/videos/get` |
| [YouTube 视频评论](https://okdata.online/zh/apis/youtube/videos/comments/list/) | 视频评论，按热门或最新。 | $0.002 / 次 | `GET /v1/youtube/videos/comments/list` |
| [YouTube 视频字幕](https://okdata.online/zh/apis/youtube/videos/transcript/get/) | 视频字幕，带时间戳，原语言或指定语言。 | $0.004 / 次 | `GET /v1/youtube/videos/transcript/get` |
| [YouTube 评论回复](https://okdata.online/zh/apis/youtube/comments/replies/list/) | 用评论的回复标识取这条评论下的回复，每次约 10 条：内容、回复者（用户名、头像、认证）、点赞，以及大约的发布时间（YouTube 只说“6 年前”）。post_id 和 parent_id 从回复标识里读出。 | $0.002 / 次 | `GET /v1/youtube/comments/replies/list` |
| [YouTube 频道帖子](https://okdata.online/zh/apis/youtube/channels/posts/list/) | 频道“帖子”栏（原“社区”）里的帖子，从新到旧，每页约 10 条，按频道 ID 或用户名取：正文、图片、点赞、帖子分享的视频（ext.video_id，封面在 images 里），以及大约的发布时间（YouTube 只说“4 天前”）。不存在的频道 ID 和没有帖子的频道一样，返回空结果。 | $0.002 / 次 | `GET /v1/youtube/channels/posts/list` |
| [YouTube 帖子详情](https://okdata.online/zh/apis/youtube/posts/get/) | 按 ID 或链接取一条频道帖子（原“社区”帖）：正文、频道、图片、点赞、帖子分享的视频（ext.video_id，封面在 images 里），以及大约的发布时间。 | $0.002 / 次 | `GET /v1/youtube/posts/get` |
| [YouTube 频道资料](https://okdata.online/zh/apis/youtube/channels/get/) | 按频道 ID 或用户名取一个频道：名称、简介、头像、认证、订阅数和视频数（按 YouTube 显示的取整），ext 里还有总播放量、注册日期、“关于”里列的链接、国家和横幅图。按用户名查时会带回用户名。 | $0.002 / 次 | `GET /v1/youtube/channels/get` |
| [YouTube 频道搜索](https://okdata.online/zh/apis/youtube/channels/search/) | 按关键词找频道，每页 20 个，按 YouTube 的顺序：频道 ID、名称、简介开头、头像和订阅数（按 YouTube 显示的取整）。这里没有用户名和认证标识，认证标识可用 youtube.channels.get 查。 | $0.004 / 次 | `GET /v1/youtube/channels/search` |
| [YouTube 频道视频](https://okdata.online/zh/apis/youtube/channels/videos/list/) | 按频道 ID 或用户名取频道的视频或 Shorts，从新到旧，每页约 30 条：标题、播放数、封面，普通视频还有时长和大约的发布时间（YouTube 只说“3 周前”）。不存在的频道 ID 和没有这类视频的频道一样，返回空结果。 | $0.002 / 次 | `GET /v1/youtube/channels/videos/list` |

## 快速开始

1. 在 [okdata 控制台](https://okdata.online/zh/signup/?src=gh-youtube-api) 用邮箱注册，拿到 `okd_` 开头的 Key。
2. 调一次接口：

```bash
export OKDATA_API_KEY=okd_...
curl -G "https://api.okdata.online/v1/youtube/videos/search" \
  -H "Authorization: Bearer $OKDATA_API_KEY" \
  --data-urlencode 'query=claude code tutorial'
```

Python 版在 [examples/quickstart.py](examples/quickstart.py)（只用标准库，会顺带演示翻页）：`python3 examples/quickstart.py`。

返回统一的结构：列表在 `data.items`，下一页用 `page.next_cursor` 传回 `cursor`，这次扣了多少钱在 `meta.billing.amount`，平台不提供的字段为 null 并在 `meta.unavailable` 里写明原因。

## 让 AI 直接用（MCP）

Claude Code：

```bash
claude mcp add --transport http --scope user okdata https://api.okdata.online/mcp --header "Authorization: Bearer $OKDATA_API_KEY"
```

Cursor、Cherry Studio、WorkBuddy 等支持远程 MCP 的客户端：

```json
{
  "mcpServers": {
    "okdata": {
      "url": "https://api.okdata.online/mcp",
      "headers": {
        "Authorization": "Bearer okd_..."
      }
    }
  }
}
```

接好以后直接用中文说需求，比如「YouTube 视频搜索：claude code tutorial」。AI 会先用免费的 `find`、`describe` 找接口和看价格，再用 `call` 取数据。

## 常见问题

**要登录平台账号吗？** 不用。数据是公开内容，okdata 在服务端获取，你的账号完全不参与。

**怎么收费？** 每个接口单独定价，表里写的就是一次调用的价格；按条计费的接口按实际返回条数算。调用失败（包括超时）不扣费。新账号送 $0.1 试用额度，之后按需充值，没有订阅。价格页：https://okdata.online/zh/pricing/

**和官方开放平台有什么区别？** 官方开放平台只能读授权给你的账号自己的数据，而且要企业资质和审核；这里是平台上任何人都能看到的公开数据，比如搜索结果、别人的笔记或视频、评论、热榜。

**能翻页吗？** 列表接口每页一次调用，把 `page.next_cursor` 原样传回 `cursor` 就是下一页，24 小时内有效。

**出错了怎么办？** 每个错误都有固定的 `code`、中文说明 `message_zh`，以及会不会扣费（`charged`）和要不要重试（`retry`）。全部错误码：https://okdata.online/zh/docs/errors/

## English

Examples for the okdata YouTube API: 10 live endpoints behind one API key, pay per call from $0.002, failed calls free, no platform login or cookies. Sign up at https://okdata.online/signup/?src=gh-youtube-api, docs at https://okdata.online/apis/, MCP at https://okdata.online/mcp/.

## License

MIT. The data comes from the okdata API; its terms apply to API use.
