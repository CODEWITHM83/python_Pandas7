import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "salary":[50000,60000,45000,52000,49000,7000,40000,58000],
    "Performance Score":[85,90,78,92,88,95,88,89]

}
df=pd.DataFrame(data)
# -----using singler Condition-------------------------
high_salary=df[df['salary']>50000]
print('Employee With salary > 50000')
print(high_salary)
# -------------using multiple Condition---------------------
#  -----Filtering rows salary > 50k & age > 30k
filter=df[(df['Age'] >30) & (df['salary']> 50000)]
print(f'Employee list Age > 30 + Salary > 50000')
print(filter)
# -------------usint OR condition-------------
filter_or=df[(df['Age']> 35) | (df["Performance Score"]> 90)]
print(filter_or)

