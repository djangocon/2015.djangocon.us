import click
import os

from bs4 import BeautifulSoup


def get_all_html_files():
    filenames = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                filenames.append(os.path.join(root, file))
    return filenames


def process(filename):
    with open(filename, 'r') as input_buffer:
        soup = BeautifulSoup(input_buffer.read(), 'html.parser')

    soup = process_anchors(soup)
    soup = process_form_actions(soup)
    soup = process_images(soup)
    soup = process_css_links(soup)
    soup = process_js_scripts(soup)

    click.echo('writing {0}'.format(filename))

    with open(filename, 'w') as output_buffer:
        output_buffer.write(str(soup))


def process_anchors(soup):
    anchors = soup.find_all('a', href=True)

    for anchor in anchors:
        link = anchor['href']
        if not link.startswith('http'):

            if link.startswith('../'):
                link = link.replace('../', '/')

            if link.endswith('.1.html'):
                link = link.replace('.1.html', '/')

            if link.startswith('index.html'):
                link = link.replace('index.html', '/')

            if link.endswith('/index.html'):
                link = link.replace('/index.html', '/')

            link = '/{0}'.format(link.lstrip('/'))

            anchor['href'] = link

        else:

            if link.startswith('https://2015.djangocon.us/'):
                link = link.replace('https://2015.djangocon.us/', '/')

            if link.startswith('http://djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('http://djangocon-us.global.ssl.fastly.net/', '/')

            if link.startswith('https://djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('https://djangocon-us.global.ssl.fastly.net/', '/')

            anchor['href'] = link

    return soup


def process_css_links(soup):
    anchors = soup.find_all('link', href=True)

    for anchor in anchors:
        link = anchor['href']

        if not link.startswith('http'):

            if link.startswith('../'):
                link = link.replace('../', '/')

            if link.startswith('/djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('/djangocon-us.global.ssl.fastly.net/', '/')

            if link.startswith('//djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('//djangocon-us.global.ssl.fastly.net/', '/')

            link = '/{0}'.format(link.lstrip('/'))

            anchor['href'] = link

        elif not link.startswith('https'):
            link = link.replace('http://', '//')
            anchor['href'] = link

        else:

            if link.startswith('https://2015.djangocon.us/'):
                link = link.replace('https://2015.djangocon.us/', '/')

            if link.startswith('http://djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('http://djangocon-us.global.ssl.fastly.net/', '/')

            if link.startswith('https://djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('https://djangocon-us.global.ssl.fastly.net/', '/')

            anchor['href'] = link

    return soup


def process_form_actions(soup):
    anchors = soup.find_all('form', action=True)

    for anchor in anchors:
        link = anchor['action']

        if not link.startswith('http'):

            if link.startswith('../'):
                link = link.replace('../', '/')

            if link.startswith('index.html'):
                link = link.replace('index.html', '/')

            if link.endswith('/index.html'):
                link = link.replace('/index.html', '/')

            link = '/{0}'.format(link.lstrip('/'))

            anchor['action'] = link

    return soup


def process_images(soup):
    anchors = soup.find_all('img', src=True)

    for anchor in anchors:
        link = anchor['src']

        if not link.startswith('http'):

            if link.startswith('../'):
                link = link.replace('../', '/')

            link = '/{0}'.format(link.lstrip('/'))

            anchor['src'] = link

        else:

            if link.startswith('https://2015.djangocon.us/'):
                link = link.replace('https://2015.djangocon.us/', '/')

            if link.startswith('https://djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('https://djangocon-us.global.ssl.fastly.net/', '/')

            anchor['src'] = link

    return soup


def process_js_scripts(soup):
    anchors = soup.find_all('script', src=True)

    for anchor in anchors:
        link = anchor['src']

        if not link.startswith('http'):

            if link.startswith('../'):
                link = link.replace('../', '/')

            link = '/{0}'.format(link.lstrip('/'))

            anchor['src'] = link

        else:

            if link.startswith('https://2015.djangocon.us/'):
                link = link.replace('https://2015.djangocon.us/', '/')

            if link.startswith('https://djangocon-us.global.ssl.fastly.net/'):
                link = link.replace('https://djangocon-us.global.ssl.fastly.net/', '/')

            anchor['src'] = link

    return soup


@click.command()
def main():
    filenames = get_all_html_files()
    for filename in filenames:
        process(filename)


if __name__ == '__main__':
    main()
