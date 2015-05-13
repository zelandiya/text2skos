__author__ = 'a_medelyan'

# Given a flat list of terms in a text file, creates an SKOS rdf file


def write_skos_header(output_file, header_file, url):
    with open(header_file) as f:
        with open(output_file, "w") as f1:
            for line in f:
                if 'URL' in line:
                    line = line.replace('URL', url)
                f1.write(line)
            f1.write('\n')


def convert_text_to_skos(text_file, skos_file, url):
    output_file = open(skos_file, 'a')
    with open(text_file, 'Ubr') as f:
        count = 0
        for line in f:
            term = line.rstrip().decode('latin-1').encode('utf-8')

            if '&' in term:
                term = term.replace('&', '&amp;')

            count += 1

            output_file.write('\t<skos:Concept rdf:about=\"' + url + '/' + str(count) + '\">\n')
            output_file.write('\t\t<skos:prefLabel xml:lang="en">' + term + '</skos:prefLabel>\n')

            output_file.write('\t</skos:Concept>\n')

    f.close()

    output_file.write('</rdf:RDF>\n')
    output_file.close()

if __name__ == "__main__":

    import sys

    if len(sys.argv) != 4:
        print 'usage: {} PATH_TO_TXT_FILE PATH_TO_SKOS_FILE URL'.format(sys.argv[0])
        sys.exit(1)

    text_file = sys.argv[1]
    skos_file = sys.argv[2]
    url = sys.argv[3]

    write_skos_header(skos_file, "skos_header.txt", url)
    convert_text_to_skos(text_file, skos_file, url)
