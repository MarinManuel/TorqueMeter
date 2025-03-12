# Torque Analyzer
a GUI for manual curation of the torque data files
![image](https://github.com/user-attachments/assets/5e0624c2-eeb8-4ca1-8325-f0fb014257a2)


# Usage
When first run, the software displays this screen:

![image](https://github.com/user-attachments/assets/e528673d-6ddc-4aaf-bf57-172c134933f7)


Use the `Result File...` button to create a new result Excel file (or open an existing one).

![image](https://github.com/user-attachments/assets/289cb568-6907-4ed9-9dfe-6abe7a8ee06a)



Then, use the `Load data files...` button to open the root folder containing all the data files to analyze (this should be the folder containing all the experiment folders with the date as the the folder name)

![image](https://github.com/user-attachments/assets/b6251af1-f913-479c-9cc9-b1f8aac62dd5)


The software then displays the first file

![image](https://github.com/user-attachments/assets/4114fe5b-fac3-44ee-a5ed-dc81b929b0c1)


When anlyzing a file, you have the option to:

- remove outliers by clicking the `Remove Outliers` check box (or press the `o` key).

![image](https://github.com/user-attachments/assets/71d63642-386f-4e24-ba7c-ae457525037b)

![image](https://github.com/user-attachments/assets/d8e96f34-aa90-4df3-ad65-d5837a5ede26)

- remove specific movement cycles from the analysis by double clicking on the shaded areas in the top two plot areas

![image](https://github.com/user-attachments/assets/b7e4cc10-7003-4403-a6f6-c263043ce33f)

![image](https://github.com/user-attachments/assets/26d14d49-9d7a-49a3-8787-ffaea6a49b19)

- reject the file altogether by clicking the red button (or press the `r` key). The software automatically moves to the next file in the list.

For instance, this file should be rejected because it does not contain enough cycles

![image](https://github.com/user-attachments/assets/a970643e-dabe-4e55-8599-6a8a2f16e454)

- when you are happy with your analysis, click the green button (or press the `a` key). The software automatically moves to the next file in the list.

![image](https://github.com/user-attachments/assets/31730adc-d0c6-4379-a378-db23c597e190)

The software automatically updates the data in the result file. You can restart your analysis where you left off by restarting the software and loading the previously-started result Excel file. Files already analyzed are not loaded unless the box `Skip already analyzed files` is unchecked.

# Resources
<a target="_blank" href="https://icons8.com/icon/4r5HpCBBbNn8/next-page">Next</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>. <a target="_blank" href="https://icons8.com/icon/LeIi2nYOolQt/back-to">Previous</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>. <a target="_blank" href="https://icons8.com/icon/Y5jV4wJL13np/open-folder">Open Folder</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
