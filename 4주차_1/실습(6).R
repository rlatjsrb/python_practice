fit <- princomp(iris[, 1:4], cor = TRUE)
# 결과를 fit에 저장
summary(fit)
loadings(fit)
screeplot(fit, type = 'lines', main = 'scree plot')
