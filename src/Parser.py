#!/usr/bin/python

import xml.etree.ElementTree as ET
import os, fnmatch
from Content import Content

class Parser:

    HOLDER = Content()
    def __init__ (self, root_dir):
        
        self.ROOT_DIR = root_dir;

    def initialize(self):
        self.find_all_files()
        self.list_all_files()
        self.HOLDER.initialize()


    def find_all_files(self):

        xml_files =  self.locate_files("*.xml", self.ROOT_DIR)
        
        for xml_file in xml_files:
            self.is_ant_xml(xml_file)

    def is_ant_xml(self, file_name):
        try:
            tree = ET.parse(file_name)

            if (tree.getroot().tag == 'project'):
                self.HOLDER.add(file_name, tree)
        except:
            print(file_name + "is not an xml file")

    def list_all_files(self):
        self.HOLDER.print_all()

    def get_all_file_names(self):
        return self.HOLDER.file_name

    def get_targets_by_file(self, file_name):
        return self.HOLDER.get_file_targets(file_name)

    def locate_files(self, pattern, root=os.curdir):
        '''Locate all files matching supplied filename pattern in and below
        supplied root directory.'''
        for path, dirs, files in os.walk(os.path.abspath(root)):
            for filename in fnmatch.filter(files, pattern):
                yield os.path.join(path, filename)
