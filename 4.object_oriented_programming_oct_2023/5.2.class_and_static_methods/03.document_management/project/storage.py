from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_object(category_id, self.categories)
        if category:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_object(topic_id, self.topics)
        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_object(document_id, self.documents)
        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_object(category_id, self.categories)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_object(topic_id, self.topics)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_object(document_id, self.documents)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])

    @staticmethod
    def __find_object(object_id, object_collection):
        return next((o for o in object_collection if o.id == object_id))
