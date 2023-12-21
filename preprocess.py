import csv

def csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r') as csv_input:
        reader = csv.reader(csv_input)
        # 첫 번째 행을 건너뛰기
        next(reader, None)
        with open(txt_file, 'w') as txt_output:
            for row in reader:

                #lable 정의
                mystrtext = row[3]
                # 텍스트 파일에 각 행을 쓰기
                txt_output.write("__label__"+mystrtext)

                #질문 정의
                mystrtext2 = row[1]
                txt_output.write(" " + mystrtext2 + '\n')
                # print(mystrtext2)


csv_filename = 'classification_data_2.csv'
txt_filename = 'reptile_dataset_2.txt'
csv_to_txt(csv_filename, txt_filename)

# 사용 예시
# csv_filename = 'classification_data.csv'
# txt_filename = 'reptile_dataset.txt'
# csv_to_txt(csv_filename, txt_filename)