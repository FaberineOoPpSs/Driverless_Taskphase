import csv
import sys

def file_writer():
    dict = {}
    field_name = ['Number', 'Name']
    with open("names.csv", "w", newline = '\r\n') as fl:
        wt = csv.DictWriter(fl, fieldnames = field_name)
        wt.writeheader()
        for i in range(5):
            rec = list(eval(input("Enter Number and Name: ")))
            dict['Number'] = rec[0]
            dict['Name'] = rec[1]
            wt.writerow(dict)

def file_reader():
    field_name = ['Number', 'Name']
    with open("names.csv", "r", newline = '\r\n') as fl:
        re = csv.DictReader(fl)
        
        for i in re:
            print(i)

def file_sort():
    field_name = ['Number', 'Name']
    with open("names.csv", 'r', newline = '\r\n') as fl:
        re = csv.DictReader(fl)
        sort = sorted(re, key = lambda x: x['Number'], reverse = False)
        for i in sort:
            print(i)

def file_mod():
    field = ['Number', 'Names']
    sort_rec = []
    with open("names.csv", 'r', newline = '\r\n') as fl:
        re = csv.reader(fl)
        count = 0
        
        for i in re:
            sort_rec.append(i)
            if count % 2 != 0:
                sort_rec.remove(i)
            count = count + 1
    print('\n')
    with open("names.csv", 'w') as wf:
        wr = csv.writer(wf)
        for i in sort_rec:
            wr.writerow(i)
    with open("names.csv", "r", newline = '\r\n') as fl:
        re = csv.reader(fl)
        for i in re:
            print(i)
def string_manipulation():
    l = []
    with open('names.csv','r',newline = '\r\n') as fl:
        re = csv.reader(fl)
        for i in re:
            str = i[1]
            b = str.replace(' ', '')
            print(b)
            least = abs(ord("z") - ord("A"))
            for x in range(len(b)):
                for y in range(len(b)):
                    t = abs(ord(b[x]) - ord(b[y]))
                    if t < least and t > 0:
                        least = t
            l.append(least)
    l.pop(0)
    print("Least value are: ",l)
def main():
    file_writer()
    print('\n')
    file_reader()
    print('\n')
    file_sort()
    print('\n')
    file_mod()
    string_manipulation()

if __name__ == '__main__':
    main()
