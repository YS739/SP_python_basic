# print('hello sparta')

# a = 3
# b = 2
#
# print(a%b)

# a = 'yunny'
#
# print(a)
#
# a = (3 == 2)
#
# print(a)
#
# first_name = 'yunny'
# last_name = ' jeong'
#
# print(first_name+last_name)

# a = '2'
# b = str(2)
#
# print(a+b)

# text = 'fafasfsdf'
#
# result = text[:]
# print(result)

# 퀴즈(내가 푼 것) = 수업 코드
# text = 'sparta'
# result = text[:3]
# print(result)
#
# #퀴즈(내가 푼 것) = 수업 코드
# phone = "02-123-1234"
# result = phone.split('-')[0]
# print(result)

# 리스트와 딕셔너리
# a_list = ['사과','감', 2, '배', False, ['포도','귤']]
# print(a_list[5][0])

# a_list = [1,5,6,3,7]
# a_list.append(99)
# a_list.append(100)
# print(a_list)

# a_list = [1,5,6,3,7]
# result = a_list[-1]
#
# print(result)
#
# a_list = [1,5,6,3,7]
# a_list.sort(reverse=True)
# print(a_list)

# a_list = [1,3,6,7,8]
# result = (1 in a_list)
#
# print(result)

# a_dict = {'name':'jun','age':30, 'friend':['영희','철수']}
# result = a_dict['friend'][0]
# print(result)
#
# a_dict = {'name':'jun','age':30, 'friend':['영희','철수']}
# a_dict['height']=180
# print('height' in a_dict)
#
#
# people = [{'name':'jun','age':29},
#           {'name':'hyun','age':28}]
# print(people[1]['age'])

# 퀴즈(내가 한 것) = 수업 코드
# people = [
#     {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
#     {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
#     {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
#     {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
# ]
#
# print(people[2]['score']['science'])


# money = 1000
# if money >3800:
#     print('take a cap')
# elif money > 1200:
#     print('take a bus')
# else:
#     print('take a walk')
#     print('what should we take?')


# #loop
# fruits = ['사과','배','감','포도','딸기']
# for fruit in fruits:
#     print(fruit)

# people = [
#     {'name': 'bob', 'age': 20},
#     {'name': 'carry', 'age': 38},
#     {'name': 'john', 'age': 7},
#     {'name': 'smith', 'age': 17},
#     {'name': 'ben', 'age': 27},
#     {'name': 'bobby', 'age': 57},
#     {'name': 'red', 'age': 32},
#     {'name': 'queen', 'age': 25}
# ]

# for i, person in enumerate(people):
#     name = person['name']
#     age = person['age']
#     print(i, name, age)
#     if i > 2:
#         break

# 퀴즈1(내가 한 것) = 수업 코드
# num_list = [1,2,3,6,3,2,4,5,6,2,4]
# for number in num_list:
#     if number % 2 == 0:
#         print(number)

# 퀴즈2(내가 한 것)
# num_list = [1,2,3,6,3,2,4,5,6,2,4]
# for number in num_list:
#     if number % 2 == 0:
#         print(len.number)
#수업 코드
# num_list = [1,2,3,6,3,2,4,5,6,2,4]
# count = 0
# for number in num_list:
#     if number % 2 == 0:
#         count += 1
# print(count)

# 퀴즈3(내가 한 것)
# num_list = [1,2,3,6,3,2,4,5,6,2,4]
#
# for num in num_list:
#     sum += num
#     print(sum)
#
# # 수업 코드
# num_list = [1,2,3,6,3,2,4,5,6,2,4]
# sum = 0
# for num in num_list:
#     sum += num
# print(sum)

# 퀴즈4. 수업 코드
# num_list = [1,2,3,6,3,2,4,5,6,2,4]
# max = 0
# for num in num_list:
#     if max < num:
#         max = num
# print(max)

# 함수
# def sum(a,b):
#     print('더하기를 하셨네요!')
#     return a+b
# result = sum(1,2)
# print(result)
#
# def bus_rate(age):
#     if age > 65:
#         return 0
#     elif age >20:
#         return 1200
#     else:
#         return 750
# myrate = bus_rate(15)
# print(myrate)

# 퀴즈(내가 한 것)
# def check_gender(pin):
#     check_gender('120101-2030455')
#     check_gender('120101-1030455')
#     check_gender('120101-4030455')
#
# for check in check_gender(pin):
#     check = int(check_gender.split('-')[:1])
#     if check % 2 == 0:
#         print('여성입니다.')
#     else:
#         print('남성입니다.')
        
#수업 코드
# def check_gender(pin):
#     num = pin.split('-')[1][:1]
#     if int(num) % 2 == 0:
#         print('여성')
#     else:
#         print('남성')
#
# check_gender('123456-2003333')
# check_gender('123456-1003333')
# check_gender('123456-4003333')

#
# student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
# student_b = ['물리1','수학1','미술','화학2','체육']
# a_set = set(student_a)
# b_set = set(student_b)
#
# print(a_set - b_set)

#
# scores = [
#     {'name':'영수','score':70},
#     {'name':'영희','score':65},
#     {'name':'기찬','score':75},
#     {'name':'희수','score':23},
#     {'name':'서경','score':99},
#     {'name':'미주','score':100},
#     {'name':'병태','score':32}
# ]
# for s in scores:
#     name = s['name']
#     score = s['score']
#     print(name+'의 점수는' +str(score)+'점입니다.')
#     print(f'{name}의 점수는 {score}점입니다.')

# people = [
#     {'name': 'bob', 'age': 20},
#     {'name': 'carry', 'age': 38},
#     {'name': 'john', 'age': 7},
#     {'name': 'smith', 'age': 17},
#     {'name': 'ben', 'age': 27},
#     {'name': 'bobby'},
#     {'name': 'red', 'age': 32},
#     {'name': 'queen', 'age': 25}
# ]
# 
# for person in people:
#     try:
#         if person['age'] > 20:
#             print(person['name'])
#     except:
#         print(person['name'],'에러입니다')


# num = 3
#
# result = '짝수' if num % 2 == 0 else '홀수'
# print(f'{num}은 {result}입니다')

# 
# a_list = [1,3,2,5,1,2]
# 
# b_list = [a*2 for a in a_list]
# print(b_list)


people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]
# result = filter(lambda x: x['age'] > 20, people)
# # result = map(lambda person: ('성인' if person['age'] > 20 else '청소년'), people)
# print(list(result))

# class Monster():
#     hp = 100
#     alive = True
#     def damage(self, attack):
#         self.hp = self.hp - attack
#         if self.hp < 0:
#             self.alive = False
#     def status_check(self):
#         if self.alive:
#             print('살았다')
#         else:
#             print('죽었다')
#
# m1 = Monster()
# m1.damage(150)
# m1.status_check()
#
# m2 = Monster()
# m2.damage(90)
# m2.status_check()



def cal2(a, b=3):
    return a + 2 * b

print(cal2(4, 2))