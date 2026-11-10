from pathlib import Path

for split in ["train", "val"]:
    labels_dir = Path(split) / "labels"

    for label in labels_dir.glob("*.txt"):
        # Remove the UUID prefix
        new_name = label.name.split("-", 1)[-1]

        new_path = label.parent / new_name

        if new_path.exists():
            raise FileExistsError(f"Already exists: {new_path}")

        label.rename(new_path)

        print(f"{label.name} -> {new_name}")
