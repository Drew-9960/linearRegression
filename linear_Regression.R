# Linear Regression (Predictive)

head(cars, 6)

plot(cars$speed, cars$dist, xlab = "Speed", ylab = "Distance", main = "Scatter Plot")
scatter.smooth(cars$speed, cars$dist) # Generates line for graph

par(mfrow=c(1,2)) # (# of row, # of column), plotting in same area
plot(density(cars$speed), ylab = "Frequency",main = "Density Plot : Speed")
plot(density(cars$dist), ylab = "Frequency", main = "Density Plot : Distance")

cor(cars$speed, cars$dist)

# Explanatory regression model
linearmod = lm(dist ~ speed, data = cars) #Simple Regression (default alpha = 0.05)
linearmod
summary(linearmod)

# Predictive regression model 

set.seed(100)
training_rowindex = sample(1:nrow(cars), 0.8*nrow(cars)) #Row indicies for training data 
training_data = cars[training_rowindex,] #Model training data
test_data = cars[-training_rowindex,] #Model test data

lmodel = lm(dist ~ speed, data = training_data)
summary(lmodel)

#testing models performance 

dist_pred = predict(lmodel, test_data)
dist_pred

#evaluating model performance

install.packages("forecast")
library(forecast)

accuracy(test_data$dist, dist_pred)

#combine actual and predicted values 
test_data$dist

actual_pred = data.frame(cbind(actuals = test_data$dist, predicted = dist_pred))
actual_pred

































