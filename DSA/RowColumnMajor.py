def rowmajor(baseaddress,elesize, total_row,total_column, row_idx, col_idx):
    return baseaddress + elesize*(row_idx*total_column+col_idx)

def colmajor(baseaddress,elesize, total_row,total_column, row_idx, col_idx):
    return baseaddress + elesize*(row_idx+col_idx*total_row)

base_address = 1020
element_size = 4        # Size of an integer in bytes
total_rows = 4          # arr[4][5]
total_cols = 5          # arr[4][5]
row_idx = 1             # Target arr[1][2]
col_idx = 2


target_address = rowmajor(base_address, element_size, total_rows,total_cols, row_idx, col_idx)
print(target_address)
#   	Col 0	Col 1	Col 2   Col 3	Col 4
# Row 0	1020	1024	1028	1032	1036
# Row 1	1040	1044	1048 👈	1052	1056
# Row 2	1060	1064	1068	1072	1076
# Row 3	1080	1084	1088	1092	1096

target_address = colmajor(base_address, element_size, total_rows,total_cols, row_idx, col_idx)
print(target_address)
#       Col 0	Col 1	Col 2   Col 3	Col 4
# Row 0	1020	1036	1052	1068	1084
# Row 1	1024	1040	1056 👈	1072	1088
# Row 2	1028	1044	1060	1076	1092
# Row 3	1032	1048	1064	1080	1096