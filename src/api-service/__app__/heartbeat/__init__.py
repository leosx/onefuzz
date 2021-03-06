#!/usr/bin/env python
#
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import json
import logging

import azure.functions as func
from onefuzztypes.models import HeartbeatEntry

from ..onefuzzlib.dashboard import get_event
from ..onefuzzlib.heartbeat import Heartbeat


def main(msg: func.QueueMessage, dashboard: func.Out[str]) -> None:
    body = msg.get_body()
    logging.info("heartbeat: %s", body)

    raw = json.loads(body)
    Heartbeat.add(HeartbeatEntry.parse_obj(raw))

    event = get_event()
    if event:
        dashboard.set(event)
