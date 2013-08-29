import sys
import pylab

for filename in sys.argv[1:]:
    print(filename)
    data = pylab.loadtxt(filename)
    c = data[:,0]
    f0 = data[:,1]
    f1 = data[:,2]
    df = f1 - f0

    #x = c**1.34
    #y = df/df[0]
    x = c
    y = df/df[0]
    y = pylab.log10(y)


    
    pylab.figure(1)
    pylab.plot(c,df,'-o')

    pylab.figure(2)
    pylab.plot(x,y,'-o')

pylab.figure(1)
pylab.grid('on')
pylab.xlabel('concentation (ml)')
pylab.ylabel('delta frequency (Hz)')

pylab.figure(2)
pylab.xlabel('concentation (ml)')
pylab.ylabel('backscatter coefficient')
pylab.grid('on')

pylab.show()
