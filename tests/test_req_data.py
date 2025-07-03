import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import crawl4ai_web_scrape as cws

class DummyCrawler:
    def __init__(self, *args, **kwargs):
        pass
    async def submit_and_wait(self, request_data, token=None, timeout=0, hook=None):
        self.request_data = request_data
        return {"result": {"markdown": "dummy"}}

def test_urls_is_list(monkeypatch):
    dummy = DummyCrawler()
    monkeypatch.setattr(cws, "Crawler", lambda *a, **k: dummy)
    tools = cws.Tools()
    asyncio.run(tools.web_scrape("http://example.com"))
    assert isinstance(dummy.request_data["urls"], list)
    assert dummy.request_data["urls"] == ["http://example.com"]
