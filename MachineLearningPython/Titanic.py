import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv') #загрузка таблицы данных с сайта
df['male'] = df['Sex'] == 'male' #создание булева столбца
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values # превращение объъекта DataFrame в массив numpy
y = df['Survived'].values #целевой столбец



model = LogisticRegression() #инициализациия класса
model.fit(X,y) #построение модели

y_pred = model.predict(X) #предсказание 
print((y == y_pred).sum()) # подсчет количество коррекктныъ предсказаний
print((y == y_pred).sum() / y.shape[0]) #процент верных предсказаний
print(model.score(X,y)) #то же самое что и в строке 13