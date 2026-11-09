"""Pack the Inferium Lab sources for Horizon's native mod registry."""
import json
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "horizon-native.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bundle = root / "mixins" / manifest["id"]
    output = root / "target" / f'{manifest["id"]}-{manifest["version"]}.hnmod'
    output.parent.mkdir(exist_ok=True)
    pending = output.with_name(f".{output.name}.{os.getpid()}.tmp")
    try:
        with ZipFile(pending, "w") as archive:
            for path in [manifest_path, *sorted(bundle.rglob("*"))]:
                if path.is_file():
                    entry = ZipInfo(path.relative_to(root).as_posix())
                    archive.writestr(entry, path.read_bytes(), compress_type=ZIP_DEFLATED)
        pending.replace(output)
    finally:
        pending.unlink(missing_ok=True)
    print(output)


if __name__ == "__main__":
    main()
