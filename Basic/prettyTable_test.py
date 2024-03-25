
""" pip install prettytable
    https://pypi.org/project/prettytable/
    시각적으로 매력적인 ASCII 테이블 형식으로 표 형식의 데이터를 쉽게 표시하기 위한 간단한 Python 라이브러리
    A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
"""

from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

# Define the table's columns
table.field_names = ["Name", "Age", "City"]

# Add rows to the table
table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "Los Angeles"])
table.add_row(["Charlie", 35, "Chicago"])

# Print the table
print(table)

# Changing Column Alignment:
table.align["Name"] = "l"  # Left align names
table.align["Age"] = "c"  # Center align age
table.align["City"] = "r"  # Right align city names

# Sorting by a Column:
table.sortby = "Age"

print("Change alignment, Sort! ")

# Print the table
print(table)

# Or, for more customization:
table.border = True
table.junction_char = "*" 

print(" 지정 컬럼만 노출, 모서리 *로 변경  ")

# Printing Only Specific Columns:
print(table.get_string(fields=["Name", "City"]))

# HTML 형식으로 테이블 표시
# PrettyTable은 HTML 형식으로 테이블을 인쇄합니다 <table>. ASCII 형식과 마찬가지로 실제로 문자열 표현을 얻을 수 있습니다 
# get_html_string(). . HTML 인쇄는 ASCII 인쇄 와 동일한 방식으로 fields, start, 및 인수를 지원합니다.

print('\n\n',table.get_html_string(attributes={"id":"my_table", "class":"red_table"}))


# Changing the Style of the Table:
# Customizing the table's appearance
table.border = False
table.header = False
table.horizontal_char = ' '
table.vertical_char = ' '
table.junction_char = ' '

print("Change Style! ")

# Print the table
print(table)


