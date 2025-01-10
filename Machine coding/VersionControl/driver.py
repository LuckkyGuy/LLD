import sys, os
sys.path.append(os.path.dirname(__file__))

from versioncControleSystem import DocumentSystem
from entites import User

# Create a system instance
system = DocumentSystem()

# Create a user
alice = User(1, "Alice")

# Alice creates a document
doc = system.create_document(alice, "DesignDoc")

# Alice updates the document
system.update_document(alice, doc.document_id, "Version 1 content")
system.update_document(alice, doc.document_id, "Version 2 content")

# Alice changes the document to version 1
system.change_version(alice, doc.document_id, 1)

# Alice tries to view version 1
version = system.go_to_version(alice, doc.document_id, 1)
print(version.content)  # Output: "Version 1 content"

# Alice deletes the document
system.delete_document(alice, doc.document_id)