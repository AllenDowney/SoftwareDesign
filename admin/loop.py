import subprocess

repos = [
    'bunyipc',
    'juliebarron',
    'tchoetso',
    'acrease77',
    'zfiddler',
    'adgarrett',
    'mgiolando',
    'cg123',
    'AmbikaGoel',
    'eguthrie',
    'hhansson',
    'skumarasena',
    'JLangowitz',
    'mmahlenk',
    'amuthaOlin',
    'allisongpatterson',
    'JPWS2013',
    'vpreston',
    'ETumang',
    'awilkinson88',
    'Brooks-Willis',
    'morganzhu',
    'DaraBehjat',
]

def run_command(cmd):
    """Runs a command in a subprocess.

    cmd: string
    """
    popen = subprocess.Popen(cmd, shell=True)
    res = popen.communicate()
    return res


def clone():
    for repo in repos:
        s = 'git clone https://github.com/%s/SoftwareDesign.git %s'
        cmd = s % (repo, repo)
        print cmd
        run_command(cmd)


def pull():
    for repo in repos:
        s = 'cd %s; git pull'
        cmd = s % repo
        print cmd
        run_command(cmd)


def run_python(repo, dirname, filename):
    s = 'cd %s/%s; python %s'
    cmd = s % (repo, dirname, filename)
    print cmd
    out, err = run_command(cmd)
    print out
    print err


def hw3():
    for repo in repos:
        run_python(repo, 'chap03', 'grid.py')
        run_python(repo, 'chap04', 'polygon.py')

pull()
