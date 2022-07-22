from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init__photos(pages)

    def __init__photos(self, pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for idx, photo in enumerate(self.photos):
            if len(photo) < PhotoAlbum.PHOTOS_PER_PAGE:
                photo.append(label)
                return f'{label} photo added successfully on page {idx + 1} slot {len(photo)}.'
        return 'No more free slots'
    
    def display(self):
        separator = '-' * 11
        result = separator + '\n'
        for page in self.photos:
            result += ' '.join('[]' for _ in page) + '\n'
            result += separator + '\n'
        return result.strip()



    

