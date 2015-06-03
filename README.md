# Useful-Scripts
### tarDirEmail.sh
___
The initiative to this shell script is that I audit a undergraduate course and need my friend to send the course materials under her account to me.
#### Instruction:
- Modify `dir` to be the path of target directory;Better use relative path, or `tar` command will give warning

- Modify `dir` to be the email address of recipient;

- If want to exclude any file or folder, modify `excld`, but **no slash** in the end; and if there is more than one file or folder to exclude, this script won't support.

### cs349_automark.py
___
To mark assignments of CS349, we need to first mark in each student's folder, and then fill the final marks in a summary excel file(CS349-S15.xlsx). Since I am lazy to do repeating work, I create this script to autofill the summary excel file. The new summary excel file is `a*.xls`. 

The reason for creating a new excel file is that python cannot write to .xlsx file with default libraries.
#### Instruction:
The script should be under `a*package` folder, along with `CS349-S15.xlsx` and `a*` folder which contains all students' assignments. The directory tree looks like this:

```
+--- cs349_automark.py
|
+--- CS349-S15.xlsx
|
+--- a*
|     |
|     +--- userID_1
|               |
|               +--- a*marks.xls
|     +--- userID_2
|               |
|               +--- a*marks.xls
|     + ...
```

Then modify variables for assignment and variables for summary excel file.

