#!/usr/bin/env python
# coding=utf-8

import datetime
from sacred.observers.base import RunObserver


def test_run_observer():
    # basically to silence coverage
    r = RunObserver()
    assert (
        r.started_event({}, "run", {}, datetime.datetime.now(datetime.UTC), {}, "comment", None) is None
    )
    assert r.heartbeat_event({}, "", datetime.datetime.now(datetime.UTC), "result") is None
    assert r.completed_event(datetime.datetime.now(datetime.UTC), 123) is None
    assert r.interrupted_event(datetime.datetime.now(datetime.UTC), "INTERRUPTED") is None
    assert r.failed_event(datetime.datetime.now(datetime.UTC), "trace") is None
    assert r.artifact_event("foo", "foo.txt") is None
    assert r.resource_event("foo.txt") is None
