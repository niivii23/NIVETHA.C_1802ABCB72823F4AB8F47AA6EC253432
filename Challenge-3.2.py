class Student :

  def _init_(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
  
  
  def sort_students(student_list):
    sorted_students = sorted(student_list,key = lambda student:student.cgpa,reverse=True)
    return sorted_students

student = [
  Student("pooja","A123","9.9"),
  Student("anitha","A124","9.8"),
  Student("hari","A1215","9.7"),
  Student("varshini","A126","9.6")
]
sorted_students=sort_students(students)

for student in sorted_students:
  print("name : {}, rollnumber : {}, cgpa: {}.".format(student.name,student.roll_number,student.cgpa))
