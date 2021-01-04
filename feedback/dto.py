class BoundingBox(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return str(self.__dict__())

    def __repr__(self):
        # return f'Data[{self.id}]'
        return str(self.__dict__())

    def __dict__(self):
        d = {
            "x": self.x,
            "y": self.y,
            "w": self.w,
            "h": self.h
        }
        return d


class UploadedImage(object):
    def __init__(self, name, source_origin):
        self.name = name
        self.source_origin = source_origin

    def __str__(self):
        return str(self.__dict__())

    def __repr__(self):
        # return f'Data[{self.id}]'
        return str(self.__dict__())

    def __dict__(self):
        d = {
            'name': self.name,
            'source_origin': self.source_origin,
        }
        return d


class ItemDto(object):
    def __init__(
            self, label, description, image, box_x, box_y, box_w, box_h,
            **kwargs
    ):
        self.label = label
        self.description = description
        self.bbox = BoundingBox(box_x, box_y, box_w, box_h)
        self.image = UploadedImage(
            image['name'], image['source_origin']
        ) if image else None

    def __str__(self):
        return str(self.__dict__())

    def __repr__(self):
        # return f'Data[{self.id}]'
        return str(self.__dict__())

    def __dict__(self):
        d = {
            'label': self.label,
            'description': self.description,
            'bbox': self.bbox.__dict__(),
        }
        if self.image:
            d['image'] = self.image.__dict__()

        return d
