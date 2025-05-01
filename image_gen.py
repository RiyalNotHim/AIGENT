from os import system, listdir

cookie="11uXWRYBQe5IJ97j9iSkf3vlrrvUw09w9LG09rb9zUFdSlPAJv3pn5ArWX_q__Ae2wlvVeCZJY0YVNqmVdjhlZu26_QzwJeyNj68IPoSeq-XfmnHEmpQilVRVMUOtFU8ViuEzwJgFHnv1FFXjDUHZnsM5m6NsOTC6NjwyrNDEpSJKJDEn4Jpo4yYSU-gBM5IqFsv-Abl8j8U0iv7U1ymRjlyEc6OApAOpjgUssSAMb_c"
def Genarate_Image(prompt):
    command = f'python -m BingImageCreator --prompt "{prompt}" -U "{cookie}"'
    system(command)
    return listdir('output')

Genarate_Image('a horse with a dog')