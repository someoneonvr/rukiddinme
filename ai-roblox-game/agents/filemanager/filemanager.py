# agents/filemanager/filemanager.py

import os
import json

class FileManagerAI:
    def __init__(self, base_dir="generated"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def accept_task(self, task):
        description = task["description"]
        target_folder = task.get("target", "Misc")

        print(f"[FileManagerAI] Organizing assets for: {description}")

        folder_path = os.path.join(self.base_dir, target_folder)
        os.makedirs(folder_path, exist_ok=True)

        # Simulate asset prep (placeholder)
        asset_filename = os.path.join(folder_path, "asset_metadata.json")
        with open(asset_filename, "w") as f:
            json.dump({
                "description": description,
                "organized": True
            }, f, indent=2)

        return f"Assets for '{description}' placed in: {folder_path}"
