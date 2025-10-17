import sys
import asyncio
from pathlib import Path
import argparse
import time

from playwright.async_api import async_playwright


async def capture_page(page, url: str, output_path: Path, wait_state: str = "load", timeout: int = 30000):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Navigating to: {url}")
    start = time.time()
    await page.goto(url, timeout=timeout)
    print(f"page.goto done in {int((time.time()-start)*1000)}ms")
    print(f"Waiting for load state: {wait_state}")
    await page.wait_for_load_state(wait_state, timeout=timeout)
    print(f"Taking screenshot -> {output_path}")
    await page.screenshot(path=str(output_path), full_page=True)


async def run_single(url: str, output: str, wait_state: str, timeout: int, headless: bool):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()
        await capture_page(page, url, Path(output), wait_state=wait_state, timeout=timeout)
        await browser.close()


async def run_batch(input_file: Path, prefix: str, out_dir: Path, start_idx: int = 1, end_idx: int = None, wait_state: str = "load", timeout: int = 30000, headless: bool = True):
    lines = [l.rstrip('\n') for l in input_file.read_text(encoding='utf-8').splitlines() if l.strip()]
    if end_idx is None:
        end_idx = len(lines)

    out_dir.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()

        i = start_idx
        for idx in range(start_idx-1, min(end_idx, len(lines))):
            raw = lines[idx].strip()
            if raw.lower().startswith("http://") or raw.lower().startswith("https://"):
                url = raw
            else:
                url = prefix.rstrip('/') + '/' + raw.lstrip('/')

            output_name = out_dir / f"photo_{i}.png"
            try:
                await capture_page(page, url, output_name, wait_state=wait_state, timeout=timeout)
                print(f"Saved {output_name}")
            except Exception as e:
                print(f"Failed to capture {url}: {e}")
            i += 1

        await browser.close()


def build_parser():
    p = argparse.ArgumentParser(description="Screenshot tool: single URL or batch from a text file")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--input", help="Path to a text file with URLs or paths (one per line) for batch mode")
    g.add_argument("url", nargs='?', help="Single URL to capture")

    p.add_argument("--output", help="Output PNG path for single mode")
    p.add_argument("--prefix", default="http://localhost:8000", help="Prefix to add to non-http lines in batch mode")
    p.add_argument("--outdir", default="output", help="Output directory for batch mode (default: output)")
    p.add_argument("--start", type=int, default=1, help="Start index (1-based) for batch mode")
    p.add_argument("--end", type=int, default=None, help="End index (inclusive) for batch mode")
    p.add_argument("--wait-state", choices=["load", "domcontentloaded", "networkidle"], default="load")
    p.add_argument("--timeout", type=int, default=30000)
    p.add_argument("--no-headless", dest="headless", action="store_false")
    return p


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv[1:])

    if args.input:
        input_file = Path(args.input)
        if not input_file.exists():
            print(f"Input file not found: {input_file}")
            return 2

        out_dir = Path(args.outdir)
        asyncio.run(run_batch(input_file, args.prefix, out_dir, start_idx=args.start, end_idx=args.end, wait_state=args.wait_state, timeout=args.timeout, headless=args.headless))
        return 0

    # single URL mode
    if not args.url or not args.output:
        print("Single mode requires both url and --output")
        return 2

    asyncio.run(run_single(args.url, args.output, wait_state=args.wait_state, timeout=args.timeout, headless=args.headless))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
