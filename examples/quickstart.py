#!/usr/bin/env python3
"""YouTube video search: one call, then the next page. Standard library only.

    export OKDATA_API_KEY=okd_...
    python3 examples/quickstart.py
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

URL = "https://api.okdata.online/v1/youtube/videos/search"
PARAMS = {"query": "claude code tutorial"}


def call(params):
    req = urllib.request.Request(
        URL + "?" + urllib.parse.urlencode(params),
        headers={"Authorization": "Bearer " + os.environ["OKDATA_API_KEY"]},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        body = json.load(err)
        raise SystemExit(f"{body['code']}: {body.get('message')} (charged: {body.get('charged')})")


def main():
    body = call(PARAMS)
    for item in body["data"]["items"]:
        print(item.get("id"), (item.get("title") or item.get("text") or "")[:60].replace("\n", " "))
    print("This page cost $" + body["meta"]["billing"]["amount"] + ", balance $" + body["meta"]["billing"]["balance_after"])
    cursor = body.get("page", {}).get("next_cursor")
    if cursor:
        nxt = call({**PARAMS, "cursor": cursor})
        print("Page 2:", len(nxt["data"]["items"]), "items, cost $" + nxt["meta"]["billing"]["amount"])


if __name__ == "__main__":
    main()
