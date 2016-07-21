from bs4 import BeautifulSoup
import argparse

def createSoup(xml_source):
    soup = BeautifulSoup(open(xml_source), "lxml")

    print soup.find_all('monster')[33].prettify()


def parseArgs():
    parser = argparse.ArgumentParser(description = 'reads monster data from xml')
    parser.add_argument('--filename', '-f', required=True)

    return parser.parse_args()

def main():
    args = parseArgs()
    createSoup(args.filename)

if __name__ == "__main__":
    main()
