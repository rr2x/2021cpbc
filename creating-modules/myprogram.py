# from <file> import <function>
# from mymodule import my_func
# my_func()

# important to have an empty __init__.py per folder
# from <folder>.<subfolder> import <file>
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

# <file>.<function>
some_main_script.report_main()
mysubscript.sub_report()
