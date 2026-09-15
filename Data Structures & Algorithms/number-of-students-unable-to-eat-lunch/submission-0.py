class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = list(reversed(sandwiches))

        j = len(sandwiches)-1;
        while students:
            
            if sandwiches[j] not in students:
                return len(students)
            
            student = students.pop(0)
                
            if student == sandwiches[j]:
                sandwiches.pop()
                j -= 1
            else:
                students.append(student)

        return len(students)