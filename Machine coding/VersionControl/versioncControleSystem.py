import sys, os
sys.path.append(os.path.dirname(__file__))

from entites import Document, User

class DocumentSystem:
    def __init__(self):
        self.documents = {}
        self.users = {}

    def create_document(self, user: User, name: str):
        if user.user_id in self.documents:
            raise ValueError("User already owns a document with this ID")
        document_id = len(self.documents) + 1
        new_document = Document(document_id, name, user.name)
        self.documents[document_id] = new_document
        user.grant_access(new_document, 'admin')
        return new_document

    def delete_document(self, user: User, document_id: int):
        document = self.documents.get(document_id, None)
        if document and user.has_access(document, 'admin'):
            document.delete()
            del self.documents[document_id]
        else:
            raise PermissionError("You do not have the required access to delete this document")

    def update_document(self, user: User, document_id: int, content: str):
        document = self.documents.get(document_id, None)
        if document and user.has_access(document, 'write'):
            document.update_document(content)
        else:
            raise PermissionError("You do not have the required access to update this document")

    def change_version(self, user: User, document_id: int, version_id: int):
        document = self.documents.get(document_id, None)
        if document and user.has_access(document, 'write'):
            document.change_version(version_id)
        else:
            raise PermissionError("You do not have the required access to change the version of this document")

    def go_to_version(self, user: User, document_id: int, version_id: int):
        document = self.documents.get(document_id, None)
        if document and user.has_access(document, 'read'):
            return document.get_version(version_id)
        else:
            raise PermissionError("You do not have the required access to view this version of the document")
