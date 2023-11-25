import sys

if len(sys.argv) != 2:
    print("missing commant line argument ")
    sys.exit(1)


print(f"hellow!! {sys.argv[1]}")



# python sys_lib.py ansal
# output -> hellow!! ansal