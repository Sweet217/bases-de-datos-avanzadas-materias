import matplotlib.pyplot as plt
import  pandas as pd

df = pd.read_csv('data.csv')


plt.figure(figsize=(8, 6))
plt.hist(df['salary'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df['hours_worked'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Hours Worked')
plt.ylabel('Frequency')
plt.title('Labor hours distribution')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df['days_worked'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Days worked')
plt.ylabel('Frequency')
plt.title('Labour days distribution')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['salary'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')
plt.grid(True)
plt.tight_layout()
plt.show()


#Site activity not working properly
df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(12, 6))
plt.scatter(df['date'], df['hours_worked'], color='skyblue', alpha=0.5)
plt.xlabel('Date')
plt.ylabel('Hours Worked')
plt.title('Site Activity by Date and Hours Worked')
plt.tight_layout()
plt.show()

#Map of mexico showing the average salary
#No pude poner el mapa, mostrare solo como barras 
salary_by_state = df['state'].value_counts().reset_index()
salary_by_state.columns = ['State', 'Salary']

plt.figure(figsize=(12,8))
plt.bar(salary_by_state['State'], salary_by_state['Salary'], color='skyblue', edgecolor = 'black')
plt.xlabel('State')
plt.ylabel('Salary')
plt.title('Salary by state')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['hours_worked'], df['salary'], color='skyblue', alpha=0.5)
plt.xlabel('Hours Worked')
plt.ylabel('Salary')
plt.title('Salary vs Hours Worked')
plt.grid(True)
plt.tight_layout()
plt.show()

#Jobs offer by state
jobs_by_state = df['state'].value_counts().reset_index()
jobs_by_state.columns = ['State', 'Number of Job Offers']

plt.figure(figsize=(12,8))
plt.bar(jobs_by_state['State'], jobs_by_state['Number of Job Offers'], color='skyblue', edgecolor = 'black')
plt.xlabel('State')
plt.ylabel('Number of job offers')
plt.title('Job offers by state')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

