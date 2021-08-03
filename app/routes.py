from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')

@app.route('/notlinkedin')
def notlinedin():
    sources = []

    sources.append({'url': 'https://news.linkedin.com/2021/june/an-update-from-linkedin', \
        'citation': '1. “An Update on Report of Scraped Data.” LinkedIn, LinkedIn Corporation, 29 June 2021.' })

    sources.append({'url': 'https://www.reuters.com/technology/linkedin-says-some-user-data-extracted-posted-sale-2021-04-09/', \
        'citation': '2. Rana, Akanksha and Tiyashi Datta. “LinkedIn Says Some User Data Scraped and Posted for Sale.” Edited \
            by Arun Koyyur, Reuters, Thomson Reuters, 9 Apr. 2021.' })

    sources.append({'url': 'https://www.forbes.com/sites/zakdoffman/2019/07/22/critical-linkedin-warning-as-irans-hackers-send-fake-invites-laced-with-malware/?sh=185f9c056ac1', \
        'citation': '3. Doffman, Zak. “Warning As Iranian State Hackers Target LinkedIn Users With Dangerous New Malware.” Forbes, Forbes Magazine, 22 July 2019.'})
    
    sources.append({'url': 'https://slate.com/technology/2019/04/linkedin-stalking-self-loathing-social-media-envy.html', \
        'citation': '4. Palus, Shannon and Heather Schwedel. “When It Comes to Feeling Bad About Yourself Online, Nothing Compares to LinkedIn.” Slate Magazine, Slate, 5 Apr. 2019,'})

    return render_template('notlinkedin.html', title='justkidding', items=sources)

@app.route('/projects')
def projects():

    # project: {'title': 'PROJECT TITLE', 'links': [{'url': 'LINK_1 URL', 'title': 'LINK_1 TITLE'}], 'desc': 'PROJECT DESCRIPTION'}
    project_list = []

    # Project 1. SaltyMicro

    project_SaltyMicro = {'title': 'SaltyMicro', 'links': [], 'desc': ''}

    project_SaltyMicro['links'].append({'url': '/pos/saltymicro', 'title': 'project-outline'})
    project_SaltyMicro['links'].append({'url': 'https://github.com/patbcole117/SBOv2', 'title': 'sbo.git'})
    project_SaltyMicro['links'].append({'url': 'https://github.com/patbcole117/SDCv2', 'title': 'sdc.git'})
    project_SaltyMicro['links'].append({'url': 'https://github.com/patbcole117/SUIv2', 'title': 'sui.git'})
    project_SaltyMicro['links'].append({'url': 'https://saltymicro.gyokuro.info/', 'title': 'website'})

    f = open('app/templates/txt/descsaltymicro.txt', 'r')
    project_SaltyMicro['desc'] = f.read()

    project_list.append(project_SaltyMicro)

    # Project 2. Homenet

    project_Homenet = {'title': 'Home Network', 'links': [], 'desc': ''}

    project_Homenet['links'].append({'url': '/pos/homenet', 'title': 'project-outline'})

    f = open('app/templates/txt/deschomenet.txt', 'r')
    project_Homenet['desc'] = f.read()

    project_list.append(project_Homenet)

    # Project 3. Patweb

    project_patweb = {'title': 'My Website', 'links': [], 'desc': ''}

    project_patweb['links'].append({'url': '/pos/patweb', 'title': 'project-outline'})
    project_patweb['links'].append({'url': 'https://github.com/patbcole117/PatWeb', 'title': 'patweb.git'})

    f = open('app/templates/txt/descpatweb.txt', 'r')
    project_patweb['desc'] = f.read()

    project_list.append(project_patweb)

    return render_template('projects.html', title='projects', project_list=sorted(project_list, key=lambda proj: proj['title']))

@app.route('/pos/saltymicro')
def posaltymicro():
    return render_template('/pos/saltymicro.html', title='saltymicro outline')

@app.route('/pos/homenet')
def poshomenet():
    return render_template('/pos/homenet.html', title='homenet outline')

@app.route('/pos/patweb')
def pospatweb():
    return render_template('/pos/patweb.html', title='patweb outline')