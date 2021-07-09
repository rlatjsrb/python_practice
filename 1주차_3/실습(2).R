age <- 20
age
age <- 30
age

# 숫자(numeric) 타입
age <- 20
class(age)

# 문자(character) 타입
name <- 'LJI'
class(name)

# 논리(logical) 타입
is_effective <- TRUE
is_effective

is_effective <- FALSE
is_effective

class(is_effective)

# 펙터(factor) 타입
# ('서울', '부산', '제주')의 전체 범주(factor) 중 '서울' 저장
sido <- factor('서울',c('서울', '부산', '제주'))

sido

class(sido)

levels(sido)

# NULL과 NA
a <- NULL
jumsu <- c(NA, 90, 100)

# Inf와 NaN
10 / 0
0 / 0
