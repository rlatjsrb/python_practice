data(Orange)
head(Orange)

model <- lm(circumference ~ age, Orange)
model

# 회귀계수
coef(model)
# 잔차
r <- residuals(model)
r[0:4]

# fitted() 함수로 model이 예측한 값 구하기
f <- fitted(model)

# residuals() 함수로 잔차 구하기
r <- residuals(model)

# 예측한 값에 잔차를 더하여 실제값과 동일한지 확인
# 예측한 값과 잔차 더하기
f[0:4] + r[0:4]

# 실제값
Orange[0:4, 'circumference']

# 잔차 제곱합
deviance(model)

# 예측
predict.lm(model, newdata = data.frame(age = 100))

summary(model)
