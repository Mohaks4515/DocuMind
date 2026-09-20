from pathlib import Path
import shutil

from fastapi import UploadFile


UPLOAD_DIR = Path("uploads")

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB


async def save_document(
    file: UploadFile,
    user_id: int
) -> str:

    user_upload_dir = UPLOAD_DIR / str(user_id)

    user_upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    safe_filename = Path(file.filename).name

    file_path = user_upload_dir / safe_filename

    total_size = 0

    try:
        with file_path.open("wb") as buffer:

            while True:
                chunk = await file.read(1024 * 1024)

                if not chunk:
                    break

                total_size += len(chunk)

                if total_size > MAX_FILE_SIZE:
                    raise ValueError(
                        "File size exceeds 20 MB limit"
                    )

                buffer.write(chunk)

        return str(file_path)

    except Exception:
        if file_path.exists():
            file_path.unlink()

        raise