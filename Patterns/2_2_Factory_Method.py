# ***************** Real application: LinkeddIn and Facebook Profiles ***********************

from abc import ABCMeta,abstractmethod

class Section(metaclass=ABCMeta):
    """Abstract class"""
    def describe(self):
        pass
# Concrete classes
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")
    
class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

# Abstract creator class
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections=[]
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSection(self,section):
        self.sections.append(section)

# concrete creator classes
class LinkedIn(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())

class Facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())

if __name__ == "__main__":
    
    profile_type=input("Which type of Profile you want to be created(LinkedIn or Facebook): ")
    profile=eval(profile_type)()
    print("Creating Profile: ",type(profile).__name__)
    print("Profile has sections: ",profile.getSections())
    
