# Torque Analyzer
a GUI for manual curation of the torque data files
![Screenshot from 2024-12-17 16-47-47](https://github.com/user-attachments/assets/c58c1b73-ef7c-4dcf-885b-1f00db7c8375)

# Usage
When first run, the software displays this screen:

![Screenshot from 2024-12-17 16-43-46](https://github.com/user-attachments/assets/4c7b8f45-888a-4c61-a4de-5af3d6580aa0)

Use the `Result File...` button to create a new result Excel file (or open an existing one).

![Screenshot from 2024-12-17 16-58-26](https://github.com/user-attachments/assets/59608c60-134a-406b-9606-ae5fd62abf70)


Then, use the `Load data files...` button to open the root folder containing all the data files to analyze (this should be the folder containing all the experiment folders with the date as the the folder name)

![Screenshot from 2024-12-17 16-45-57](https://github.com/user-attachments/assets/f1289dc7-bc6b-4a9f-8afd-9acbb5655fcf)

The software then displays the first file

![Screenshot from 2024-12-17 16-46-21](https://github.com/user-attachments/assets/99bb797b-dd5f-4422-855c-88ae14c57953)

When anlyzing a file, you have the option to:

- remove outliers by clicking the `Remove Outliers` check box (or press the `o` key).

![Screenshot from 2024-12-17 16-48-37](https://github.com/user-attachments/assets/d92a7b97-3868-40b8-800d-500044ef9d17)

![Screenshot from 2024-12-17 16-49-14](https://github.com/user-attachments/assets/46423371-7dc2-44cf-b842-6837129e383c)

- remove specific movement cycles from the analysis by double clicking on the shaded areas in the top two plot areas

![Screenshot from 2024-12-17 16-47-10](https://github.com/user-attachments/assets/369a30f5-30b6-4b33-956c-f6e93730717d)

![Screenshot from 2024-12-17 16-47-47](https://github.com/user-attachments/assets/9ac9ee3e-80cc-45fc-8f02-9d13b69795fc)

- reject the file altogether by clicking the red button (or press the `r` key). The software automatically moves to the next file in the list.

![Screenshot from 2024-12-17 16-49-43](https://github.com/user-attachments/assets/ec4e8101-40c2-4855-a5f9-4148316772eb)

For instance, this file should be rejected because it does not contain enough cycles

The software automatically updates the data in the result file. You can restart your analysis where you left off by restarting the software and loading the previously-started result Excel file. Files already analyzed are not loaded unless the box `Skip already analyzed files` is unchecked.

# Resources
<a target="_blank" href="https://icons8.com/icon/4r5HpCBBbNn8/next-page">Next</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>. <a target="_blank" href="https://icons8.com/icon/LeIi2nYOolQt/back-to">Previous</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>. <a target="_blank" href="https://icons8.com/icon/Y5jV4wJL13np/open-folder">Open Folder</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

[Tutorial](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/) for PyInstaller
# Create exe with PyInstaller
In Windows virtual box, open conda, activate GUI env, run:
```shell
pyinstaller TorqueAnalyzer.spec
```
