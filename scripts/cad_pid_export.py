#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAD PID 提取与 Excel 导出工具

用途：
  1) 扫描 CAD 导出文本 / CSV / TXT / DXF ASCII 文本中的管线号
  2) 提取格式如 15-HV-0103-A2E
  3) 转换为 NEW PIPE /15-HV-0103-A2E PSPEC /A2E
  4) 导出 Excel 表格

示例：
  python scripts/cad_pid_export.py D:/cad/export.txt --out pid_export.xlsx
  python scripts/cad_pid_export.py D:/cad --out pid_export.xlsx

依赖：
  pip install openpyxl
"""

import argparse
import os
import re
import sys
from collections import OrderedDict
from pathlib import Path

try:
    from openpyxl import Workbook
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing dependency: openpyxl. Please install with: pip install openpyxl"
    ) from exc

# 识别 PID 号，支持 15-HV-0103-A2E 这类模式
PIPE_RE = re.compile(
    r"(?<![A-Z0-9])(?P<pid>\d{1,4}-[A-Z]{2}-\d{3,6}-[A-Z0-9]{2,5})(?![A-Z0-9])",
    re.IGNORECASE,
)

TEXT_EXTS = {
    ".txt",
    ".csv",
    ".log",
    ".dat",
    ".out",
    ".dxf",
    ".xml",
    ".md",
    ".rst",
    ".json",
    ".ini",
    ".cfg",
    ".mpp",
}


def normalize_pid(value: str) -> str:
    value = value.strip().upper().replace(" ", "")
    return value


def format_pid(pid: str) -> str:
    suffix = pid.rsplit("-", 1)[-1]
    return f"NEW PIPE /{pid} PSPEC /{suffix}"


def extract_from_text(text: str):
    matches = []
    for match in PIPE_RE.finditer(text):
        pid = normalize_pid(match.group("pid"))
        if pid and pid not in matches:
            matches.append(pid)
    return matches


def iter_candidate_files(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    if p.is_file():
        yield p
        return

    for root, _, files in os.walk(str(p)):
        for f in sorted(files):
            full = os.path.join(root, f)
            ext = Path(full).suffix.lower()
            if ext in TEXT_EXTS or "." not in f:
                yield Path(full)


def extract_pipe_ids(input_path: str):
    results = OrderedDict()
    for file_path in iter_candidate_files(input_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as fh:
                text = fh.read()
        except OSError:
            continue

        for pid in extract_from_text(text):
            results.setdefault(pid, file_path.name)

    return list(results.keys())


def write_excel(pipe_ids, output_path: str):
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "PID"
    ws.append(["PID", "FORMATTED"])

    for pid in pipe_ids:
        ws.append([pid, format_pid(pid)])

    # 自动调整列宽
    for column_cells in ws.columns:
        max_len = 0
        column = column_cells[0].column_letter
        for cell in column_cells:
            try:
                val_len = len(str(cell.value))
            except Exception:
                val_len = 0
            if val_len > max_len:
                max_len = val_len
        ws.column_dimensions[column].width = min(max_len + 2, 40)

    wb.save(str(out))
    return str(out)


def main():
    parser = argparse.ArgumentParser(
        description="Extract PID numbers from CAD/export text and export to Excel."
    )
    parser.add_argument("input", help="CAD export text file or folder")
    parser.add_argument(
        "--out",
        default="cad_pid_export.xlsx",
        help="output Excel path, default: cad_pid_export.xlsx",
    )
    args = parser.parse_args()

    try:
        pids = extract_pipe_ids(args.input)
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")
        return 1

    if not pids:
        print("[INFO] No PID-like numbers found.")
        return 0

    out_path = write_excel(pids, args.out)
    print(f"[OK] Extracted {len(pids)} PID entries.")
    print(f"[OK] Excel saved to: {out_path}")
    for pid in pids:
        print(f"{pid} -> {format_pid(pid)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
