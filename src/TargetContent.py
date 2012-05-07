#!/usr/bin/python

class TargetContent:
    Name = ""
    Depends = []
    Description = ""
    UnlessProp = []
    IfProp = []
    File_key = "";

    def __init__ (self, name, description="",depends=[], unlessprop="", ifprop="", file_key=""):
        self.Name = name
        self.Depends = depends
        self.Description = description
        self.UnlessProp = unlessprop
        self.IfProp = ifprop
        self.File_key = file_key;


