# Scruby-Return-Dict - In search methods, returns results in the form of dictionaries.
# Copyright (c) 2026 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Scruby-Return-Dict Plugin."""

from __future__ import annotations

from typing import Any

from scruby_plugin import ScrubyPlugin


class ReturnDict(ScrubyPlugin):
    """Scruby-Return-Dict Plugin.

    In search methods, returns results in the form of dictionaries.
    """

    def __init__(self, scruby_self: Any) -> None:  # noqa: D107
        ScrubyPlugin.__init__(self, scruby_self)
