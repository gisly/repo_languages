#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'gisly'
import codecs
import json
import os


def read_lines_from_filename(input_filename):
    lines = []
    with codecs.open(input_filename, 'r', 'utf-8') as fin:
        for line in fin:
            lines.append(line.strip())
    return lines

def read_lines_from_filename_skipping(input_filename, line_symbol_to_skip):
    lines = []
    with codecs.open(input_filename, 'r', 'utf-8') as fin:
        for line in fin:
            if not line.startswith(line_symbol_to_skip):
                lines.append(line.strip())
    return lines

def read_numbers_from_filename(input_filename):
    nums = []
    with codecs.open(input_filename, 'r', 'utf-8') as fin:
        for line in fin:
            nums.append(float(line.strip()))
    return nums


def write_line_to_file(line, fout):
    fout.write(line + os.linesep)


def read_json(input_filename):
    with codecs.open(input_filename, 'r', 'utf-8') as json_data:
        return json.load(json_data)


def write_json_array(data_arr, comment, output_filename):
    with codecs.open(output_filename, 'w', 'utf-8') as outfile:
        outfile.write(comment + os.linesep)
        json.dump(data_arr, outfile, ensure_ascii=False)


def write_array_of_arrays_to_filehandle(data_arr, outfile, delimiter):
   for element in data_arr:
       outfile.write(delimiter.join(element) + os.linesep)