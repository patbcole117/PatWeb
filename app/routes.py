from app import app
from flask import render_template

from app.sprinkles.funlink import Funlink
from app.sprinkles.projobj import Projobj
from app.sprinkles.nav import Nav

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home', nav=Nav())

@app.route('/about')
def about():
    return render_template('about.html', title='about', nav=Nav())

@app.route('/contact')
def contact():
    f1 = Funlink('mailto:pcolemanofficial@gmail.com', 'pcolemanofficial@gmail.com', 100)
    return render_template('contact.html', title='contact', fl=f1, nav=Nav())

@app.route('/notlinkedin')
def notlinedin():
    f1 = Funlink('https://news.linkedin.com/2021/june/an-update-from-linkedin', '1. “An Update on Report of Scraped Data.” LinkedIn, LinkedIn Corporation, \
        29 June 2021.', 50)

    f2 = Funlink('https://www.reuters.com/technology/linkedin-says-some-user-data-extracted-posted-sale-2021-04-09/', '2. Rana, Akanksha and Tiyashi Datta. \
        “LinkedIn Says Some User Data Scraped and Posted for Sale.” Edited by Arun Koyyur, Reuters, Thomson Reuters, 9 Apr. 2021.', 50)

    f3 = Funlink('https://www.forbes.com/sites/zakdoffman/2019/07/22/critical-linkedin-warning-as-irans-hackers-send-fake-invites-laced-with-malware/?sh=185\
        f9c056ac1', '3. Doffman, Zak. “Warning As Iranian State Hackers Target LinkedIn Users With Dangerous New Malware.” Forbes, Forbes Magazine, 22 July 2019.', 50)

    f4 = Funlink('https://slate.com/technology/2019/04/linkedin-stalking-self-loathing-social-media-envy.html', '4. Palus, Shannon and Heather Schwedel. \
        “When It Comes to Feeling Bad About Yourself Online, Nothing Compares to LinkedIn.” Slate Magazine, Slate, 5 Apr. 2019,', 50)

    fl_list = [f1, f2, f3, f4]

    return render_template('notlinkedin.html', title='notlinkedin', fl_list=fl_list, nav=Nav())

@app.route('/projects')
def projects():

    pj_list = []

    # Project 1. SaltyMicro
    saltyMicro = Projobj('SaltyMicro', 'app/templates/txt/descsaltymicro.txt')
    saltyMicro.push_link(Funlink('/pos/saltymicro', 'project-outline', 50))
    saltyMicro.push_link(Funlink('https://github.com/patbcole117/SBOv2', 'sbo.git', 50))
    saltyMicro.push_link(Funlink('https://github.com/patbcole117/SDCv2', 'sdc.git', 50))
    saltyMicro.push_link(Funlink('https://github.com/patbcole117/SUIv2', 'sui.git', 50))
    saltyMicro.push_link(Funlink('https://saltymicro.gyokuro.info/', 'website', 50))
    pj_list.append(saltyMicro)

    # Project 2. Home Network
    homenet = Projobj('Home Network', 'app/templates/txt/deschomenet.txt')
    homenet.push_link(Funlink('/pos/homenet', 'project-outline', 50))
    pj_list.append(homenet)

    # Project 3. My Website
    patweb = Projobj('My Website', 'app/templates/txt/descpatweb.txt')
    patweb.push_link(Funlink('/pos/patweb', 'project-outline', 50))
    patweb.push_link(Funlink('https://github.com/patbcole117/PatWeb', 'patweb.git', 50))
    pj_list.append(patweb)
    return render_template('projects.html', title='projects', pj_list=sorted(pj_list, key=lambda p: p.title), nav=Nav())

@app.route('/pos/saltymicro')
def posaltymicro():
    return render_template('/pos/saltymicro.html', title='saltymicro outline', nav=Nav())

@app.route('/pos/homenet')
def poshomenet():
    return render_template('/pos/homenet.html', title='homenet outline', nav=Nav())

@app.route('/pos/patweb')
def pospatweb():
    return render_template('/pos/patweb.html', title='patweb outline', nav=Nav())