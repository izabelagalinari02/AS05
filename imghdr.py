#!/usr/bin/env python3
"""
imghdr.py - Determine the type of image contained in a file or byte stream.
Adapted from Python 3.10 standard library.
"""
import os

# Content-marker dictionary:
# maps image type name to (offset, magic bytes, mask bytes)
MAGIC: dict[str, tuple[int, bytes, bytes | None]] = {
    "rgb": (0, b"\x01\xda\x01", None),
    "gif": (0, b"GIF87a", None),
    "gif": (0, b"GIF89a", None),
    "pbm": (0, b"P4", None),
    "pgm": (0, b"P5", None),
    "ppm": (0, b"P6", None),
    "tiff": (0, b"MM\x00*", None),  # Big-endian TIFF
    "tiff": (0, b"II*\x00", None),  # Little-endian TIFF
    "rast": (0, b"YJLS", None),
    "xbm": (0, b"#define ", None),
    "jpeg": (0, b"\xff\xd8\xff", None),
    "png": (0, b"\211PNG\r\n\032\n", None),
    "bmp": (0, b"BM", None),
    "webp": (8, b"WEBP", None),
}

# Additional testers

def _test_exr(h: bytes, f: object) -> bool:
    # OpenEXR files start with 'v/1_0\0\0\0\0\0\0'
    return h.startswith(b"v/1_0")

# List of test functions
_tests: list[callable] = []

def test_rgb(h: bytes, f: object) -> bool:
    return h[0:3] == b"\x01\xda\x01"
_tests.append(test_rgb)

import struct

def test_exr(h: bytes, f: object) -> bool:
    return _test_exr(h, f)
_tests.append(test_exr)

# Define other typed tests dynamically

def what(file: str | os.PathLike | None = None, h: bytes | None = None) -> str | None:
    """
    Determine image type based on file header or initial bytes.
    """
    if h is None:
        if file is None:
            return None
        try:
            with open(file, 'rb') as f:
                h = f.read(32)
        except OSError:
            return None
    else:
        # ensure h is at least 32 bytes
        h = h[:32]
    for name, (offset, magic, mask) in MAGIC.items():
        if len(h) < offset + len(magic):
            continue
        segment = h[offset:offset + len(magic)]
        if mask:
            # apply mask
            seg2 = bytes(c & m for c, m in zip(segment, mask))
            if seg2 == magic:
                return name
        else:
            if segment == magic:
                return name
    # fallback to call test functions
    for tester in _tests:
        try:
            if tester(h, None):
                return tester.__name__[5:]
        except Exception:
            pass
    return None

# Expose public API names
__all__ = ["what"]
