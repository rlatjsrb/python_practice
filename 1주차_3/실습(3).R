students_age <- c(11, 12, 13, 20, 15, 21)
students_age

class(students_age)
length(students_age)

# 벡터 인덱싱
students_age[11]
students_age[3]
students_age[-1]

# 벡터 슬라이싱
students_age[1:3]
students_age[4:6]

# 벡터 데이터 추가, 갱신
score <- c(1, 2, 3)
score[1] <- 10
score[4] <- 4
score

# 벡터 데이터 타입
code <-  c(1, 12,'30')
class(code)
code

# 벡터 순열 생성
data <- c(1:10)
data

data1 <- seq(1,10)
data1

data2 <- seq(1, 10, by = 2)
data2

data3 <- rep(1, times = 5)
data3

data4 <- rep(1:3, each = 3)
data4

# 행렬
var1 <- c(1, 2, 3, 4, 5, 6)

x1 <- matrix(var1, nrow = 2, ncol = 3)
x1

x2 <- matrix(var1, ncol = 2)
x2

# 행렬 일부 데이터만 접근
x1[1,]
x1[, 1]
x1[2, 2]

# 행렬에 데이터 추가
x1
x1 <- rbind(x1, c(10, 10, 10))
x1 <- cbind(x1, c(20, 20, 20))
x1

# 데이터프레임
no <- c(10, 20, 30, 40, 50, 60, 70)
age <- c(18, 15, 13, 12,  10, 9, 7)
gender <- c('M', 'M', 'M', 'M', 'M', 'F', 'M')
students <- data.frame(no, age, gender)
students

# 데이터프레임 열의 이름과 행의 이름 확인인
colnames(students)
rownames(students)

# 데이터프레임 열의 이름과 행의 이름 수정정
colnames(students) <- c('no', '나이', '성별')
rownames(students) <- c('A', 'B', 'C', 'D', 'E', 'F', 'G')
students
colnames(students) <- c('no', 'age', 'gender')

# 데이터프레임 일부 데이터만 접근근
students$no
students$age

students[, 'no']
students[, 'age']

students[, 1]
students[, 2]

students['A',]
students[2, ]

students[3, 1]
students['A', 'no']

# 데이터프레임 열 데이터 추가
students$name <- c('이용', '준희', '이훈', '서희', 
                   '승희', '하정', '하준')
students

# 데이터프레임 행 데이터 추가
students['H',] <- c(80, 10, 'M', '홍길동')
tail(students)

# 배열
var1 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
arr1 <- array(var1, dim = c(2, 2, 3))
arr1

# 리스트
v_data <- c('02-111-2222', '01022223333')
m_data <- matrix(c(21:26), nrow = 2)
a_data <- array(c(31:36), dim = c(2, 2, 2))
d_data <- data.frame(address = c('seoul', 'busan'),
                     name = c('Lee', 'Kim'), stringsAsFactors = F)
list_data <- list(name = '홍길동',
                  tel = v_data,
                  score1 = m_data,
                  score2 = a_data,
                  freinds = d_data)

list_data$name
list_data$tel
list_data[1]
list_data$name
