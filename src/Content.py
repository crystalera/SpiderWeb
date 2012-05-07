#!/usr/bin/python

from TargetContent import TargetContent
class Content:
    file_name = []
    contents = []
    targets = []

    def initialize(self):
        self.populate_targets()

    def add(self, name,tree):
        if not name in self.file_name:
            self.file_name.append(name)

        for target in tree.findall("target"):
            self.contents.append((target, name))

    def print_all(self):
        for indv in self.contents:
            print(indv)

    def populate_targets(self):

        name = ""
        description = ""
        depends = []
        ifprop = ""
        unlessprop = ""
        file_key="";

        for target,file_name in self.contents:

            if 'name' in target.attrib:
                name = target.attrib['name'].strip()

            if 'description' in target.attrib:
                description = target.attrib['description'].strip()

            if 'depends' in target.attrib:
                depends = target.attrib['depends'].split(',')

            if 'if' in target.attrib:
                ifprop = target.attrib['if'].strip()

            if 'unless' in target.attrib:
                unlesssprop = target.attrib['unless'].strip()

            self.targets.append(TargetContent(name, description,depends, unlessprop, ifprop,file_name))


    def print_targets(self):
        for indv in self.targets:
            print "" , u'\u2500' * len(indv.Name)
            print u'\u2502' + indv.Name + u'\u2502'
            print "" , u'\u2500' * len(indv.Name)

    def get_file_targets(self, file_name):
        targets = []

        for target in self.targets:
            if target.File_key == file_name:
                targets.append(target)
        return targets;

    def get_target_dependencies(self, target_name):
        full_dependencies = ""
        for target in self.targets:
            if target.Name == target_name:
                if target.Depends == []:
                    return "No Dependencies"
                else:
                    for depend in target.Depends:
                        if (full_dependencies == ""):
                            full_dependencies = depend
                        else:
                            full_dependencies += " \n|\n " + depend
                        #self.get_target_dependencies(depend)
        return full_dependencies
            
    def get_target(self, target_name):
        for indv in self.targets:
            if indv.name == target_name:
                return indv
        return None;
            

