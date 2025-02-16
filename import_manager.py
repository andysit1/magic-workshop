import os
import re

class ImportManager:
    def __init__(self):
        self.import_cache = {}

    def register(self, class_name, path):
        """Store the new location of a class."""
        self.import_cache[class_name] = path

    def fix_imports(self, files):
        """Rewrite imports to match the new file locations."""
        for path, content in files.items():
            new_content = content
            for class_name, new_path in self.import_cache.items():
                new_import = f"from {new_path.replace('/', '.')} import {class_name}"
                new_content = re.sub(rf"from .* import {class_name}", new_import, new_content)

            with open(path, "w") as f:
                f.write(new_content)

        print("Fixed imports!")
