import pandas as pd
import datetime


def load_employee_data():
    df = pd.read_csv('employee.csv')

    new_employees = [
        {'Id': 5, 'Name': 'Thanh Bình', 'Dob': '14/09/1999', 'Role': 'Data Scientist'},
        {'Id': 6, 'Name': 'Minh Anh', 'Dob': '27/05/2000', 'Role': 'UI/UX Designer'},
        {'Id': 7, 'Name': 'Văn Khoa', 'Dob': '03/12/2001', 'Role': 'DevOps Engineer'},
        {'Id': 8, 'Name': 'Thị Mai', 'Dob': '18/07/1998', 'Role': 'Product Manager'},
        {'Id': 9, 'Name': 'Quốc Bảo', 'Dob': '22/11/2002', 'Role': 'Web Developer'}
    ]

    new_df = pd.DataFrame(new_employees)
    df = pd.concat([df, new_df], ignore_index=True)

    return df

def calculate_age(dob_str):
    try:
        # Parse the date string in DD/MM/YYYY format
        dob = datetime.datetime.strptime(dob_str, '%d/%m/%Y')
        # Calculate age based on current date
        today = datetime.datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    except:
        return None


# Task 1:
def show_all_employees(df):
    print("\n--- All Employees Data ---")
    print(df.to_string(index=False))


# Task 2:
def filter_employees_born_in_2001(df):
    # Filter employees born in 2001
    born_in_2001 = df[df['Dob'].str.contains('/2001')]

    print("\n--- Employees Born in 2001 ---")
    if not born_in_2001.empty:
        print(born_in_2001.to_string(index=False))
    else:
        print("No employees born in 2001")

    return born_in_2001

# Task 3:
def export_top_3_oldest_employees(df):

    if 'Age' not in df.columns:
        df['Age'] = df['Dob'].apply(calculate_age)

    oldest_employees = df.sort_values(by='Age', ascending=False).head(3)

    print("\n--- TOP 3 Oldest Employees ---")
    print(oldest_employees.to_string(index=False))

    return oldest_employees


#Task 4
def filter_employees_with_tester_role(df):
    # Filter employees with Tester role
    testers = df[df['Role'] == 'Tester']

    print("\n--- Employees with Tester Role ---")
    if not testers.empty:
        print(testers.to_string(index=False))
    else:
        print("No employees with Tester role")

    return testers


# Task 5: Count the number of Employees by Role
def count_employees_by_role(df):
    # Group by Role and count
    role_counts = df.groupby('Role').size().reset_index(name='Count')

    print("\n--- Number of Employees by Role ---")
    print(role_counts.to_string(index=False))

    return role_counts



# Load and prepare the data
df = load_employee_data()
df['Age'] = df['Dob'].apply(calculate_age)
# Task 1: Export all Employee data
show_all_employees(df)
# Task 2: Filter employees born in 2001
filter_employees_born_in_2001(df)
# Task 3: Export TOP 3 oldest employees
export_top_3_oldest_employees(df)

# Task 4: Filter employees with Tester role
filter_employees_with_tester_role(df)

# Task 5: Count employees by role
count_employees_by_role(df)

