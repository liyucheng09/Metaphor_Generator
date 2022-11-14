from glob import glob
import re

if __name__ == '__main__':

    files = glob('CLC_processed/*.txt')
    out_file = open('CLC_processed/processed_sentences.txt', 'w', encoding='utf-8')

    for file in files:
        f = open(file, encoding='utf-8')
        text = f.read(10000)
        remains = ''
        while text:
            text = remains + text
            sentences = re.split(r"(。|！|？)", text)
            if len(sentences) %2 == 0:
                remian = ''
                for i in range(0, len(sentences), 2):
                    sent = sentences[i]+sentences[i+1]
                    if len(sent)<10:
                        continue
                    out_file.write(sent+'\n')
            else:
                remains = sentences[-1]
                for i in range(0, len(sentences)-1, 2):
                    sent = sentences[i]+sentences[i+1]
                    if len(sent)<10:
                        continue
                    out_file.write(sent+'\n')
            text = f.read(10000)
        print(f'Finish spliting {file}.')
        f.close()
    
    out_file.close()
