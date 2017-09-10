#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = "gisly"

import sys
import codecs
import github_api
import file_utils

MAIN_LANGUAGE_FILENAME = 'resources/language_names.txt'
DELIMITER = '\t'
COMMENT_LABEL = '#'


def search_languages_on_github(language_list_filename, output_filename):
    language_names_english = file_utils.read_lines_from_filename_skipping(language_list_filename, COMMENT_LABEL)
    with codecs.open(output_filename, 'w', 'utf-8') as outfile:
        total_num = len(language_names_english)
        for index, language_name_english in enumerate(language_names_english):
            result = search_github_repos(language_name_english)
            if result:
                file_utils.write_array_of_arrays_to_filehandle(result, outfile, DELIMITER)
            if index % 10 == 0:
                print('language # %s ot of %s' % (index, total_num))


def search_github_repos(text_to_search):
    repos = github_api.search_repos(text_to_search)
    if repos:
        res = []
        for rep in repos:
            rep_res = [ text_to_search, rep['html_url']]
            if rep.get('homepage'):
                rep_res.append(rep.get('homepage'))
            res.append(rep_res)
        return res
    return []


def main():
    if len(sys.argv) < 2:
        print('usage: search_repos.py {output_filename} {language_list_filename}')
        return
    output_filename = sys.argv[1]
    if len(sys.argv) > 2:
        language_list_filename = sys.argv[2]
    else:
        language_list_filename = MAIN_LANGUAGE_FILENAME
    search_languages_on_github(language_list_filename, output_filename)


if __name__ == '__main__':
    main()