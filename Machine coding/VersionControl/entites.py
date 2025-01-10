class Version:
    def __init__(self, version_id: int, content: str):
        self.version_id = version_id
        self.content = content

class Document:
    def __init__(self, document_id: int, name: str, owner: str):
        self.document_id = document_id
        self.name = name
        self.owner = owner
        self.versions = []
        self.current_version = None

    def create_version(self, content: str):
        version_id = len(self.versions) + 1
        new_version = Version(version_id, content)
        self.versions.append(new_version)
        self.current_version = new_version

    def get_version(self, version_id: int):
        for version in self.versions:
            if version.version_id == version_id:
                return version
        return None

    def update_document(self, content: str):
        self.create_version(content)

    def change_version(self, version_id: int):
        version = self.get_version(version_id)
        if version:
            self.current_version = version
        else:
            raise ValueError("Version not found")

    def delete(self):
        self.versions.clear()
        self.current_version = None


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.access_rights = {}

    def grant_access(self, document: Document, access_level: str):
        self.access_rights[document.document_id] = access_level

    def has_access(self, document: Document, required_level: str):
        access_level = self.access_rights.get(document.document_id, None)
        if access_level is None:
            return False
        access_levels = ['read', 'write', 'admin']
        return access_levels.index(access_level) >= access_levels.index(required_level)