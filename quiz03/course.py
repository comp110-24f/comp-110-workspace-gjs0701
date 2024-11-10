class Course:
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        if self.level < 400:
            return False
        else:
            for x in self.prerequisites:
                if x == prereq:
                    return True
            return False


def find_courses(list1: list[Course], prereq: str) -> list[str]:
    new_list = []
    for x in list1:
        if x.level >= 400:
            for y in x.prerequisites:
                if y == prereq:
                    new_list.append(x.name)
    return new_list
