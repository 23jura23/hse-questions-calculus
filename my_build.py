#!/usr/bin/env python3

import subprocess as su

conspect="""



\\input{core}
\\usepackage{epigraph}
\\usepackage{import}








\\enablemath 

\\begin{document}

\\gdef\\CourseName{Билет %s} 
\\author{Автор1, \\ldots, АвторN} 




\\makegood




\\input{parts/%s/%s}
\\end{document}
"""

ra = [(1, 11), (12, 39), (40, 72), (73, 98), (99, 102)]
na = ['01_integral', '02_metric', '03_series', '04_multivariable', '05_measure']

path = 'src/term2-calculus-questions'
path2 = 'pdf/term2-calculus-questions.pdf'
pdir = 'pdf/separate-q'

su.run(['mkdir', pdir])

for d in range(0, 5):
    for j in range(ra[d][0], ra[d][1]+1):
        s = str(j)
        if j < 10:
            s = '0'+s
        con = conspect % (s, na[d], 'question' + s)
        with open('%s/conspect.tex' % path, 'w') as o:
            o.write(con)
        su.run(['./build.py'])
        rc = su.run(['diff',path2, '%s/question%s.pdf' % (pdir, s)]).returncode
        if rc == 2:
            su.run(['cp', path2, '%s/.question%s_orig.pdf' % (pdir, s)])
            su.run(['mv', path2, '%s/question%s.pdf' % (pdir, s)])
        elif rc == 1:
            rc2 = su.run(['diff', '%s/question%s.pdf' % (pdir, s), '%s/.question%s_orig.pdf' % (pdir, s)]).returncode
            if rc2 == 0:
                su.run(['cp', path2, '%s/.question%s_orig.pdf' % (pdir, s)])
                su.run(['mv', path2, '%s/question%s.pdf' % (pdir, s)])
                print('update %s' % (s))
            else:
                print('cannot change %s: file exists and changed' % (s))
        else:
            print('cannot change %s: file exists and changed' % (s))
        
