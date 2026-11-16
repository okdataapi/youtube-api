# YouTube API: video search, details, comments, transcripts and channels

**YouTube data API · YouTube video search · YouTube comments · YouTube transcripts with timestamps · YouTube channel videos and posts.**

Examples for the [okdata](https://okdata.online/?src=gh-youtube-api) YouTube API: 10 live endpoints behind one API key, pay per call from $0.002. No YouTube login, no cookies and no browser, so there is no account to get blocked.

[Sign up free ($0.10 of trial credit)](https://okdata.online/signup/?src=gh-youtube-api) · [All YouTube endpoints](https://okdata.online/apis/youtube/?src=gh-youtube-api) · [Use it from Claude, Cursor or any MCP client](https://okdata.online/mcp/?src=gh-youtube-api)

## Endpoints

| Endpoint | What it returns | Price | Path |
|---|---|---|---|
| [YouTube video search](https://okdata.online/apis/youtube/videos/search/) | Videos matching keywords with views, length and channel. | $0.004 a call | `GET /v1/youtube/videos/search` |
| [YouTube video detail](https://okdata.online/apis/youtube/videos/get/) | One video by ID or link: title, description, views, likes and channel. | $0.002 a call | `GET /v1/youtube/videos/get` |
| [YouTube video comments](https://okdata.online/apis/youtube/videos/comments/list/) | Comments on a video, top or newest first. | $0.002 a call | `GET /v1/youtube/videos/comments/list` |
| [YouTube video transcript](https://okdata.online/apis/youtube/videos/transcript/get/) | The transcript of a video with timestamps, in the original or a chosen language. | $0.004 a call | `GET /v1/youtube/videos/transcript/get` |
| [YouTube comment replies](https://okdata.online/apis/youtube/comments/replies/list/) | The replies under a comment, by the comment's replies token, about 10 at a time: text, replier (handle, avatar, verification), likes, and roughly when it was posted (YouTube says "6 years ago"). post_id and parent_id are read from the token. | $0.002 a call | `GET /v1/youtube/comments/replies/list` |
| [YouTube channel posts](https://okdata.online/apis/youtube/channels/posts/list/) | The posts on a channel's Posts tab (once Community), newest first, about 10 a page, by channel ID or handle: text, pictures, likes, the video a post shares (ext.video_id, its cover in images), and roughly when it was posted (YouTube says "4 days ago"). A channel ID nobody has reads like a channel without posts: an empty page. | $0.002 a call | `GET /v1/youtube/channels/posts/list` |
| [YouTube post detail](https://okdata.online/apis/youtube/posts/get/) | One channel post (once a Community post) by ID or link: text, channel, pictures, likes, the video it shares (ext.video_id, its cover in images), and roughly when it was posted. | $0.002 a call | `GET /v1/youtube/posts/get` |
| [YouTube channel profile](https://okdata.online/apis/youtube/channels/get/) | A channel by ID or handle: name, description, avatar, verification, subscribers and video count (rounded as YouTube shows them), and under ext its total views, the day it joined, the links in its About section, country and banner. The handle comes back when you ask by handle. | $0.002 a call | `GET /v1/youtube/channels/get` |
| [YouTube channel search](https://okdata.online/apis/youtube/channels/search/) | Find channels by keywords, 20 a page in YouTube's order: channel ID, name, the start of the description, avatar and subscribers (rounded as YouTube shows them). No handle or badge here; youtube.channels.get gives the badge. | $0.004 a call | `GET /v1/youtube/channels/search` |
| [YouTube channel videos](https://okdata.online/apis/youtube/channels/videos/list/) | A channel's videos or its Shorts, newest first, about 30 a page, by channel ID or handle: title, views, cover and, for videos, length and roughly when it was published (YouTube says "3 weeks ago"). A channel ID nobody has reads like a channel without such videos: an empty page. | $0.002 a call | `GET /v1/youtube/channels/videos/list` |

## Quick start

1. Sign up at the [okdata console](https://okdata.online/signup/?src=gh-youtube-api) with your email and copy the key that starts with `okd_`.
2. Make a call:

```bash
export OKDATA_API_KEY=okd_...
curl -G "https://api.okdata.online/v1/youtube/videos/search" \
  -H "Authorization: Bearer $OKDATA_API_KEY" \
  --data-urlencode 'query=claude code tutorial'
```

The Python version is [examples/quickstart.py](examples/quickstart.py) (standard library only, and it fetches a second page too): `python3 examples/quickstart.py`.

Every endpoint answers in the same shape: the list is in `data.items`, `page.next_cursor` goes back as `cursor` for the next page, what the call cost is in `meta.billing.amount`, and a field the platform does not provide is null with the reason in `meta.unavailable`.

## Use it from AI (MCP)

Claude Code:

```bash
claude mcp add --transport http --scope user okdata https://api.okdata.online/mcp --header "Authorization: Bearer $OKDATA_API_KEY"
```

Cursor, Windsurf, VS Code and other clients with remote MCP:

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

Then ask in plain words, for example "YouTube video search: claude code tutorial". The agent uses the free `find` and `describe` tools to pick the endpoint and see its price, then `call` to fetch the data.

## FAQ

**Do I need a YouTube account?** No. The data is public content, fetched on the server; your own account is never involved.

**How is it billed?** Each endpoint has its own price, listed above for one call; endpoints billed per item count what comes back. A call that reached the data source is charged even when it comes back empty, not found or failed (one item for per-item endpoints); calls stopped before reaching a source (bad parameters, balance) are free. New accounts get $0.10 to try; after that you top up as you go, with no subscription. Pricing: https://okdata.online/pricing/

**Why not the YouTube Data API?** It runs on a daily quota (a search uses 100 of the default 10,000 units) and does not return captions for videos you do not own. Here a search is one call at a fixed price, and transcripts work for any public video that has captions.

**Can I page through results?** Each page of a list is one call: pass `page.next_cursor` back as `cursor` for the next one. A cursor stays valid for 24 hours.

**What happens when a call fails?** Every error has a fixed `code`, a `message`, and says whether you were charged (`charged`) and whether to retry (`retry`). All error codes: https://okdata.online/docs/errors/

## 中文说明

**YouTube 数据 API · YouTube 视频搜索 · YouTube 评论采集 · YouTube 字幕 · YouTube 频道视频。**

okdata 的YouTube接口示例：10 个接口在线可用，一个 API Key 调用，按次计费（$0.002 起），不用登录平台账号、不用 Cookie。中文文档：https://okdata.online/zh/apis/youtube/?src=gh-youtube-api · 注册：https://okdata.online/zh/signup/?src=gh-youtube-api · 接入 AI（MCP）：https://okdata.online/zh/mcp/?src=gh-youtube-api

## License

MIT. The data comes from the okdata API; its terms apply to API use.
