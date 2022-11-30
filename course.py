import os, re, string, pathlib,ffmpeg, datetime
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

f = open(os.getcwd().split('/')[-1]+".txt", "w", encoding='utf-8')
f.writelines(["TYPE,CONTENT,DESCRIPTION,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE\n"])
dirs = sorted([x  for x in os.listdir() if isfloat(x.split()[0])], key=lambda s: int(re.search(r'\d+', s).group()))
total = 0
for section in dirs:
    section_total = 0.
    if os.path.isdir(os.path.join(os.getcwd(), section)):
        curdir = os.path.join(os.getcwd(), section)

        lectures = sorted([x  for x in os.listdir(curdir) if isfloat(x.split()[0])], key=lambda s: int(re.search(r'\d+', s).group()))
        lecture_list = []
        order_no = '0'
        for lecture in lectures:
            indent = '2'
            if order_no == lecture.split('.')[0]:
                indent = '3'
            order_no = lecture.split('.')[0]
            filename = pathlib.Path(os.path.join(os.getcwd(), section,lecture))
            ft = lecture.split('.')[-1]
            if ft in ['mp4', 'avi']:
                duration = float(ffmpeg.probe(os.path.join(curdir,lecture))['format']['duration'])
                lecture_list.append("task,"+filename.stem+","+str(datetime.timedelta(seconds=duration)).split('.')[0]+",4,"+indent+",,,,,Asia/Ashgabat\n")
                section_total = section_total + duration 
            if ft == 'html':
                lecture_list.append("task,"+filename.stem+",,4,"+indent+",,,,,Asia/Ashgabat\n")

    f.writelines(["task,"+section+","+str(datetime.timedelta(seconds=section_total)).split('.')[0]+",4,1,,,,,Asia/Ashgabat\n"])
    f.writelines(lecture_list)
    total = total +section_total
f.close()
print(total)
os.rename(os.getcwd().split('/')[-1]+".txt", os.getcwd().split('/')[-1]+'_'+str(datetime.timedelta(seconds=total)).split('.')[0].replace(':','_')+".csv")
    # f.write("task,"+section+",DESCRIPTION,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE")
    # task,1. Introduction,42:46,4,1,,,,,Asia/Ashgabat
# print(dirs)
# for i in sorted(os.listdir(),key=lambda s: int((re.search(r'\d+', s) or 0))):
#     print(i)
# print(os.listdir())




# import os, re
# import ffmpeg
# is_root = True
# def extract_num(s, p, ret=0):
#     search = p.search(s)
#     if search:
#         return int(search.groups()[0])
#     else:
#         return ret
# p = re.compile(r'(\d+)')
# for address, dirs, files in sorted(os.walk(os.curdir), key=lambda s: int((re.search(r'\d+', s) or 0))):
#     print(f"adress:{address} dirs:{dirs} files:{files}" )
#     # print(address)
#     # if is_root:
#     #     f = open(files[0]+".txt", "w")
#     #     is_root = False
#     #     f.write("TYPE,CONTENT,DESCRIPTION,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE")
#     #     continue
        
#     # try:
#     #     for name in sorted(files, key=lambda s: int(re.search(r'\d+', s).group())):
#     #         if name.split('.')[-1]=='mp4':
#     #             info=ffmpeg.probe(os.path.join(address,name))
#     #             print("\t",name, ' ', info['format']['duration'])
#     #         # info=ffmpeg.probe(os.path.join(address,name))
#     #         # print(f"duration={info['format']['duration']}")
        
#     # except:
#     #     pass