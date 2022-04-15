# Faculty class
class Faculty:
    def __init__(self, name, profile):
        self.name = name
        self.profile = profile

    def printFaculty(self):
        print('Faculty Name:', self.name)
        print('Faculty Profile:', self.profile)


# Curriculum class
class Curriculum:
    def __init__(self, name, curriculumListDetails):
        self.name = name
        self.curriculumListDetails = curriculumListDetails

    def printCurriculum(self):
        print('Curriculum Name:', self.name)
        print('Curriculum Details:', self.curriculumListDetails)


# Course Class
class Course:
    def __init__(self, courseName, courseURL):
        self.courseName = courseName
        self.courseURL = courseURL
        self.courseDesc = ''
        self.courseLearnings = []
        self.courseRequirements = []
        self.courseFeatures = []
        self.courseCurriculums = []
        self.courseFaculties = []

    def set_courseDesc(self, desc):
        self.courseDesc = desc

    def add_courseLearnings(self, learning):
        self.courseLearnings.append(learning)

    def add_courseRequirements(self, requirement):
        self.courseRequirements.append(requirement)

    def add_courseFeatures(self, feature):
        self.courseFeatures.append(feature)

    def add_courseCurriculums(self, curriculum):
        self.courseCurriculums.append(curriculum)

    def get_courseCurriculumNames(self):
        curclNames = []
        for curr in self.courseCurriculums:
            curclNames.append(curr.name)
        return curclNames

    def add_courseFaculties(self, faculty):
        self.courseFaculties.append(faculty)

    def get_courseFaculty(self):
        faculties = []
        for faculty in self.courseFaculties:
            faculties.append(faculty.name)
        return faculties

    def printCourse(self):
        print('Course name:', self.courseName)
        print('Course desc:', self.courseDesc)
        print('Course URL:', self.courseURL)
        print('Course learnings:', self.courseLearnings)
        print('Course requirements:', self.courseRequirements)
        print('Course features:', self.courseFeatures)
        print('Course curriculums:')
        if isinstance(self.courseCurriculums, list):
            for i in self.courseCurriculums:
                if isinstance(i, Curriculum):
                    i.printCurriculum()
        print('Course faculties:')
        if isinstance(self.courseFaculties, list):
            for i in self.courseFaculties:
                if isinstance(i, Faculty):
                    i.printFaculty()


# SubTopic Class
class SubTopic:
    def __init__(self, subTopicName, subTopicURL, subTopicCourses=None):
        self.subTopicName = subTopicName
        self.subTopicURL = subTopicURL
        self.subTopicCourses = []

    def add_subTopicCourse(self, course):
        self.subTopicCourses.append(course)

    def printSubTopic(self):
        print("SubTopic Name:", self.subTopicName)
        print("SubTopic URL:", self.subTopicURL)
        if isinstance(self.subTopicCourses, list):
            for i in self.subTopicCourses:
                if isinstance(i, Course):
                    i.printCourse()


# MainCourse Class
class MainCourse:
    def __init__(self, courseName, subTopics=None):
        self.courseName = courseName
        self.subTopics = []

    def add_subTopic(self, subTopic):
        self.subTopics.append(subTopic)

    def get_subTopics(self):
        return self.subTopics

    def printMainCourse(self):
        print("CourseName:", self.courseName)
        if isinstance(self.subTopics, list):
            for i in self.subTopics:
                if isinstance(i, SubTopic):
                    i.printSubTopic()