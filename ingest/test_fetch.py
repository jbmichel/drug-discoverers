"""Offline tests for the parts that do not need network.

The paging arithmetic is the one place a silent bug costs you an archive,
so it is tested per platform against hand-computed values.
"""
import json, pathlib, sys, tempfile, types

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from ingest.fetch import Store, next_params, parse_items, extract_title


def test_paging():
    # Blogger: 1-based item offsets -> 1, 501, 1001
    assert [next_params("start-index", {"max-results": 500}, p, 500)["start-index"]
            for p in range(3)] == [1, 501, 1001]
    # WordPress: 1-based page numbers -> 1, 2, 3
    assert [next_params("paged", {}, p, 10)["paged"] for p in range(3)] == [1, 2, 3]
    # Substack: 0-based item offsets -> 0, 50, 100
    assert [next_params("offset", {"limit": 50}, p, 50)["offset"]
            for p in range(3)] == [0, 50, 100]
    try:
        next_params("bogus", {}, 0, 10)
    except ValueError:
        pass
    else:
        raise AssertionError("unknown paging scheme must raise")
    print("paging arithmetic ok (blogger / wordpress / substack)")


def test_store_roundtrip_and_resume():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        s = Store(root=root, delay=0)
        s.write(person="X", method="git", source_url="u1", title="t", text="hello")
        s.write(person="X", method="git", source_url="u2", title="t2", text="world")
        assert s.have("u1") and not s.have("u3")
        s.state["k"] = {"page": 7}
        s.save_state()

        # a fresh Store must rediscover what was already fetched
        s2 = Store(root=root, delay=0)
        assert s2.have("u1"), "resume failed: docs.jsonl not replayed"
        assert s2.state["k"]["page"] == 7, "resume failed: state lost"
        rows = [json.loads(l) for l in (root / "docs.jsonl").open()]
        assert len(rows) == 2
        assert all(r["person"] == "X" and r["source_url"] and r["fetched_at"]
                   for r in rows), "provenance missing"
        blob = (root / "raw" / f"{rows[0]['sha256']}.bin").read_bytes()
        assert blob == b"hello"
        print("store round-trip, provenance and resume ok")


def test_parsers():
    # Blogger JSON shape
    fake = types.SimpleNamespace(
        headers={"content-type": "application/json"},
        json=lambda: {"feed": {"entry": [{
            "title": {"$t": "Post A"},
            "published": {"$t": "2020-01-01"},
            "content": {"$t": "<p>body</p>"},
            "link": [{"rel": "self", "href": "x"},
                     {"rel": "alternate", "href": "https://b/post-a.html"}]}]}})
    items = parse_items(fake)
    assert items == [{"url": "https://b/post-a.html", "title": "Post A",
                      "published": "2020-01-01", "text": "<p>body</p>"}]

    # Substack list shape
    fake2 = types.SimpleNamespace(
        headers={"content-type": "application/json"},
        json=lambda: [{"canonical_url": "https://s/p1", "title": "P1",
                       "post_date": "2021-02-03", "body_html": "<p>hi</p>"}])
    assert parse_items(fake2)[0]["url"] == "https://s/p1"

    assert extract_title("<html><title> Hello </title>") == "Hello"
    print("blogger / substack parsers and title extraction ok")


if __name__ == "__main__":
    test_paging()
    test_store_roundtrip_and_resume()
    test_parsers()
    print("\nall offline tests passed")
