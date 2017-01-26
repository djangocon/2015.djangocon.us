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

                link = '/{0}'.format(link.lstrip('/'))

                anchor['href'] = link

    click.echo('writing {0}'.format(filename))
    with open(filename, 'w') as output_buffer:
        output_buffer.write(str(soup))

    # links = soup.find_all('links', src=True)
    # click.echo(links)


@click.command()
def main():
    filenames = get_all_html_files()
    for filename in filenames:
        process(filename)


if __name__ == '__main__':
    main()
