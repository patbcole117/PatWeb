class Projobj:
    def __init__(self, title, desc_file):
        self.title = title
        self.desc = self.set_desc(desc_file)
        self.links = []

    def set_desc(self, desc_file):
        f = open(desc_file, 'r')
        return f.read()

    def push_link(self, link):
        self.links.append(link)

    def to_dict(self):
        return {
            'title': self.title,
            'desc': self.desc,
            'links': self.links
        }