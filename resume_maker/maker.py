from __future__ import print_function
from mailmerge import MailMerge



docfile='resume_maker/my_resume.docx'

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    test='test sucess'
 )

document.write('test-output.docx')