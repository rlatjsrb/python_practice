cor(Orange$circumference, Orange$age)

plot(Orange$circumference, Orange$age, col = 'red', pch = 19)

cor(iris[, 1:4])

cor.test(iris$Petal.Length, iris$Petal.Width, method = 'pearson')