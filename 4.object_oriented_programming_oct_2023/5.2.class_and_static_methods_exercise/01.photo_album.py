# Create a class called PhotoAlbum. Upon initialization, it should receive pages (int). It should also have one more
# attribute: photos (empty matrix) representing the album with its pages where you should put the photos. Each page can
# contain only 4 photos. The class should also have 3 more methods:
# •	from_photos_count(photos_count: int) - creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos.
# •	add_photo(label: str) - adds the photo in the first possible page and slot and return "{label} photo added
# successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}". If there are no free slots
# left, return "No more free slots"
# •	display() - returns a string representation of each page and the photos in it. Each photo is marked with "[]", and
# the page separation is made using 11 dashes (-). For example, if we have 1 page and 2 photos:
# -----------
# [] []
# -----------
# and if we have 2 empty pages:
# -----------
#
# -----------
#
# -----------
#
# Test code:
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
#
# Output:
# baby photo added successfully on page 1 slot 1
# first grade photo added successfully on page 1 slot 2
# eight grade photo added successfully on page 1 slot 3
# party with friends photo added successfully on page 1 slot 4
# [['baby', 'first grade', 'eight grade', 'party with friends'], []]
# prom photo added successfully on page 2 slot 1
# wedding photo added successfully on page 2 slot 2
# -----------
# [] [] [] []
# -----------
# [] []
# -----------

import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        separator = "-----------\n"
        result = separator
        for page in self.photos:
            result += " ".join(["[]" for _ in page]) + "\n"
            result += separator
        return result.strip()


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
