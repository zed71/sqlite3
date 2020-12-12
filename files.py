import sqlite3

# import os

fileList = (
    "data.pdf",
    "Hello.txt",
    "information.docx",
    "myImage.png",
    "myMovie.mp4",
    "myPhoto.jpg",
    "World.txt",
)

conn = sqlite3.connect("files.db")

with conn:
    cur = conn.cursor()
    cur.execute(
        "Create Table If Not Exists tbl_files( \
                id Integer Primary Key Autoincrement, \
                col_files Text)"
    )
    conn.commit()
conn.close()

conn = sqlite3.connect("files.db")

with conn:
    cur = conn.cursor()
    file_ = [(f,) for f in fileList if f.endswith(".txt")]
    cur.executemany("Insert Into tbl_files(col_files) Values (?);", file_)
    conn.commit()
    cur.execute('Select col_files From tbl_files Where col_files Like "%txt"')
    tup_files = cur.fetchall()
    list_files = ["".join(i) for i in tup_files]
    for item in list_files:
        msg = "The files with file types .txt from this directory are: \n>>>: {}".format(
            item
        )
        print(msg)
conn.close()
