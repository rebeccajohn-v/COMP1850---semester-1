import rect
import person as p
import datetime

x = rect.Rectangle(3,4)
y = rect.Rectangle(2,2)


p1 = p.Person("Rebecca Johndice Val", datetime.date(2008,11,18))
p2 = p.Person("Yassssmina Zalfreezi Ameena",datetime.date(2003,10,29))


print(p1.is_birthday())
print(p2.is_birthday())
print(p1.initials())
print(p2.initials())

#print(x.is_square())
#print(y.is_square())
# print(x.area())
# print(x.perimeter())
