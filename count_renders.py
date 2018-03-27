import os
import csv
import sys
import re
import click



def get_files():
    path = next((obj for obj in sys.argv if "/" in obj), ".")
    regex = re.compile("^renders_\d{4}-\d{2}-\d{2}.csv$")

    try:
        files = [f for f in os.listdir(path) if regex.match(f)]

    except OSError as e:
        print "please enter proper path"
        return e

    if len(files) == 0:
        print "no file exists with the required name format"

    return files



@click.command()
@click.option('-app', required=False,nargs=1, type=str)
@click.option('-renderer',required=False,nargs=1, type=str)
@click.option('-failed', is_flag=True)
@click.option('-avgtime', is_flag=True)
@click.option('-avgcpu', is_flag=True)
@click.option('-avgram', is_flag=True)
@click.option('-maxram', is_flag=True)
@click.option('-maxcpu', is_flag=True)
@click.option('-summary', is_flag=True)
def main(app, renderer, failed, avgtime, avgcpu, avgram, maxcpu, maxram, summary):

    options = {
        'avgtime':'avg_time', 
        'avgcpu': 'avg_cpu', 
        'avgram':'avg_ram', 
        'maxcpu':'max_cpu', 
        'maxram':'max_ram'
    }

    count = 0
    total_time, total_cpu, total_ram, max_ram, max_cpu = 0,0,0,0,0

    conditions = []
    no_option = True


    if app:
        conditions.append("row[1] == app")
    if renderer: 
        conditions.append("row[2] == renderer")
    if not failed:
        conditions.append("row[5].lower() == 'true'")


    condition_str = " and ".join(conditions) or 'True'

    for filename in get_files():
        with open(filename, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                row = [i.decode('utf-8') for i in row] 
                if eval(condition_str):
                    count += 1
                    total_time += int(row[6]) if row[6] else 0
                    total_cpu += float(row[8]) if row[8] else 0
                    total_ram += float(row[7]) if row[7] else 0

                    avg_time = (total_time/(count*1000))
                    avg_cpu = (total_cpu/(count))
                    avg_ram = (total_ram/(count))

                    if row[7] and int(row[7])>max_ram:
                        max_ram = int(row[7]) if row[7] else 0

                    if row[8] and int(row[8])>max_cpu:
                        max_cpu = int(row[8]) if row[8] else 0


    for con, var in options.items():
        if summary or eval(con):
            no_option = False
            answer = eval(var)
            print answer

    if no_option:
        answer = count
        print answer


if __name__ == '__main__':
    main()

