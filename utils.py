import os
import re
from typing import Any
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 7-bit C1 ANSI sequences
ANSI_ESCAPE = re.compile(
    r"""
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
""",
    re.VERBOSE,
)

def run_command(command):
    """Execute a shell command and return its output"""
    import subprocess

    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = process.communicate()
    out = out.decode("utf-8") if out else ""
    out = ANSI_ESCAPE.sub("", out.replace("\n", "<|__newline__|>")).replace(
        "<|__newline__|>", "\n"
    )
    err = err.decode("utf-8") if err else ""
    err = ANSI_ESCAPE.sub("", err.replace("\n", "<|__newline__|>")).replace(
        "<|__newline__|>", "\n"
    )
    return process.returncode, out, err

def _log(msg: str) -> str:
    """Log an informational message"""
    logger.info(msg)
    return msg

def _err(_msg: Any, prefix: str = "Error") -> str:
    """Log an error message"""
    msg = str(_msg)
    logger.error(f"{prefix}: {msg}")
    return f"{prefix}: {msg}"