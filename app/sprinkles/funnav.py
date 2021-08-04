from app.sprinkles.funlink import Funlink

class Funnav():
    def __init__(self):
        self.fl_list= self.make_links()
        self.bar_color = self.make_bar(0, 100)
        self.border_color = self.make_bar(155, 255)

    def make_links(self):
        home = Funlink('/home', 'home')
        about = Funlink('/about', 'about')
        projects = Funlink('/projects', 'projects')
        notlinkedin = Funlink('/notlinkedin', 'linkedin')
        contact = Funlink('/contact', 'contact')
        fl_list = [home, about, projects, notlinkedin, contact]
        return fl_list

    def make_bar(self, min=0, max=225):
        bar = Funlink('null', 'null', min, max)
        bar_color = bar.color
        return bar_color
