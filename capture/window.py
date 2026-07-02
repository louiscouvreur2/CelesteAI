from __future__ import annotations

from dataclasses import dataclass

import win32gui


@dataclass
class GameWindow:
    hwnd: int
    title: str
    left: int
    top: int
    width: int
    height: int


def _enum_callback(hwnd: int, windows: list[GameWindow]) -> None:
    if not win32gui.IsWindowVisible(hwnd):
        return

    title = win32gui.GetWindowText(hwnd)

    if "Celeste" not in title:
        return

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    windows.append(
        GameWindow(
            hwnd=hwnd,
            title=title,
            left=left,
            top=top,
            width=right - left,
            height=bottom - top,
        )
    )


def find_celeste_window() -> GameWindow | None:
    """
    Recherche la première fenêtre contenant 'Celeste' dans son titre.
    """

    windows: list[GameWindow] = []

    win32gui.EnumWindows(
        lambda hwnd, _: _enum_callback(hwnd, windows),
        None,
    )

    if not windows:
        return None

    return windows[0]